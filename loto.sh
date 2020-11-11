#!/bin/bash

set -e 

if [ "$ENV" = 'loto7' ]; then
    exec python get_randoms.py 7 37
elif [ "$ENV" = 'loto6' ]; then
    exec python get_randoms.py 6 43
else
    echo "select loto7 or loto6."
fi
