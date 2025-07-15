#!/bin/sh

url="$1"
folder="$2"

# Check number of arguments
if [ "$#" -ne 2 ]; then
    printf "Usage:\n  sh ./hw1.sh git_url folder_name\n"
    exit 1
fi

echo "Checking if '$folder' exists"

# Define a function to list folder contents
list_folder_contents() {
    echo "Contents of '$folder':"
    ls -l
}

if [ -e "$folder" ]; then
    echo "'$folder' exists"
    echo "Updating '$folder'"
    cd "$folder" || { echo "Failed to cd into '$folder'"; exit 1; }
    git pull "$url" || { echo "Failed to pull from $url"; exit 1; }
    echo "Success: Pulled from $url"
    list_folder_contents
else
    echo "'$folder' does not exist"
    echo "Cloning into '$folder'"
    git clone "$url" "$folder" || { echo "Failed to clone from $url"; exit 1; }
    echo "Success: Cloned from $url"
    cd "$folder" || { echo "Failed to cd into '$folder' after cloning"; exit 1; }
    list_folder_contents
fi
