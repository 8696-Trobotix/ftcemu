#!/bin/bash

if [[ $1 == "" ]]; then
    echo "Please enter a repository that has been cloned in repos."
    exit
fi

read -p "Overwrite contents in TeamCode? " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Canceled."
    exit
fi

echo "Loading..."
rm -rf TeamCode/src/main/java/org/firstinspires/ftc/teamcode/*
rm -rf TeamCode/src/main/assets/*
cp -r repos/$1/TeamCode/src/main/java/org/firstinspires/ftc/teamcode TeamCode/src/main/java/org/firstinspires/ftc
cp -r repos/$1/TeamCode/src/main/assets TeamCode/src/main
echo "Complete."
