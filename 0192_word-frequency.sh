# Read from the file words.txt and output the word frequency list to stdout.
declare -A array
readarray -t words < words.txt
for w in ${words[@]}; do
    if [ -v 'array[i]' ];then
        array[$w]=0
    else
        ((array[$w]+=1))
    fi
done

for key in "${!array[@]}"; do
    echo $key ${array[$key]}
done | sort -k 2nr
