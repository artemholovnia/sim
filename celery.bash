CELERY_WORKDIR=/home/artemholovnia/artemholovnia/project/celery/
APP_DIR=/home/artemholovnia/artemholovnia/project/sim/
APP=sim
VENV=/home/artemholovnia/artemholovnia/project/venv/bin/activate

BEAT_PID=beat.pid
WORKER_PID=worker.pid
BEATSCHEDULE=beat_schedule
LOGLEVEL=DEBUG
CONCURRENCY=4
BEAT_LOG=beat.log
WORKER_LOG=worker.log

pkill -f celery
rm -rf $CELERY_WORKDIR$BEAT_PID $CELERY_WORKDIR$WORKER_PID $CELERY_WORKDIR$BEATSCHEDULE
. $VENV
cd $APP_DIR
celery worker -A $APP --detach --loglevel=$LOGLEVEL --logfile=$CELERY_WORKDIR$WORKER_LOG --pidfile=$CELERY_WORKDIR$WORKER_PID --concurrency=$CONCURRENCY
celery beat -A $APP --detach --loglevel=$LOGLEVEL --logfile=$CELERY_WORKDIR$BEAT_LOG --pidfile=$CELERY_WORKDIR$BEAT_PID --schedule=$CELERY_WORKDIR$BEATSCHEDULE
