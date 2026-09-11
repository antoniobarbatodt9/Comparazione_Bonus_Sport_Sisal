#!/usr/bin/env bash
# Produzione famiglia verticale (10,0 s, 250 f, 25 fps, CON audio: bed stadio + SFX ri-temporizzati): render 2x → Lanczos → MP4 master/web (AAC) + web MUTO → GIF → end-frame.
# Uso: bash make_vertical.sh <size> [duration=10] [fps=25]     (SKIP_RENDER=1 per riusare i frame 2x)
set -euo pipefail
cd "$(dirname "$0")"
SIZE="$1"; DUR="${2:-10}"; FPS="${3:-25}"; W="${SIZE%x*}"; H="${SIZE#*x}"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
ROOT=../../..; PREV=$ROOT/09_preview/vertical; EXP=$ROOT/10_export/vertical
NAME="BonusSport_${SIZE}_25fps_10s_M"; AUDIO=$ROOT/08_progetto/audio/BonusSport_V_audio_48k.wav
mkdir -p "$PREV" "$EXP" "$EXP/audio"
[ -f "$AUDIO" ] || python3 $ROOT/08_progetto/audio/make_audio.py "$AUDIO" --profile vertical > "$EXP/audio/BonusSport_vertical_audio_misura.json"
cp "$AUDIO" "$EXP/audio/BonusSport_vertical_audio_48k24.wav"
if [ "${SKIP_RENDER:-0}" != "1" ]; then
  rm -rf "$PREV/${SIZE}_2x" "$PREV/${SIZE}_gif_2x"
  echo "[1/6] $SIZE render 2x (deriva)";  node render_vertical.mjs --size "$SIZE" --fps "$FPS" --duration "$DUR" --out "$PREV/${SIZE}_2x" --scale 2 --bgmode drift
  echo "[2/6] $SIZE render 2x (fermo, GIF)"; node render_vertical.mjs --size "$SIZE" --fps "$FPS" --duration "$DUR" --out "$PREV/${SIZE}_gif_2x" --scale 2 --bgmode still
fi
echo "[3/6] downsample Lanczos ${W}x${H}"
rm -rf "$PREV/${SIZE}_frames" "$PREV/${SIZE}_gif_frames"; mkdir -p "$PREV/${SIZE}_frames" "$PREV/${SIZE}_gif_frames"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_2x/f%04d.png" -vf "scale=${W}:${H}:flags=lanczos" "$PREV/${SIZE}_frames/f%04d.png"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_2x/f%04d.png" -vf "scale=${W}:${H}:flags=lanczos" "$PREV/${SIZE}_gif_frames/f%04d.png"
echo "[4/6] MP4 master (CRF 12, AAC 192k) + archivio 444 (PCM 24 bit)"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 12 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$EXP/${NAME}_MASTER.mp4"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 10 -pix_fmt yuv444p -c:a pcm_s24le -shortest "$EXP/${NAME}_MASTER_444_archivio.mov"
echo "[5/6] MP4 web (CRF 17, AAC 128k, ≤ 3,5 MB) + MP4 web MUTO"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 17 -profile:v high -level 4.0 -pix_fmt yuv420p -c:a aac -b:a 128k -shortest -movflags +faststart "$EXP/${NAME}_WEB.mp4"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_frames/f%04d.png" -c:v libx264 -preset veryslow -crf 17 -profile:v high -level 4.0 -pix_fmt yuv420p -an -movflags +faststart "$EXP/${NAME}_WEB_MUTO.mp4"
echo "[6/6] GIF di controllo"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_frames/f%04d.png" -vf "fps=$FPS,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"
GIFSZ=$(stat -c %s "$EXP/${NAME}_CONTROL.gif")
if [ "$GIFSZ" -gt 3500000 ]; then echo "GIF 25 fps = $GIFSZ > 3,5 MB → 12,5 fps"
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_frames/f%04d.png" -vf "fps=12.5,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"; fi
GIFSZ=$(stat -c %s "$EXP/${NAME}_CONTROL.gif")
if [ "$GIFSZ" -gt 3500000 ]; then echo "GIF 12,5 fps = $GIFSZ > 3,5 MB → 10 fps"
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/${SIZE}_gif_frames/f%04d.png" -vf "fps=10,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"; fi
LAST=$(printf "f%04d.png" $((FPS*DUR-1)))
cp "$PREV/${SIZE}_frames/$LAST" "$EXP/${NAME}_ENDFRAME_fallback_statico.png"
ls -la "$EXP" | grep "$SIZE"
