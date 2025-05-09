#!/bin/bash

echo "###########################"
echo "#########DAY4##############"
echo "###########################"

ROOT="output"
mkdir -p "$ROOT"

echo "Enter your Name please: "
read name

echo "thx!"
echo "Enter your age please"
read age

echo "thx!"
echo "Enter your fav commmand in Linux"
read command

name="${name^}"
command=$(echo "$command" | tr 'A-Z' 'a-z')
echo "[$(date +'%Y-%m-%d %H:%M')] Name: $name, Age: $age, Favorite Command: $command" >> $ROOT/user_profiles.txt


echo "Logged in $ROOT/user_profiles.txt"
echo "###############END##########"
