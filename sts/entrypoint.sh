#!/bin/bash

echo "Waiting for db..."

while !</dev/tcp/$DATABASE_HOST/$DATABASE_PORT; do
    sleep 0.1
done 2>/dev/null
sleep 2

echo "DB Started"

exec "$@"
