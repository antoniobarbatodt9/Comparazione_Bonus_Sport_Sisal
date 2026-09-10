#!/usr/bin/env bash
# Pipeline di produzione (dopo approvazione): render 2x → downsample Lanczos → MP4 master, MP4 web, GIF di controllo.
# Uso: bash make_master.sh <bg_image_path_relative_to_08_progetto> [duration=9] [fps=25]
set -euo pipefail
cd "$(dirname "$0")"
BG="${1:-assets/env/env_A_pitch_FINAL.jpg}"; DUR="${2:-9}"; FPS="${3:-25}"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
ROOT=..; PREV=$ROOT/09_preview; EXP=$ROOT/10_export
NAME="BonusSport_970x250_25fps_9s"
rm -rf "$PREV/master_frames_2x" "$PREV/master_frames" "$PREV/gif_frames_2x" "$PREV/gif_frames"
echo "[1/6] render 2x (drift, per MP4)"
node render.mjs --fps "$FPS" --duration "$DUR" --out "$PREV/master_frames_2x" --bg "$BG" --scale 2 --bgmode drift
echo "[2/6] render 2x (ambiente fermo, per GIF)"
node render.mjs --fps "$FPS" --duration "$DUR" --out "$PREV/gif_frames_2x" --bg "$BG" --scale 2 --bgmode still
echo "[3/6] downsample Lanczos a 970x250"
mkdir -p "$PREV/master_frames" "$PREV/gif_frames"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/master_frames_2x/f%04d.png" -vf "scale=970:250:flags=lanczos" "$PREV/master_frames/f%04d.png"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/gif_frames_2x/f%04d.png" -vf "scale=970:250:flags=lanczos" "$PREV/gif_frames/f%04d.png"
mkdir -p "$EXP"
echo "[4/6] MP4 master (CRF 12, yuv420p) + copia archivio yuv444p"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/master_frames/f%04d.png" -c:v libx264 -preset veryslow -crf 12 -pix_fmt yuv420p -movflags +faststart -an "$EXP/${NAME}_MASTER.mp4"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/master_frames/f%04d.png" -c:v libx264 -preset veryslow -crf 10 -pix_fmt yuv444p -an "$EXP/${NAME}_MASTER_444_archivio.mp4"
echo "[5/6] MP4 web (CRF 17, ≤ 3,5 MB)"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/master_frames/f%04d.png" -c:v libx264 -preset veryslow -crf 17 -profile:v high -level 4.0 -pix_fmt yuv420p -movflags +faststart -an "$EXP/${NAME}_WEB.mp4"
echo "[6/6] GIF di controllo (ambiente fermo)"
"$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/gif_frames/f%04d.png" -vf "fps=$FPS,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/BonusSport_970x250_CONTROL.gif"
GIFSZ=$(stat -c %s "$EXP/BonusSport_970x250_CONTROL.gif")
if [ "$GIFSZ" -gt 3500000 ]; then
  echo "GIF a 25 fps = $GIFSZ byte > 3,5 MB → fallback 12,5 fps"
  "$FF" -y -loglevel error -framerate "$FPS" -i "$PREV/gif_frames/f%04d.png" -vf "fps=12.5,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$EXP/BonusSport_970x250_CONTROL.gif"
fi
cp "$PREV/master_frames/f0224.png" "$EXP/${NAME}_ENDFRAME_fallback_statico.png"
ls -la "$EXP"
