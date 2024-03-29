#!/bin/bash
clear
echo "[LOG] Updating repository ..."
git pull origin main
git status
git add .
git commit -am "$1"
git push origin main
git log -1 --pretty=oneline
echo