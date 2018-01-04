#!/bin/bash -e

astyle "*.h" "*.c" -r --options=astylerc
find $1 -name "*.orig" -delete
