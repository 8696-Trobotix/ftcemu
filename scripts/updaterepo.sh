#!/bin/bash

if [[ $1 == "" ]]; then
    echo "Please enter a repository that has been cloned in repos."
    exit
fi

read -p "Overwrite contents in $1? " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Canceled."
    exit
fi

echo "Updating..."
rm -rf repos/$1/TeamCode/src/main/java/org/firstinspires/ftc/teamcode
rm -rf repos/$1/TeamCode/src/main/assets
cp -r TeamCode/src/main/java/org/firstinspires/ftc/teamcode repos/$1/TeamCode/src/main/java/org/firstinspires/ftc
cp -r TeamCode/src/main/assets repos/$1/TeamCode/src/main
echo "Complete."
