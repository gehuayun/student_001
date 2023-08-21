print('Hello World !!!')
import os
import time

source = ['"D:\\python-test1/t2"']
target_dir = 'D:\\t1'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

command = input('Enter a commmand --> ')

if len(command)==0:
    target = today + os.sep + now +'.zip'
else:
    target = today + os.sep +now + '_' + command.replace('','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')