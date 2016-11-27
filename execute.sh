foldername=$(date +%Y-%m-%d-%H:%M:%S)
mkdir -p "$foldername"
echo "Lets take the readings"
echo "Lets start with the current direction[0]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/0degree" > /dev/null &
sleep 5
kill -9 $!

echo "Turn 45 degrees to the left[45]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/45degree" > /dev/null &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[90]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/90degree" > /dev/null &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[135]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/135degree" >/dev/null &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[180]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/180degree" >/dev/null &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[225]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/225degree" >/dev/null &
sleep 5
kill -9 $!

echo "Turn 45 degrees to the left[270]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/270degree" > /dev/null &
sleep 5
kill -9 $!

echo "Turn 45 degrees to the left[315]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh "$foldername/315degree" > /dev/null &
sleep 5
kill -9 $!

echo "readings have been collected"
#cp "radio.py" $foldername
#cd $foldername

python2 radio.py $foldername
