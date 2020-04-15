#!/bin/bash

 LOCPRO='../'
 NASPRO='cboehm@141.39.133.51:/home/cboehm/Projects/202004_website'

 git ls-files -z | rsync -e 'ssh -p 312' --exclude-from=- --from0 --exclude=.git -raz --progress $LOCPRO $NASPRO
