
apk --no-cache add inotify-tools

# here every change will be registered and we have to restart the server
# but on every change we can not restart, so we will put it to sleep for a min and 
# let's see how it works 
count=1
while inotifywait -e modify,create,delete,move -r /app/openai_plus; do 
    echo "restarting the server" && 
    sleep 60 &&
    echo "count of restarts $count" &&
    count=$((count+1)) &&
    docker restart openai_container &&
    echo "connection restablish"
done

echo "My watch has ended"