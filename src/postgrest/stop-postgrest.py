sudo systemctl stop postgrest
exit 0

now=`date`

pid=`ps aux | grep [p]ostgrest.conf | awk '{print $2}'`
if [ "$pid" > " " ]; then
  msg="postgrest stopping"
  echo $msg
  echo "$msg - $now" >> data/logs/postgrest/postgrest.log
  kill -9 $pid > /dev/null 2>&1
else
  echo "postgrest stopped"
fi

##pid=`ps aux | grep 'npm exec http.server' | awk '{print $2}'`
##if [ "$pid" > " " ]; then
##  msg="swagger  stopping"
##  echo $msg
##  echo "$msg - $now" >> data/logs/postgrest/swagger.log
##  kill -9 $pid > /dev/null 2>&1
##else
##  echo "swagger stopped"
##fi

exit 0
