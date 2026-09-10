#!/usr/bin/env bash
# Pipeline di produzione del CONCEPT M (12,0 s, 300 fotogrammi, con audio SFX): render 2x → Lanczos 970x250 → MP4 master/web (AAC) → MP4 web muto → GIF.
# Uso: bash make_master_M.sh [duration=12] [fps=25]
set -euo pipefail
cd "$(dirname "$0")"
DUR="${1:-12}"; FPS="${2:-25}"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
ROOT=..; PREV=$ROOT/09_preview; EXP=$ROOT/10_export
NAME="BonusSport_970x250_25fps_12s_M"; AUDIO="audio/BonusSport_M_audio_48k.wav"
if [ "${SKIP_RENDER:-0}" != "1" ]; then
rm -rf "$PREV/M_master_frames_2x" "$PREV/M_master_frames" "$PREV/M_gif_frames_2x" "$PREV/M_gif_frames"
echo "[1/7] render 2x (deriva ambiente, per MP4)"
node render_scene.mjs --fps "$FPS" --duration "$DUR" --out "$PREV/M_master_frames_2x" --scale 2 --bgmode drift
echo "[2/7] render 2x (ambiente fermo, per GIF)"
node render_scene.mjs --fps "$FPS" --duration "$DUR" --out "$PREV/M_gif_frames_2x" --scale 2 --bgmode still
else echo "[1-2/7] render saltato (SKIP_RENDER=1): uso i fotogrammi 2x esistenti"; rm -rf "$PREV/M_master_frames" "$PREV/M_gif_frames"; fi
echo "[3/7] downsample Lanczos a 970x250"
mkdir -p "$PREV/M_master_frames" "$PREV/M_gif_frames"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_master_frames_2x/f%04d.png" -vf "scale=970:250:flags=lanczos" "$PREV/M_master_frames/f%04d.png"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_gif_frames_2x/f%04d.png" -vf "scale=970:250:flags=lanczos" "$PREV/M_gif_frames/f%04d.png"
mkdir -p "$EXP" "$EXP/audio"
echo "[4/7] audio: sintesi deterministica (già eseguita) → copia WAV in export"
python3 audio/make_audio.py "$AUDIO" > "$EXP/audio/${NAME}_audio_misura.json"; cp "$AUDIO" "$EXP/audio/${NAME}_audio_48k24.wav"
echo "[5/7] MP4 master (CRF 12, yuv420p, AAC 192k) + archivio yuv444p"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_master_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 12 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$EXP/${NAME}_MASTER.mp4"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_master_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 10 -pix_fmt yuv444p -c:a pcm_s24le -shortest "$EXP/${NAME}_MASTER_444_archivio.mov"
echo "[6/7] MP4 web (CRF 17, AAC 128k, ≤ 3,5 MB) + MP4 web MUTO"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_master_frames/f%04d.png" -i "$AUDIO" -c:v libx264 -preset veryslow -crf 17 -profile:v high -level 4.0 -pix_fmt yuv420p -c:a aac -b:a 128k -shortest -movflags +faststart "$EXP/${NAME}_WEB.mp4"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_master_frames/f%04d.png" -c:v libx264 -preset veryslow -crf 17 -profile:v high -level 4.0 -pix_fmt yuv420p -an -movflags +faststart "$EXP/${NAME}_WEB_MUTO.mp4"
echo "[7/7] GIF di controllo (ambiente fermo, muta)"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_gif_frames/f%04d.png" -vf "fps=$FPS,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"
GIFSZ=$(stat -c %s "$EXP/${NAME}_CONTROL.gif")
if [ "$GIFSZ" -gt 3500000 ]; then
  echo "GIF a 25 fps = $GIFSZ byte > 3,5 MB → fallback 12,5 fps"
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/M_gif_frames/f%04d.png" -vf "fps=12.5,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/${NAME}_CONTROL.gif"
fi
cp "$PREV/M_master_frames/f0300.png" "$EXP/${NAME}_ENDFRAME_fallback_statico.png"
ls -la "$EXP"
