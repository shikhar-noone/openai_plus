curr_date=$(date)
ct=4
ct=$(($ct+2))
echo $ct
echo $curr_date
sleep 2




#!/bin/bash

# Define two dates in the "YYYY-MM-DD" format
date1=$curr_date
date2=$(date +"%H:%M:%S")
echo $date1 $date2
# Convert dates to seconds since the epoch
seconds1=$(($date1 +%s))
seconds2=$(($date2 +%s))

echo $seconds1 $seconds2

# Add the two date values in seconds
result_seconds=$((seconds1 + seconds2))

# Convert the result back to a human-readable format
result_date=$(date -d "@$result_seconds" +"%Y-%m-%d")

echo "Result Date: $result_date"
