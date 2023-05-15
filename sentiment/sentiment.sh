#!/bin/bash
 
python sentiment.test.py  -a api -p 8000 -v 1 -r 1 -l alice --password wonderland --sentence "life is beautiful"
python sentiment.test.py  -a api -p 8000 -v 2 -r 1 -l alice --password wonderland --sentence "life is beautiful"
python sentiment.test.py  -a api -p 8000 -v 2 -r 0 -l alice --password wonderland --sentence "life sucks"
python sentiment.test.py  -a api -p 8000 -v 1 -r 0 -l alice --password wonderland --sentence "life sucks"
