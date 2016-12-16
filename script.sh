FOLDER="./"
FOL="$FOLDER$1"
OUT=`ls $FOL|grep 2016`
for f in $OUT
do
    FILE="$FOL/$f"
    echo "Processing $FILE"
    python2 radio.py $FILE
done
