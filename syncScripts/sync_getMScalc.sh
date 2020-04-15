#!/bin/bash

 LOCPRO='../data/'
 NASPRO='cboehm@141.39.166.112:/home/cboehm/Projects/202004_website/data/'

 rsync -e 'ssh -p 312' -raz --progress $NASPRO $LOCPRO
