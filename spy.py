#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import RPi.GPIO as IO
import os
import time

#
# 初始化图片名字和邮件相关
#
iname=1
picture=str(iname)+".jpeg"     # 发送图片的名字
email="n81ming@qq.com"         # 发送到这个email地址
title="spy system"                # 发送邮件的标题
content="Warning! Warning!"  # 发送邮件的内容
os.environ['email']=str(email)
os.environ['picture']=str(picture)
os.environ['title']=str(title)
os.environ['content']=str(content)

#
# 初始化LED:GPIO8和按键:GPIO25
#
LED=8
switch=7
IO.setmode(IO.BCM)
IO.setwarnings(False)
#IO.setup(switch,IO.IN,IO.PUD_UP)
IO.setup(switch,IO.IN)
IO.setup(LED,IO.OUT)

#
# 主循环
#
print("\n")
print("**********************基于Raspberry Pi的红外监控拍摄系统********************")
print("1. 功能介绍")
print("   当按下按键1时，灯灭，进入拍照状态，然后将图片发送到指定的邮箱，最后灯灭。")
print("2. 注意事项")
print("3. 版本号")
print("1.0")
print("****************************************************************************")
print("\n")
print("请按下按键1：")
while 1:
  if IO.input(switch) == 0:   # 按键按下
      IO.output(LED,IO.HIGH)  # 灯灭，进入拍照模式
      os.system("streamer -f jpeg -o "+picture) # 拍照
      #os.system("echo 'Warning: There are people walking into the monitoring area.'")
      print("\n")
      print("正在发送...")
      os.system('echo "$content" | sudo mutt -s "$title" -a $picture -- $email') # 发送到邮箱
      print("发送成功！")
      print("****************************************************************************")
      print("请再次按下按键1：")
      #time.sleep(1)           # 延时1秒
  else:
      IO.output(LED,IO.LOW)   # 灯亮，等待接收按键或者表示发送完成
                
IO.cleanup()



