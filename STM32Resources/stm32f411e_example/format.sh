#!/bin/bash -e

astyle "*.h" "*.c" -r --options=astylerc
find . -name "*.orig" -delete
