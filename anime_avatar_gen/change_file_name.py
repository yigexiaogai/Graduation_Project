from distutils import filelist
import os
 
path = 'G:/Py program/anime_avatar_gen/model/gan'

filelist = os.listdir(path=path)
# print(filelist)
delta = 625
n= 0
number = ['0', '1', '2', '3' ,'4' ,'5' ,'6' ,'7', '8' ,'9']
for file in filelist:
    if file[-3:] == 'png':
        # 获取文件旧名
        oldname = path + os.sep + filelist[n]
        # 转换文件名
        num = eval(file[:-4])
        # 设置新文件名
        newname = path + os.sep + str(num+delta) + '.png'
        os.rename(oldname, newname)
        print(oldname,'======>',newname)
    elif file[-3:] == 'pth':
        # 获取文件旧名
        oldname = path + os.sep + filelist[n]
        # 转换文件名
        num = ''
        for i in file:
            if i in number:
                num = num + i

        if num !='':
            num = eval(num)
            # 设置新文件名
            newname = path + os.sep + file[:5] + str(num+delta) + '.pth'
            
            os.rename(oldname, newname)
            print(oldname,'======>',newname)
    n += 1