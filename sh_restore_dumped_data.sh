#!/bin/bash

# --------------------------------------------------------
# AFter restaring container , you won't lost data because
# You dumped them inside script sh_dump_blog_data.sh
#
# Now, you can restore those data o container. You will see
# The articles you have already writen.
# 
# Hince!: I don' know why the volume db_data don't prsist it
#         Through: db_bd:/var/lib/mysql/
# We must investigate to know why.
# --------------------------------------------------------

RESET="\e[0m"
RED="\e[31m"
GREEN="\e[32m"
CYAN="\e[36m"
LGRAY="\e[36m"

DUMPED_SQL_FILE="$HOME/PROJETS_PERSONNELS/GIT_RESPONSIBLE_BLOG/backup.sql"
DOCKERS_QUERIES_DIR="/docker-entrypoint-initdb.d/queries"

# Remove old backup [If exists]
DOCKERS_QUERIES_DIR="/docker-entrypoint-initdb.d/queries"
docker exec -it responsive_mysql_cont /bin/bash -c "rm -rf $DOCKERS_QUERIES_DIR/backup.sql"

docker cp $DUMPED_SQL_FILE responsive_mysql_cont:$DOCKERS_QUERIES_DIR/backup.sql

# Check the nw created backup.sql
docker exec -it responsive_mysql_cont /bin/bash -c "ls -lrt $DOCKERS_QUERIES_DIR/backup.sql"

## -- RUN HIS INSIDE mysql_cont
# mysql -u root -p mydb < docker-entrypoint-initdb.d/queries/backup.sql;