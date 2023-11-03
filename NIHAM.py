import os, sys
try:os.system('git pull')
except:pass
try:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
except:pass
import NIHAM64
