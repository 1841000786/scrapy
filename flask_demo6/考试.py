import os
import shutil
filelist =[]
rootdir= "D:\\E\\wegame\\lol\\lol.exe"
filelist = os.listdir(rootdir)
for f in filelist:
  filepath = os.path.join( rootdir,f )
  if os.path.isfile(filepath):
    os.remove(filepath)
    print(filepath+" removed!")
  elif os.path.isdir(filepath):
    shutil.rmtree(filepath,True)
    print("dir "+filepath+" removed!")