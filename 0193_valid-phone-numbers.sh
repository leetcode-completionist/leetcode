# Read from the file file.txt and output all valid phone numbers to stdout.
while read -r number; do
    if [[ $number =~ ^\([0-9]{3}\)\ [0-9]{3}-[0-9]{4}$ ]]; then
        echo $number
    elif [[ $number =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
        echo $number
    fi
done < file.txt
