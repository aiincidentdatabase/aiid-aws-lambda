#!/bin/sh -l

echo "Hello $1"
python /parsenews.py
time=$(date)
echo "::set-output name=time::$time"
