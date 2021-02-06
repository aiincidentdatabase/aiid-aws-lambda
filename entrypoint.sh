#!/bin/sh -l

echo "Hello $1"
python newsplease.py
time=$(date)
echo "::set-output name=time::$time"
