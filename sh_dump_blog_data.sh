#!/bin/bash

# --------------------------------------------------------
# Before stopping container , we need to dump_data (Hence we don't know why through db_data we cannot resore myql table's data)
# 
# The creadted dumped file will be : $HOME/PROJETS_PERSONNELS/GIT_RESPONSIBLE_BLOG/backup.sql
#
# --------------------------------------------------------

RESET="\e[0m"
RED="\e[31m"
GREEN="\e[32m"
CYAN="\e[36m"
LGRAY="\e[36m"

#INIT_SQL_FILE="$HOME/PROJETS_PERSONNELS/GIT_RESPONSIBLE_BLOG/mysql_dir/queries/init.sql"
DUMPED_SQL_FILE="$HOME/PROJETS_PERSONNELS/GIT_RESPONSIBLE_BLOG/backup.sql"
DOCKERS_QUERIES_DIR="/docker-entrypoint-initdb.d/queries"

docker exec -it responsive_mysql_cont /bin/bash -c "mysqldump -u root -p  mydb > $DOCKERS_QUERIES_DIR/backup.sql"

rm -rf $HOME/PROJETS_PERSONNELS/GIT_RESPONSIBLE_BLOG/backup.sql 2>/dev/null

docker cp responsive_mysql_cont:$DOCKERS_QUERIES_DIR/backup.sql $DUMPED_SQL_FILE

# Check if the backup file is empty
DUMPED_FILE_INFO=$(ls -lrt $DUMPED_SQL_FILE 2>/dev/null)
if [ -z "$DUMPED_FILE_INFO" ]; then
    echo -e "$RED Failed to dump data $CYAN Please relaunch the same command again\n"
else
    echo -e "\n[$GREEN SUCCESS $RESET]:\n$LGRAY $DUMPED_FILE_INFO $RESET\n"
fi
