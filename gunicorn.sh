#!/bin/bash
set -e
LOGFILE=/home/admin/Workspace/pando/pando/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=1
# user/group to run as
USER=root
GROUP=root
ADDRESS=127.0.0.1:8000
cd /home/admin/Workspace/pando/pando
source /home/admin/Workspace/pando/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django pando -w $NUM_WORKERS --bind=$ADDRESS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE
