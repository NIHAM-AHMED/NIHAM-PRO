#coding=utf-8
import os, sys, platform
#os.system('xdg-open https://chat.whatsapp.com/J7W0XhWjOCM5e78jQc10aX')
#os.system('xdg-open https://facebook.com/groups/1999316193754030/')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf NIHAM64.cpython-311.so')
except:
    pass
os.system('rm -rf NIHAM64.cpython-311.so')
os.system('git pull')
try:os.mkdir('/sdcard/NIHAM')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('NIHAM64.cpython-311.so'):
        os.system('curl -L https://raw.githubusercontent.com/NIHAM-71/NIHAM-PRO/main/NIHAM64.cpython-311.so?raw=true -o NIHAM64.cpython-311.so') 
        import NIHAM64
    else:
        import NIHAM64
