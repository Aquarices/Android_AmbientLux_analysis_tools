#!/usr/bin/python
#coding:utf-8
import os, sys

#Name:bugreportCut
#Description:去除多余的log信息，保留和调光相关的内容
def bugreportCut(bugreport):   
   inPutFile = open(bugreport, encoding='utf-8')
   outPutFile = open(bugreport +'_result.txt', 'w')
   print('Create'+ bugreport + '_result.txt success\n')
   print('Start to read lines...\n')
   lines = inPutFile.readlines()
   for line in lines:
      if "D AutomaticBrightnessController" in line:
	item = [line.count(" "), line.lstrip()]
	if lastTemp == []:lastTemp = item
		if item[0] > lastTemp[0]:
			
		
        outPutFile.write(line)
		 
   inPutFile.close()
   outPutFile.close()
         

#-----主程序入口-----
#获取当前目录路径
dirPath = os.path.dirname(os.path.abspath(__file__))
#按降序对文件排序,排除掉程序自己，从而处理其他bugreport文件
dirs = os.listdir(dirPath)
del dirs[0]
#开始处理bugreport
for file in dirs:
   #去除多余的log信息，保留和调光相关的内容
   bugreportCut(file) 


