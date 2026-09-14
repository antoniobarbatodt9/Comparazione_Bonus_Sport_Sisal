#!/usr/bin/env bash
# Produzione famiglia orizzontale (10,0 s, 250 f, 25 fps, CON audio): render 2x → Lanczos → MP4 master/web (AAC) + web MUTO → GIF → end-frame.
# Uso: bash make_horizontal.sh <size> [duration=10] [fps=25]     (SKIP_RENDER=1 per riusare i frame 2x)
# 1920x1080: WEB.mp4 con CRF crescente fino a ≤ 3,5 MB (se CRF 17 supera la soglia resta come WEB_HQ.mp4, dichiarato fuori soglia);
#            GIF di controllo a 720x405 / 10 fps da una sequenza "fermo" resa a 1x (una GIF 1920x1080, e anche 960x540, di 10 s non sta in 3,5 MB: 960x540 a 8 fps = 5,2 MB).
set -euo pipefail
cd "$(dirname "$0")"
SIZE="$1"; DUR="${2:-10}"; FPS="${3:-25}"; W="${SIZE%x*}"; H="${SIZE#*x}"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
ROOT=../../..; PREV=$ROOT/09_preview/horizontal; EXP=$ROOT/10_export/horizontal
NAME="BonusSport_${SIZE}_25fps_10s_M"; AUDIO=$ROOT/08_progetto/audio/BonusSport_H_audio_48k.wav
mkdir -p "$PREV" "$EXP" "$EXP/audio"
[ -f "$AUDIO" ] || python3 $ROOT/08_progetto/audio/make_audio.py "$AUDIO" --profile horizontal > "$EXP/audio/BonusSport_horizontal_audio_misura.json"
cp "$AUDIO" "$EXP/audio/BonusSport_horizontal_audio_48k24.wav"
BIG=0; [ "$W" -gt 1000 ] && BIG=1
if [ "${SKIP_RENDER:-0}" != "1" ]; then
  rm -rf "$PREV/${SIZE}_2x" "$PREV/${SIZE}_gif_2x" "$PREV/${SIZE}_gif_1x"
  echo "[1/6] $SIZE render 2x (deriva)";  node render_horizontal.mjs --size "$SIZE" --fps "$FPS" --duration "$DUR" --out "$PREV/${SIZE}_2x" --scale 2 --bgmode drift
  if [ "$BIG" = 1 ]; then echo "[2/6] $SIZE render 1x 10 fps (fermo, GIF 720x405)"; node render_horizontal.mjs --size "$SIZE" --fps 10 --duration "$DUR" --out "$PREV/${SIZE}_gif_1x" --scale 1 --bgmode still
  else echo "[2/6] $SIZE render 2x (fermo, GIF)"; node render_horizontal.mjs --size "$SIZE" --fps "$FPS" --duration "$DUR" --out "$PREV/${SIZE}_gif_2x" --scale 2 --bgmode still; fi
fi
echo "[3/6] downsample Lanczos ${W}x${H}"
rm -rf "$PREV/${SIZE}_frames" "$PREV/${SIZE}_gif_frames"; mkdir -p "$PREV/${SIZE}_frames" "$PREV/${SIZE}_gif_frames"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_2x/f%04d.png" -vf "scale=${W}:${H}:flags=lanczos" "$PREV/${SIZE}_frames/f%04d.png"
if [ "$BIG" = 1 ]; then "$FF" -y -loglevel error -framerate 10 -i "$PREV/${SIZE}_gif_1x/f%04d.png" -vf "scale=$((W*3/8)):$((H*3/8)):flags=lanczos" "$PREV/${SIZE}_gif_frames/f%04d.png"
else "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_2x/f%04d.png" -vf "scale=${W}:${H}:flags=lanczos" "$PREV/${SIZE}_gif_frames/f%04d.png"; fi
echo "[4/6] MP4 master (CRF 12, AAC 192k) + archivio 444 (PCM 24 bit)"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 12 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$EXP/${NAME}_MASTER.mp4"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 10 -pix_fmt yuv444p -c:a pcm_s24le -shortest "$EXP/${NAME}_MASTER_444_archivio.mov"
echo "[5/6] MP4 web (≤ 3,5 MB, AAC 128k) + MP4 web MUTO"
rm -f "$EXP/${NAME}_WEB_HQ.mp4"
CRFS="17 19 21 23 25 27"; [ "$BIG" = 0 ] && CRFS="12 14 17 19 21 23"
for CRF in $CRFS; do
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf $CRF -profile:v high -level 4.1 -pix_fmt yuv420p -c:a aac -b:a 128k -shortest -movflags +faststart "$EXP/${NAME}_WEB.mp4"
  SZ=$(stat -c %s "$EXP/${NAME}_WEB.mp4"); echo "  WEB CRF $CRF = $SZ byte"
  if [ "$SZ" -le 3500000 ]; then WEBCRF=$CRF; break; fi
  if [ "$CRF" = 17 ] && [ "$BIG" = 1 ]; then cp "$EXP/${NAME}_WEB.mp4" "$EXP/${NAME}_WEB_HQ.mp4"; echo "  CRF 17 > 3,5 MB: conservato come WEB_HQ.mp4 (fuori soglia)"; fi
