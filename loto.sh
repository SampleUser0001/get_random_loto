#!/bin/bash

set -e 

if [ "$ENV" = 'loto7' ]; then
    if [ "$ARRANGE" = 'arrange01' ]; then
        exec python get_randoms_arrange01.py 7 37
    else 
        exec python get_randoms.py 7 37
    fi
elif [ "$ENV" = 'loto6' ]; then
    if [ "$ARRANGE" = 'arrange01' ]; then
        exec python get_randoms_arrange01.py 6 43
    else 
        exec python get_randoms.py 6 43
    fi
else 
    echo "select loto7 or loto6."
fi
