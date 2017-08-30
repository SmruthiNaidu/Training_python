#Script to print ls command in Json format
import subprocess
import csv

process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
stderr, stdout = process.communicate()


reader = csv.DictReader(stdout.decode(),splitlines(),
                        delimiter='\t',
                        keynames=['permissions', 'links',
                                    'owner', 'group', 'size',
                                    'date', 'time', 'filename'])

for row in reader:
    print(row)