done
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -c:v libx264 -preset veryslow -crf $WEBCRF -profile:v high -level 4.1 -pix_fmt yuv420p -an -movflags +faststart "$EXP/${NAME}_WEB_MUTO.mp4"
echo "$WEBCRF" > "$EXP/${NAME}_WEB_crf.txt"
echo "[6/6] GIF di controllo"
GFPS=$FPS; [ "$BIG" = 1 ] && GFPS=10
"$FF" -y -loglevel error -framerate "$GFPS" -i "$PREV/${SIZE}_gif_frames/f%04d.png" -vf "fps=$GFPS,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"
GIFSZ=$(stat -c %s "$EXP/${NAME}_CONTROL.gif")
if [ "$GIFSZ" -gt 3500000 ] && [ "$BIG" = 0 ]; then echo "GIF 25 fps = $GIFSZ > 3,5 MB → 12,5 fps"
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_frames/f%04d.png" -vf "fps=12.5,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"; fi
GIFSZ=$(stat -c %s "$EXP/${NAME}_CONTROL.gif")
if [ "$GIFSZ" -gt 3500000 ]; then echo "GIF = $GIFSZ > 3,5 MB → 8/10 fps"
  R=10; [ "$BIG" = 1 ] && R=8
  "$FF" -y -loglevel error -framerate "$GFPS" -i "$PREV/${SIZE}_gif_frames/f%04d.png" -vf "fps=$R,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"; fi
LAST=$(printf "f%04d.png" $((FPS*DUR-1)))
cp "$PREV/${SIZE}_frames/$LAST" "$EXP/${NAME}_ENDFRAME_fallback_statico.png"

if [ "$BIG" = 0 ]; then
  W2=$((W*2)); H2=$((H*2)); N2="${NAME}_2x_${W2}x${H2}"
  echo "[7/7] varianti 2x (${W2}x${H2}, per schermi HiDPI / anteprima su PC): MP4 web + muto + GIF, ≤ 3,5 MB"
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_2x/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 12 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$EXP/${N2}_MASTER.mp4"
  for CRF in 12 14 15 17 19 21 23; do
    "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_2x/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf $CRF -profile:v high -level 4.1 -pix_fmt yuv420p -c:a aac -b:a 128k -shortest -movflags +faststart "$EXP/${N2}_WEB.mp4"
    SZ=$(stat -c %s "$EXP/${N2}_WEB.mp4"); echo "  WEB 2x CRF $CRF = $SZ byte"; if [ "$SZ" -le 3500000 ]; then WEBCRF2=$CRF; break; fi
  done
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_2x/f%04d.png" -c:v libx264 -preset veryslow -crf $WEBCRF2 -profile:v high -level 4.1 -pix_fmt yuv420p -an -movflags +faststart "$EXP/${N2}_WEB_MUTO.mp4"
  echo "$WEBCRF2" > "$EXP/${N2}_WEB_crf.txt"
  # GIF 2x: prima a risoluzione doppia riducendo il frame-rate (25 → 12,5 → 10 → 8); se non basta, a 1,5x (12,5 → 10 → 8 fps)
  rm -f "$EXP/${N2}_CONTROL_gif_fps.txt"; GIFOK=0
  for SC in 2 1.5; do
    GW=$(python3 -c "print(int($W*$SC))"); GH=$(python3 -c "print(int($H*$SC))"); SF="scale=${GW}:${GH}:flags=lanczos,"; [ "$SC" = 2 ] && SF=""
    RATES="25 12.5 10 8"; [ "$SC" = 1.5 ] && RATES="12.5 10 8"
    for R in $RATES; do
      "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_2x/f%04d.png" -vf "fps=$R,${SF}split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${N2}_CONTROL.gif"
      SZ=$(stat -c %s "$EXP/${N2}_CONTROL.gif"); echo "  GIF 2x ${GW}x${GH} $R fps = $SZ byte"
      if [ "$SZ" -le 3500000 ]; then rm -f "$EXP/${NAME}_"*"x_"*"_CONTROL.gif" "$EXP/${NAME}_"*"x_"*"_CONTROL_gif_fps.txt"; mv "$EXP/${N2}_CONTROL.gif" "$EXP/${NAME}_${SC}x_${GW}x${GH}_CONTROL.gif"; echo "${GW}x${GH} @ $R fps" > "$EXP/${NAME}_${SC}x_${GW}x${GH}_CONTROL_gif_fps.txt"; GIFOK=1; break; fi
    done
    [ "$GIFOK" = 1 ] && break
  done
  cp "$PREV/${SIZE}_2x/$LAST" "$EXP/${N2}_ENDFRAME_fallback_statico.png"
fi
ls -la "$EXP" | grep "$SIZE"
echo "ALL_DONE $SIZE"
