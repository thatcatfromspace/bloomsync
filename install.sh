# Shell script to initialize local and 
# external directories and
# set up cron job 
# read -p "Local directory: " local

# python3 /home/dinesh/code/bloomsync/src/main.py ${local} 

mkdir -p ~/.bloomsync 
touch ~/dirs.json
cp ./dirs_default.json ~/.bloomsync/dirs.json 
touch ~/.bloomsync/sync.log
