videos=$(find -name "*.mp4" -size +700M); for i in $videos;  do  echo $i; mv $i $i.mp4; ffmpeg -i $i.mp4 -s 850x480 -c:a copy $i -hide_banner -loglevel panic; done

OIFS="$fileFS"
IFS=$'\n'
for file in `find . -type f -name "*.mp4" -size +800M`  
do
     echo "$file";
     mv "$file" "$file.mp4";
     ffmpeg -i "$file.mp4" -s 850x480 -c:a copy "$file" -hide_banner -loglevel panic;
done
IFS="$OIFS"


# find -size +700M

# videos=($(find -name "*.mp4" -size +700M));
# for index in ${!videos[@]}; do
#     echo $((index+1))/${#videos[@]} = "${videos[index]}";
#     mv $i $i.mp4;
#     ffmpeg -i $i -s 850x480 -c:a copy $i -hide_banner -loglevel panic;
# done
