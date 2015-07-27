#!/bin/bash
src=$1

sed 's/<[^>]*>//g' $src > $src.out
sed '/^\s*$/d' -i $src.out
