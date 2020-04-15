#!/bin/bash

 LOCPRO='../'
 NASPRO='/Volumes/TUMERO0GF-Karampinos/Boehm/Projects/202004_website/'

 git ls-files -z | rsync --exclude-from=- --from0 --exclude=.git -uatrviz --progress $LOCPRO $NASPRO
