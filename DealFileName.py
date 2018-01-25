#coding:utf-8
import os
path=input('please input filepath/ ')       
#获取该目录下所有文件，存入列表中
f=os.listdir(path)
n=0
for i in f:  
    #设置旧文件名（就是路径+文件名）
    oldname=path+f[n]   
    #设置新文件名
    if n < 9:
    	newname=path+'00'+str(n+1)+'.bmp'
    elif n < 99:
    	newname=path+'0'+str(n+1)+'.bmp'
    else:
    	newname=path+str(n+1)+'.bmp'    
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)    
    n+=1
