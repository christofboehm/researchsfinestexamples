#!/bin/bash

 LOCPRO='../data/'
 NASPRO='cboehm@141.39.133.51:/home/cboehm/Projects/202004_website/data/'

 rsync -e 'ssh -p 312' -raz --progress $NASPRO $LOCPRO