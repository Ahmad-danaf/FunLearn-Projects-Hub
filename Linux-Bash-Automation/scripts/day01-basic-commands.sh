#!/bin/bash

echo "===================================="
echo "==============DAY ONE==============="
echo "===================================="

echo "creating the folders"
mkdir -p output/day01/{projects,backup}

echo "creating the files"
touch output/day01/projects/{notes.txt,script.sh}

echo "adding a new line"
echo "Hello World!" > output/day01/projects/notes.txt

echo "copy&rename"
cp -v output/day01/projects/notes.txt output/day01/backup/
cp -v output/day01/projects/script.sh output/day01/projects/my_script.sh

echo "print the list of filines in projects folder"
cd output/day01/projects
ls -la

echo "===================================="
echo "===================END=============="
echo "===================================="

