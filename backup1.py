"""
backup import file. How to do that?
1. which files need to be backuped, and where are they?
2. where to store the backup, and in what's kind of format?
3. how to do that?

"""

import os
import time

source = ['/']

target_dir = []

target = target_dir + time.strftime('%Y%m%d%H%M%S')+ '.zip'

zip_command = "zip -qr  '%s'  %s"%(target, ''.join(source))


if os.system(zip_command) == 0:
    print "successful backup to", target

else:
    print "Backup Failed"
