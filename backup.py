"""
zip-backup
===========
A simple zip backup script that creates a <date_time>.zip 
archive of specified directory.
"""
__author__ = 'Blayne Campbell'
__date__ = '2015-02-28'

from datetime import datetime
import zipfile
import time
import glob
import os

backup_target = 'C:\\path\\to\\backup\\*'
backup_destination = 'C:\\backups'

backup_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


if __name__ == '__main__':
    print("Starting backup of %s" % backup_target)
    if not os.path.exists(backup_destination):
        try:
            os.makedirs(backup_destination)
        except Exception as e:
            print(e)
    backup = zipfile.ZipFile('%s\%s.zip' % (backup_destination,
                                            backup_time), mode='w')
    try:
        for file in glob.glob(backup_target):
            print("Backing up: %s" % file)
            backup.write(file)
    except Exception as e:
        print(e)
    finally:
        backup.close()
        print("Backup completed!\nBackup File:%s\\%s.zip"
              % (backup_destination, backup_time))
