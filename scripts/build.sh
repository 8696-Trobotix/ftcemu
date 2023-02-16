#!/bin/bash

read -p $'Build Task\n1: Gradle\n2: Make\n> ' -n 1 -r
echo
if [[ $REPLY =~ 1 ]]; then
    ./gradlew build
elif [[ $REPLY =~ 2 ]]; then
    cd tui/build
    make
fi
