# -- coding: utf-8 --
import Psyunew6
import sys
from ctypes import *


ret=c_int()
ver=c_int()

KeyPath=create_string_buffer(260)
ret=Psyunew6.FindPort(0,KeyPath)

if ret != 0:   
    print('未找到加密锁,请插入加密锁后，再进行操作。\n')
    sys.exit(1)


##      用于返回加密狗的ID号，加密狗的ID号由两个长整型组成。
ID_1=c_ulong(1)
ID_2=c_ulong()
ret=Psyunew6.GetID(byref(ID_1),byref(ID_2),KeyPath)
if ret==0 :
    print('锁ID是: %8x %8x\n' %(ID_1.value,ID_2.value))
else:
    print('返回ID错误\n')

#用于返回加密狗的版本号
ret=Psyunew6.NT_GetIDVersion(byref(ver),KeyPath)
if ret==0 :
    print('锁的版本号是:%d\n'%(ver.value))
else:
    print('返回版本号错误\n')


# 设置锁的读密码，注意设置锁的读密码，是输入原来的“写”密码，而不是原来的“读”密码
if Psyunew6.SetReadPassword(b'ffffffff',b'ffffffff',b'11111111',b'11111111',KeyPath)!=0:
    print( '设置读密码失败\n')
else:
    print( '设置读密码成功\n')

# 设置锁的写密码

if Psyunew6.SetWritePassword(b'ffffffff',b'ffffffff',b'ffffffff',b'ffffffff',KeyPath)!=0 :
    print( '设置写密码失败\n')
else:
    print( '设置写密码成功\n')


#注意，如果是普通单片机芯片，储存器的写次数是有限制的，写次数为1000次，读不限制，如果是智能芯片，写的次数为10万次
#写入字符串到加密锁中,使用默认的写密码ffffffff', b'ffffffff', 写入到加密锁的第0个地址    
InString='加密锁'.encode('utf-8')
ret = Psyunew6.YWriteString(InString, 0, b'ffffffff', b'ffffffff', KeyPath)
if ret != 0 :
    print('写字符串失败\n')  
else:
    print('写入成功。写入的字符串的长度是:%d\n'%(len(InString)))

#从加密锁中读取字符串,使用默认的读密码:ffffffff', b'ffffffff', 从加密锁的第0个地址开始读
mylen=c_short()
mylen = 9#注意这里的长度，长度要与写入的字符串的长度相同,
outstring=create_string_buffer((mylen+1))        
if Psyunew6.YReadString(outstring, 0, mylen, b'11111111', b'11111111', KeyPath) != 0:
    print('读字符串失败\n') 
else:
    print('读字符串成功:%s\n'%(outstring.value))


#设置增强算法密钥一
#注意:密钥为不超过32个的0-F字符，例如:1234567890ABCDEF1234567890ABCDEF,不足32个字符的，系统会自动在后面补0
Key=b'1234567890ABCDEF1234567890ABCDEF'
ret = Psyunew6.SetCal_2(Key, KeyPath)
if ret != 0:
    print('设置增强算法密钥错误\n')
else:
    print('已成功设置了增强算法密钥\n')

##使用增强算法一对字符串进行加密
InString = b'abc'
mylen = len(InString)+1
if mylen < 8 :
    mylen = 8 
outstring =create_string_buffer((mylen* 2+1))#//注意，这里要加1一个长度，用于储存结束学符串          
ret = Psyunew6.EncString(InString, outstring, KeyPath)
if ret != 0:
    print('加密字符串出现错误\n')  
else:
    print('已成功对字符串进行加密，加密后的字符串为:%s\n' % outstring.value)
    print(Psyunew6.StrEnc('abc', '1234567890ABCDEF1234567890ABCDEF'))

