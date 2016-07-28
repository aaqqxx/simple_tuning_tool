# !/usr/bin/env python
# -*- coding: utf-8 -*-

from ftplib import FTP
import sys
from PyQt4 import QtGui, QtCore
import os


def ftp_up(filename=r"C:\Users\XingHua\git\vxWorks\IL_prog"):
    ftp = FTP()
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息;0为关闭调试信息
    ftp.connect('192.168.14.100', 21)  # 连接
    ftp.login('aaqqxx', 'abc123')  # 登录，如果匿名登录则用空串代替即可
    # print ftp.getwelcome()#显示ftp服务器欢迎信息
    ftp.cwd('IL') #选择操作目录
    bufsize = 1024  # 设置缓冲块大小
    file_handler = open(filename, 'rb')  # 以读模式在本地打开文件
    ftp.storbinary('STOR %s' % os.path.basename(filename), file_handler, bufsize)  # 上传文件
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()
    print "ftp up OK"


def ftp_down(filename=r"C:\Users\XingHua\git\vxWorks\IL_prog"):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('192.168.14.100', 21)
    ftp.login('aaqqxx', 'abc123')
    # print ftp.getwelcome()#显示ftp服务器欢迎信息
    # ftp.cwd('xxx/xxx/') #选择操作目录
    bufsize = 1024
    # filename = "IL_prog"
    file_handler = open(filename, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR %s' % os.path.basename(filename), file_handler.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()
    print "ftp down OK"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    upload = QtGui.QPushButton("upload")
    # QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"),
    #                        app, QtCore.SLOT("ftp_down()"))
    QtCore.QObject.connect(upload, QtCore.SIGNAL("clicked()"),
                           ftp_up)
    upload.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    upload.setWindowTitle("Upload for VxWorks Server")
    upload.show()
    sys.exit(app.exec_())

