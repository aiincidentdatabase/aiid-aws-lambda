#!/bin/sh -l

echo "Hello $1"
ls -la
pwd
python newsplease.py
time=$(date)
echo "::set-output name=time::$time"
