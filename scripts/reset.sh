#!/bin/bash

read -p "Delete contents in TeamCode? " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Canceled."
    exit
fi

echo "Deleting..."
rm -rf TeamCode/src/main/java/org/firstinspires/ftc/teamcode/*
rm -rf TeamCode/src/main/assets/*
echo "Complete."
