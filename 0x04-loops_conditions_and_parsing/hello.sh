#!/usr/bin/env bash

car=$1
case $car in
	"BMW" )
		echo "This is my car in 2033" ;;
	"Mercedese" )
		echo "This is my car in 2027" ;;
	"Honda" )
		echo "This is my car in 2025" ;;
	"Toyota" )
		echo "This is my car in 2025" ;;
	* )
		echo "I don't drive this car" ;;
esac
