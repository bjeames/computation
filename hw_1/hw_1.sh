#!/bin/sh 

url=$1
folder=$2

if [ $# != 2 ]

then
    echo "Please check the format.\nExample: "sh ./hw1.sh git_url folder_path""
    exit
fi

echo "Checking if $folder exists"

if [ -e $folder ]
then
    echo "$folder exists"
    echo "updating $folder"
    cd $folder
    git pull $url || { 
        echo  "Failed to pull from $url to $folder"
        exit
    }
    echo "Success: Pulled from $url to $folder"
    ls -la
else
    echo "$folder does not exist"
    echo "cloning $folder"
    git clone $url || {
        echo "Failed to clone from $url to $folder"
        exit
    }
    echo "Success: Cloned from $url to $folder"
    cd $folder
    ls -la
fi