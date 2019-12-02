# -- coding: utf-8 --
import platform
from ctypes import *


if 'Windows' in platform.system():
    Psyuunew=windll.LoadLibrary('Syunew6D.dll')
else:
    Psyuunew=cdll.LoadLibrary('libPsyunew6_64.so')
    # Psyuunew=cdll.LoadLibrary('libPsyunew6.so')     


##获到锁的版本
NT_GetIDVersion=Psyuunew.NT_GetIDVersion
NT_GetIDVersion.argtypes=(c_void_p,c_char_p)
NT_GetIDVersion.restypes=(c_int)


##获取锁的扩展版本
NT_GetVersionEx=Psyuunew.NT_GetVersionEx
NT_GetVersionEx.argtypes=(c_void_p,c_char_p)
NT_GetVersionEx.restypes=(c_int)


##算法函数
sWrite_2Ex_New=Psyuunew.sWrite_2Ex_New  
sWrite_2Ex_New.argtypes=(c_ulong ,c_void_p,c_char_p)
sWrite_2Ex_New.restypes=(c_int)

sWriteEx_New=Psyuunew.sWriteEx_New  
sWriteEx_New.argtypes=(c_ulong ,c_void_p,c_char_p)
sWriteEx_New.restypes=(c_int)

sWrite_2Ex=Psyuunew.sWrite_2Ex  
sWrite_2Ex.argtypes=(c_ulong ,c_void_p,c_char_p)
sWrite_2Ex.restypes=(c_int)

sWriteEx=Psyuunew.sWriteEx  
sWriteEx.argtypes=(c_ulong ,c_void_p,c_char_p)
sWriteEx.restypes=(c_int)

sRead=Psyuunew.sRead  
sRead.argtypes=(c_void_p,c_char_p)
sRead.restypes=(c_int)

sWrite_2=Psyuunew.sWrite  
sWrite_2.argtypes=(c_ulong ,c_char_p)
sWrite_2.restypes=(c_int)

sWrite_2=Psyuunew.sWrite_2  
Psyuunew.argtypes=(c_ulong ,c_char_p)
sWrite_2.restypes=(c_int)
##算法函数


##写一个字节到加密锁中
YWrite=Psyuunew.YWrite
YWrite.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YWrite.restypes=(c_int)

##从加密锁中读取一批字节
YRead=Psyuunew.YRead
YRead.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YRead.restypes=(c_int)

##查找指定的加密锁（使得普通算法一）
FindPort_2=Psyuunew.FindPort_2  
FindPort_2.argtypes=(c_int ,c_ulong ,c_ulong ,c_char_p)
FindPort_2.restypes=(c_int)

##查找指定的加密锁（使得普通算法二）
FindPort_3=Psyuunew.FindPort_3  
FindPort_3.argtypes=(c_int ,c_ulong ,c_ulong ,c_char_p)
FindPort_3.restypes=(c_int)

##查找加密锁
FindPort=Psyuunew.FindPort  
FindPort.argtypes=(c_int ,c_char_p)
FindPort.restypes=(c_int)

##获取锁的ID
GetID=Psyuunew.GetID  
GetID.argtypes=(c_void_p,c_void_p,c_char_p)
GetID.restypes=(c_int)

##从加密锁中读字符串
YReadString=Psyuunew.YReadString 
YReadString.argtypes=(c_char_p ,c_short,c_int ,c_char_p ,c_char_p,c_char_p)
YReadString.restypes=(c_int)

##写字符串到加密锁中
YWriteString=Psyuunew.YWriteString
YWriteString.argtypes=(c_char_p,c_short,c_char_p ,c_char_p,c_char_p )
YWriteString.restypes=(c_int)

##设置写密码
SetWritePassword=Psyuunew.SetWritePassword
SetWritePassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetWritePassword.restypes=(c_int)

##设置读密码
SetReadPassword=Psyuunew.SetReadPassword
SetReadPassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetReadPassword.restypes=(c_int)

##设置增强算法密钥一
SetCal_2=Psyuunew.SetCal_2
SetCal_2.argtypes=(c_char_p,c_char_p)
SetCal_2.restypes=(c_int)

##使用增强算法一对字符串进行加密
EncString=Psyuunew.EncString  
EncString.argtypes=(c_char_p,c_char_p,c_char_p)
EncString.restypes=(c_int)

##使用增强算法一对二进制数据进行加密
Cal=Psyuunew.Cal  
Cal.argtypes=(c_void_p,c_void_p,c_char_p)
Cal.restypes=(c_int)

