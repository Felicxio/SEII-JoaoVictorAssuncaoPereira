#!/bin/bash

case ${1,,} in
	joao3653 | administrator)
		echo "Hello, you're the boos here!"
		;;
	help)
		echo "Just enter your username!"
		;;
	*)
		echo "Hello there. u're not the boss of me. Enter a valid username!"
esac

