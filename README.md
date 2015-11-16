Infrared Webcam Spy System
===========
It is an infrared and Webcam spy system based on Raspberry Pi and STM8S105S4. Through thewifi network, the system detects the people who get in the infrared area and then takes a picture which be sent to the user via Wechat(A popular social APP).
这是一个基于树莓派 (Raspberry Pi,ARM11 开发板) 和单片机 STM8S105S4 的红外 监控拍摄系统。利用红外模块监控是否有人进入红外区域,当有人进入时,红外模块的 某个引脚电平发生改变,单片机检测电平的变化并作信号处理,最终发送到服务器—— 树莓派(ARM11 开发板)。当服务器接收到单片机发送的信号,就会启动摄像头拍照, 最后将照片发送到指定的邮箱,用户利用微信的邮件提醒功能就可以达到实时监控的 目的。
