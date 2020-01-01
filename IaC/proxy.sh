#! /bin/bash

INSTANCE=$1
echo "Connecting to instance: ${INSTANCE}"
[ "$1" = "" ] && echo "Please supply database instance" && exit 255
CONNECTION=`gcloud sql instances describe $INSTANCE | grep conn | awk '{print $2}'`
echo Connection address: $CONNECTION
cloud_sql_proxy -instances=$CONNECTION=tcp:5432
