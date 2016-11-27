foldername=$(date +%Y-%m-%d-%H:%M:%S)
mkdir -p "$foldername"
echo "Lets take the readings"
echo "Lets start with the current direction[0]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/0degree" &
sleep 5
kill -9 $!

echo "Turn 45 degrees to the left[45]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/45degree" &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[90]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/90degree" &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[135]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/135degree" &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[180]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/180degree" &
sleep 5
kill -9 $!


echo "Turn 45 degrees to the left[225]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/225degree" &
sleep 5
kill -9 $!

echo "Turn 45 degrees to the left[270]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/270degree" &
sleep 5
kill -9 $!

echo "Turn 45 degrees to the left[315]"
echo "Press any  key to start"
read -n 1 -s
. ./run.sh fire > "$foldername/315degree" &
sleep 5
kill -9 $!

echo "readings have been collected"
