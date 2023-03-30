du -skc $FS | grep total | awk '{print $1;}' > $FS/size.txt 