##设置增强算法密钥二
SetCal_New=Psyuunew.SetCal_New
SetCal_New.argtypes=(c_char_p,c_char_p)
SetCal_New.restypes=(c_int)

##使用增强算法二对字符串进行加密
Cal_New=Psyuunew.Cal_New  
Cal_New.argtypes=(c_void_p,c_void_p,c_char_p)
Cal_New.restypes=(c_int)

##使用增强算法二对字符串进行加密
EncString_New=Psyuunew.EncString_New  
EncString_New.argtypes=(c_char_p,c_char_p,c_char_p)
EncString_New.restypes=(c_int)

##使用增强算法对字符串进行解密使用软件
##StrDec=Psyuunew.StrDec
##StrDec.argtypes=(c_char_p,c_char_p,c_char_p)
##StrDec.restypes=(c_void )
##
##StrEnc=Psyuunew.StrEnc  
##StrEnc.argtypes=(c_char_p,c_char_p,c_char_p)
##StrEnc.restypes=(c_void)
##
##EnCode=Psyuunew.EnCode    
##EnCode.argtypes=(c_void_p ,c_void_p ,  c_char_p )
##EnCode.restypes=(c_void)
##
##DeCode=Psyuunew.DeCode   
##DeCode.argtypes=(c_void_p , c_void_p , c_char_p  )
##DeCode.restypes=(c_void)
##使用增强算法对字符串进行解密使用软件)


##使用增强算法对二进制数据进行加密使用软件)
DecBySoft=Psyuunew.DecBySoft         
DecBySoft.argtypes=(c_void_p, c_void_p )

EncBySoft=Psyuunew.EncBySoft         
EncBySoft.argtypes=(c_void_p   ,  c_void_p   )
##使用增强算法对二进制数据进行加密使用软件)

##字符串及二进制数据的转换
##HexStringToc_byteArray=Psyuunew.HexStringToc_byteArray
##HexStringToc_byteArray.argtypes=(c_char_p ,c_void_p)
##HexStringToc_byteArray.restypes=(c_void)
##
##ByteArrayToHexString=Psyuunew.ByteArrayToHexString
##ByteArrayToHexString.argtypes=(c_void_p,c_char_p ,c_int )
##ByteArrayToHexString.restypes=(c_void)
##字符串及二进制数据的转换

 ##初始化锁函数,注意，初始化锁后，所有的数据为0，读写密码也为00000000-00000000，增强算法不会被初始化
ReSet=Psyuunew.ReSet
ReSet.argtypes=[c_char_p]
ReSet.restypes=(c_int)

##以下函数只限于带U盘的锁
##设置是否显示U盘部分盘符，真为显示，否为不显示
SetHidOnly=Psyuunew.SetHidOnly 
SetHidOnly.argtypes=( c_bool,c_char_p)
SetHidOnly.restypes=(c_int)

##设置U盘部分为只读状态，
SetUReadOnly=Psyuunew.SetUReadOnly 
SetUReadOnly.argtypes=[c_char_p]
SetUReadOnly.restypes=(c_int)
##以上函数只限于带U盘的锁

##以下函数只支持智能芯片的锁
##生成SM2密钥对
YT_GenKeyPair=Psyuunew.YT_GenKeyPair
YT_GenKeyPair.argtypes=(c_char_p ,c_char_p,c_char_p,c_char_p)
YT_GenKeyPair.restypes=(c_int)

##设置Pin码
YtSetPin=Psyuunew.YtSetPin
YtSetPin.argtypes=(c_char_p,c_char_p,c_char_p )
YtSetPin.restypes=(c_int)

##设置SM2密钥对及身份
Set_SM2_KeyPair=Psyuunew.Set_SM2_KeyPair
Set_SM2_KeyPair.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p )
Set_SM2_KeyPair.restypes=(c_int)

##返回加密锁的公钥
Get_SM2_PubKey=Psyuunew.Get_SM2_PubKey
Get_SM2_PubKey.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p)
Get_SM2_PubKey.restypes=(c_int)

##对二进制数据进行SM2加密
SM2_EncBuf=Psyuunew.SM2_EncBuf
SM2_EncBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p)
SM2_EncBuf.restypes=(c_int)

##对二进制数据进行SM2解密
SM2_DecBuf=Psyuunew.SM2_DecBuf
SM2_DecBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p ,c_char_p)
SM2_DecBuf.restypes=(c_int)

##对字符串进行SM2加密
SM2_EncString=Psyuunew. SM2_EncString
SM2_EncString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2_EncString.restypes=(c_int)

