#!/bin/bash

echo "Type your name: "
read name
echo "What is your age: "
read age
echo "Hello $name, you are $age years old."
sleep 2
rich=$((( $RANDOM % 14) + $age ))

echo "$name, you will get rich at age $rich"
echo "$PWD, $SHELL, $USER, $HOSTNAME"
