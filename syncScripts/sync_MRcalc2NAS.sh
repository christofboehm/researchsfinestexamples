#!/bin/bash
LOCPRO='../'

NASPRO='/home/cboehm/NAS/Boehm/Projects/202004_website/'

rsync -raz --progress $LOCPRO $NASPRO
