#!/usr/bin/python
#coding:utf-8
import os, sys

#Name:bugreportCut
#Description:去除多余的log信息，保留和调光相关的内容
def bugreportCut(bugreport):
   #添加文件   
   with open(bugreport, encoding='utf-8') as inPutFile:
      lines = inPutFile.readlines()
   #开始按行处理
   for line in lines:
	  #如果含有自动调光关键信息，执行以下代码
      if "D AutomaticBrightnessController" in line:
         lineList = line.split(" ")
	 print(lineList)
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
inPutFile.close()
outPutFile.close()


