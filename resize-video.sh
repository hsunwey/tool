videos=$(find -name "*.mp4" -size +700M)

for i in $videos;
 do
 ffmpeg -i $i -s 850x480 -c:a copy $i.mp4;
done
