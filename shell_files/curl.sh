set -a

tyr="$1" # to give input from outside
ert="trest" # to declare variable

if [-n $tyr]; then
    echo "why $ert $tyr" | grep "where" >> ./output.txt # every time it will append this statement if it contains "where" word to output.txt
fi
# looping through test_curl.txt file and creating a variable named curl
# while read line; do
#     echo line
#     curl="$curl\n$line"
# done < ./test_curl.txt
file_location="./test_curl.txt"
cat $file_location
curl=$(cat $file_location)
# echo $curl
# executing curl and saving the response in curl_response.txt
eval $curl >> curl_response.txt




# curl -L -X GET -o ./output.txt 'http://127.0.0.1:8040/query/1' \
# -H 'X-Digio-Checksum: 9876543210' \
# -H 'Content-Type: application/json'


# curl -L -X POST 'http://127.0.0.1:8040/query/' \
# -H 'X-Digio-Checksum: 9876543210' \
# -H 'Content-Type: application/json' \
# --data-raw '{
#     "query": "what is not not possible",
#     "language": "danish"
# }'
