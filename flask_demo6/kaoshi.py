import os
def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            print('文件: %s' % tmp_path)
        else:
            print('文件夹：%s' % tmp_path)
            traverse(tmp_path)
path = 'D:\E'
traverse(path);


path1='D:\E\wegame\lol\lol.exe'
os.remove(path1)
print('删除成功')
