# Shell script to initialize local and 
# external directories and
# set up cron job 
git clone https://github.com/scaredyspacecat/bloomsync.git "bloomsync"
cd bloomsync
python3 -v

if [$?==1]
  exit
fi

read -p "Local directory: " local
read -p "External directory: " external

python3 ./src/main.py -l ${local} -e ${external}
python3 ./src/main.py --sync now 
