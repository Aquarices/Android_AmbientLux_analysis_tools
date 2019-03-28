#!/usr/bin/python
#coding:utf-8
import os, sys

#Name:saveString
#Description:保存每一行的结果
def saveString(string):
   line = "%s\n"%(string)
   with

#Name:bugreportCut
#Description:去除多余的log信息，保留和调光相关的内容
def bugreportCut(bugreport):
   #定义相关数组
   output = []
   lineTemp = []
   lastTemp = []
   #按“行”打开
   with open(bugreport, encoding='utf-8') as inPutFile:
      mdFile = inPutFile.readlines()
   #保存上传结果
   resultFile = bugreport + "_output.csv"
   
    = open(bugreport, encoding='utf-8')
   outPutFile = open(bugreport +'_result.txt', 'w')
   print('Create'+ bugreport + '_result.txt success\n')
   print('Start to read lines...\n')
   lines = inPutFile.readlines()
   for line in lines:
      if "D AutomaticBrightnessController" in line:
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


