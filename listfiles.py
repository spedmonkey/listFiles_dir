#best commit ever
#another good commit
from os import walk
import shutil 

f = []
for (dirpath, dirnames, filenames) in walk('/home/spedmonkey/Pictures/goPro/100GOPRO'):
    f.extend(filenames)
    break

for i in filenames[0::50]:
	shutil.copyfile(dirpath+'/'+i, '/home/spedmonkey/Pictures/'+str(i))


