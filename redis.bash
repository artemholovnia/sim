REDIS_WORKDIR=/home/artemholovnia/artemholovnia/project/redis-server/
REDIS_CONF=redis.conf
fuser -k 7000/tcp
#pkill -f redis-server
redis-server $REDIS_WORKDIR$REDIS_CONF