##对字符串进行SM2解密
SM2_DecString=Psyuunew.SM2_DecString
SM2_DecString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2_DecString.restypes=(c_int)

##返回锁的硬件芯片唯一ID
GetChipID=Psyuunew.GetChipID 
GetChipID.argtypes=(c_char_p,c_char_p)
GetChipID.restypes=(c_int)
##以上函数只支持智能芯片的锁


if 'Linux' in platform.system():
	CloseUsbHandle=Psyuunew.CloseUsbHandle
	CloseUsbHandle.argtype=c_char_p
	CloseUsbHandle.restypes=(c_void_p)


def HexStringToByteArrayEx(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_byte
    temp=''
    for n in range(0,mylen,2):
        temp=InString[n:2+n]
        temp='0x'+temp
        in_data=int(temp,16)
        array_data[n/2]=(in_data)
    return array_data

def StringToByteArray(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_int
    temp=''
    for n in range(0,mylen):
        temp=InString[n:1+n]
        in_data=ord(temp)
        array_data[n]=(in_data)
    array_data[n+1]=0
    return array_data

def ByteArrayToString(InBuf):
    OutString=create_string_buffer('\0'*(len(InBuf)+1))
    for n in range(0,len(InBuf)):
        OutString[n]=chr(InBuf[n])
    return OutString.value
    

def ByteArrayToHexString(in_data,inlen):
    OutString=''
    temp=''
    for n in range(0,inlen):
        temp='%02X' % in_data[n]
        OutString=OutString+temp
    return OutString

def EnCode(InData,Key):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=EncBySoft(InData,KeyBuf)    
    return OutData

def DeCode(InData,Key):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=DecBySoft(InData,KeyBuf)
    return OutData


def EncBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray

    temp_string=''
    cnDelta = 2654435769
    _sum = 0
    a = 0
    b = 0
    c = 0
    d = 0
 
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d 
    y = 0
    z = 0

    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = (inb[pos +n + 4])
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        _sum = (cnDelta + _sum) & 0xffffffff
        temp=(z << 4) & 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1= (z + _sum) & 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        y = (y+ temp)& 0xffffffff
        temp=(y << 4)& 0xffffffff
        temp=(temp + c)& 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        z=(z+temp)& 0xffffffff
        n = n - 1

    outb={}
    for n in range(0,4):
        outb [n]= (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def DecBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray
    temp_string=''
    cnDelta = 2654435769
    _sum = 0xC6EF3720
    a = 0
    b = 0
    c = 0
    d = 0
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d
    y = 0
    z = 0
    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = inb[pos +n + 4]
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        temp=(y << 4)
        temp= ( temp+ c) & 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        z=(z-temp) & 0xffffffff
        #z -= ((y << 4) + c) ^ (y + _sum) ^ ((y >> 5) + d)
        temp=(z << 4)& 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1=(z + _sum)& 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        y = (y -temp)& 0xffffffff
        _sum = (_sum -cnDelta)& 0xffffffff
        n = n - 1
    
    outb={}
    for n in range(0,4):
        outb[n] = (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def StrDec(InString,Key):
   OutBuf={}
   mylen=len(InString)/2
   KeyBuf=HexStringToByteArrayEx(Key)
   InBuf=HexStringToByteArrayEx(InString)
   for n in range(0,(mylen-8)+1,8):
        tempBuf=DecBySoft(InBuf,KeyBuf,n)
        for i in range(0,8):
             OutBuf[i+ n] = tempBuf[i]
   if mylen>8:
       for n in range(len(OutBuf),mylen):
            OutBuf[n]=(InBuf[n])
   return ByteArrayToString(OutBuf)


def StrEnc(InString,Key):
    OutBuf={}
    InBuf={}
    temp_Buf=bytes(InString, encoding="utf8")
    mylen=len(InString)+1
    for n in range(0,mylen-1):
        InBuf[n]=temp_Buf[n]
    InBuf[n+1]=(0)
    if mylen<8:
            for n in range(mylen,8):
                 InBuf[n]=(0)
            mylen=8
            
    KeyBuf=HexStringToByteArrayEx(Key)
    for n in range(0,(mylen-8)+1,8):
         tempBuf=EncBySoft(InBuf,KeyBuf,n)

         for i in range(0,8):
              OutBuf[i+ n] = tempBuf[i]
    if mylen>8:
       for n in range(len(OutBuf),mylen-1):
            OutBuf[n]=(InBuf[n])
       OutBuf[n+1]=0
    OutString=ByteArrayToHexString(OutBuf,mylen)
    return OutString


