#!/bin/bash
echo "==============DAY 2==============="

ROOT=output

echo "creating files"
cd "$ROOT"
mkdir -p day02-lab
cd day02-lab
touch script.sh notes.txt public.log


echo "applying permisstions"
chmod 700 script.sh
chmod 600 notes.txt
chmod 444 public.log

echo "output"
ls -l

echo "============END==========="
echo "Date: $(date)"


