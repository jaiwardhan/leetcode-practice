#!/bin/bash

c=$(cat "./codes.txt")
for i in $c
do
    problem_path=$(echo $i | cut -d '-' -f1)
    problem_code=$(echo $i | cut -d '-' -f2)
    echo "$f ==== $g"
done