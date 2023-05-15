#!/bin/bash

python perm.test.py  -a api -p 8000 -s 200 -l alice --password wonderland
python perm.test.py  -a api -p 8000 -s 200 -l bob --password builder
python perm.test.py  -a api -p 8000 -s 403 -l clementine --password mandarine
