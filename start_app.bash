APP_PORT=8000
WORK_DIRECTORY=/home/artemholovnia/artemholovnia/project/sim/
REDIS_START=/home/artemholovnia/artemholovnia/project/redis.bash
CELERY_START=/home/artemholovnia/artemholovnia/project/celery.bash
VEVN=/home/artemholovnia/artemholovnia/project/venv/bin/activate

sudo fuser -k $APP_PORT

source $VENV
cd $WORK_DIRECTORY
python3 manage.py runserver $APP_PORT
echo "App on port $APP_PORT started"

. $REDIS_START
. $CELERY_START


