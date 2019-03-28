#!/usr/bin/python
#coding:utf-8
import os, sys
         
#-----主程序入口-----
#获取当前目录路径
dirPath = os.path.dirname(os.path.abspath(__file__))
#按降序对文件排序,排除掉程序自己，从而处理其他bugreport文件
dirs = os.listdir(dirPath)
del dirs[0]
#创建路径保存分析结果
outPutFile = open('result.txt','w')
#添加文件   
for file in dirs:
   #去除多余的log信息，初步保留和调光相关的内容
   inPutFile = open(file, encoding='utf-8')
   lines = inPutFile.readlines()
   #开始按行处理
   for line in lines:
      #如果含有自动调光关键信息，执行以下代码
      if "D AutomaticBrightnessController" in line:
         lineList = line.split()
         del lineList[0]
         for i in range(1,6):
            del lineList[1]
         line = '  '.join(lineList)
         print(line)
         outPutFile.write(line)
         outPutFile.write('\n')
inPutFile.close()
outPutFile.close()
