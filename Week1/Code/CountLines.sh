#!/bin/bash
var=${1:-../Data/spawannxs.txt} # set a default value if $1 unset in command line
NumLines=`wc -l < $var`
echo "The file $var has $NumLines lines"