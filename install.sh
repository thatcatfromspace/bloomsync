# Shell script to initialize local and 
# external directories and
# set up cron job 
read -p "Local directory: " local

python3 /home/dinesh/code/bloomsync/src/main.py ${local} 