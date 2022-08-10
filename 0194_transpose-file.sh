# Read from the file file.txt and print its transposed content to stdout.
declare -A transposed

nrows=0
ncols=0

while read -r -a row; do
    # read each row
    for ((i = 0; i < ${#row[@]}; i++)); do
        # for each word in the row
        # set it as transposed on a 2D
        # table
        transposed[$i,$nrows]=${row[i]}
    done
    
    # increase our row count
    ((nrows++))
    
    # update total number of columns
    ncols=${#row[@]}
done < file.txt

for ((i = 0; i < ncols; i++)); do
    # no delimiter for the first word
    delimiter=""
    for ((j = 0; j < nrows; j++)); do
        printf '%s%s' "$delimiter" "${transposed[$i,$j]}"
        
        # delimiter after the first word
        delimiter=" "
    done
    
    # new line for the next row
    printf '\n'
done
