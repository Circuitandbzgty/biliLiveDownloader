ffmpeg -i muxvideo_hls.mp4corrupted -codec copy -movflags faststart -f mp4 muxvideo_hls_finalfix.mp4
rm *.mp4corrupted