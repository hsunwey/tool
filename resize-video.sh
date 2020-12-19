videos=$(find -name "*.mp4" -size +700M); for i in $videos;  do  echo $i; mv $i $i.mp4; ffmpeg -i $i.mp4 -s 850x480 -c:a copy $i -hide_banner -loglevel panic; done

videos=$(find -name "*.mp4" -size +700M)
for i in $videos;
 do
 ffmpeg -i $i -s 850x480 -c:a copy $i.mp4;
done

# find -size +700M
