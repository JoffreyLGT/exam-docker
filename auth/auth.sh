#!/bin/bash
 
python auth.test.py  -a api -p 8000 -s 200 -v 1 -l alice --password wonderland --sentence "life sucks"
python auth.test.py  -a api -p 8000 -s 200 -v 2 -l alice --password wonderland --sentence "life sucks"
python auth.test.py  -a api -p 8000 -s 200 -v 1 -l bob --password builder --sentence "life sucks"
python auth.test.py  -a api -p 8000 -s 403 -v 2 -l bob --password builder --sentence "life sucks"
