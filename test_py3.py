# -- coding: utf-8 --
import Psyunew6
import sys
from ctypes import *

SIGN_LEN= (64*2+1)
SM2_ADDBYTE= 97
MAX_ENCLEN=  128
MAX_DECLEN=  (MAX_ENCLEN + SM2_ADDBYTE)
SM2_USENAME_LEN= 80
	
KeyPath=create_string_buffer(260)

ret=c_int()
ver=c_int()
verEx=c_int()

ret=Psyunew6.FindPort(0,KeyPath)
if(ret==0):

##	  /*查找是否存在指定的加密狗,如果找到，则返回0,KeyPath为锁所在的返回设备所在的路径。
##        '1、首先使用我们的开发工具来设置自定义的算法密钥
##        '2、在让加密锁进行加密运算那里随意输入一个数
##        '3、然后读出对应的检验码(即加密后的数据)，
##        '4、然后将输入的数和返回的数替换这里的参数“1”及参数“134226688”
##        '5、提示，设置不同的自定义密钥，对于同一输入数据，返回的检验码不相同*/
	#
			
        if Psyunew6.FindPort_2(0, 1, 134226688, KeyPath) != 0:
            print('未找到指定的加密锁\n')
        else:
            print('找到指定的加密锁\n')

##        //使用普通算法二来查找指定的加密锁
##        /*查找是否存在指定的加密狗,如果找到，则返回0,KeyPath为锁所在的返回设备所在的路径。
##        注意！！！！！！！！！这里的参数“1”及参数“134226688”，随每个软件开发商的不同而不同，因为每个开发商的加密锁的加密算法都不一样，
##        1、运行我们的开发工具，
##        2、在“算法设置及测试页”-》“加密”-》“请输入要加密的数据”那里随意输入一个数
##        3、然后单击“加密数据(使用普通算法二)”
##        4、然后就会返回对应的数据(即“加密后的数据”)，
##        然后将输入的数和返回的数替换这里的参数“1”及参数“134226688”*/
        if Psyunew6.FindPort_3(0, 1, 134226688, KeyPath) != 0:
            print('未找到指定的加密锁\n')
        else:
            print('找到指定的加密锁\n')


##      用于返回加密狗的ID号，加密狗的ID号由两个长整型组成。
        ID_1=c_ulong(1)
        ID_2=c_ulong()
        ret=Psyunew6.GetID(byref(ID_1),byref(ID_2),KeyPath)
        if ret==0 :
            print('锁ID是:%08x--%08x\n' %(ID_1.value,ID_2.value))
        else:
            print('返回ID错误\n')

#用于返回加密狗的版本号
        ret=Psyunew6.NT_GetIDVersion(byref(ver),KeyPath)
        if ret==0 :
            print('锁的版本号是:%d\n'%(ver.value))
        else:
            print('返回版本号错误\n')

##        //对输入的数进行加密运算，然后读出加密运算后的结果(使用普通算法一)	
        m_in1=c_ulong(1)
        m_out1=c_ulong()
        if Psyunew6.sWriteEx(m_in1,byref(m_out1), KeyPath)!= 0 :
            print( '(使用普通算法一)加密错误\n')
        else:
            print( '(使用普通算法一)加密成功,对数据1加密后的结果是:%d\n'%m_out1.value)

##        //对输入的数进行解密运算，然后读出解密运算后的结果(使用普通算法一)	
        m_in2=c_ulong(1)
        m_out2=c_ulong()
        if Psyunew6.sWrite_2Ex(m_in2,byref(m_out2), KeyPath)!= 0 :
            print( '(使用普通算法一)解密错误\n')
        else:
            print( '(使用普通算法一)解密成功，对数据1解密后的结果是:%d\n'%m_out2.value)

##        //对输入的数进行加密运算，然后读出加密运算后的结果，(使用普通算法二)
        if Psyunew6.NT_GetIDVersion(byref(ver),KeyPath) != 0 :
            print( '返回加密锁扩展版本号错误\n')
            exit()
        if ver.value<10 :
            print( '锁的扩展版本少于10,不支持普通算法二')
        else:
                if Psyunew6.sWriteEx_New(m_in1,byref(m_out1), KeyPath)!= 0 :
                    print( '(使用普通算法二)加密错误\n')
                else:
                    print( '(使用普通算法二)加密成功,对数据1加密后的结果是:%d\n'%m_out1.value)

##        //对输入的数进行解密运算，然后读出解密运算后的结果(使用普通算法二)
        if Psyunew6.NT_GetIDVersion(byref(ver),KeyPath) != 0 :
            print( '返回加密锁扩展版本号错误\n')
            exit()
        if ver.value<10 :
            print( '锁的扩展版本少于10,不支持普通算法二')
        else:
                if Psyunew6.sWrite_2Ex_New(m_in2,byref(m_out2), KeyPath)!= 0 :
                    print( '(使用普通算法二)解密错误\n')
                else:
                    print( '(使用普通算法二)解密成功，对数据1解密后的结果是:%d\n'%m_out2.value)


#注意，如果是普通单片机芯片，储存器的写次数是有限制的，写次数为1000次，读不限制，如果是智能芯片，写的次数为10万次
#写入字符串到加密锁中,使用默认的写密码ffffffff', 'ffffffff'.encode('utf-8'), 写入到加密锁的第0个地址	
        InString='加密锁'.encode('utf-8')
        ret = Psyunew6.YWriteString(InString, 0, 'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath)
        if ret != 0 :
            print('写字符串失败\n')  
        else:
            print('写入成功。写入的字符串的长度是:%d\n'%(len(InString)))

#从加密锁中读取字符串,使用默认的读密码:ffffffff', 'ffffffff'.encode('utf-8'), 从加密锁的第0个地址开始读
        mylen=c_short()
        mylen = 9#注意这里的长度，长度要与写入的字符串的长度相同,
        outstring=create_string_buffer((mylen+1))		
        if Psyunew6.YReadString(outstring, 0, mylen, 'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath) != 0:
            print('读字符串失败\n') 
        else:
            print('读字符串成功:%s\n'%(outstring.value))


#注意，如果是普通单片机芯片，储存器的写次数是有限制的，写次数为1000次，读不限制，如果是智能芯片，写的次数为10万次
#写入字符串带长度，这个代码与上面的不同的是:写入字符串的同时将字符串的长度也一并写入，
#使用默认的写密码ffffffff', 'ffffffff'.encode('utf-8'), 写入到加密锁的第200个地址
        InArray=c_ubyte*1
        InString = '加密锁'.encode('utf-8')
        blen = InArray(len(InString))
        
        #写入字符串到地址200+1			
        ret = Psyunew6.YWriteString(InString, 200+1, 'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath)
        if ret != 0 :
            print('写入字符串错误\n' )
        #写入字符串的长度到地址200,写入的长度为1
        ret = Psyunew6.YWrite(byref(blen), 200, 1, 'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath)
        if ret != 0 :
            print('写入字符串长度错误。\n')
        else:
            print('写入字符串成功\n')
	
#读取字符串带长度，这个代码与上面不同的是:先将事先写入到锁中的字符串长度取出，再读取指定长度的字符串
        
#先从地址200读到以前写入的字符串的长度		
        ret = Psyunew6.YRead(blen, 200, 1, 'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath)
        if ret != 0 :
            print('读取字符串长度错误。\n')
        outstring=create_string_buffer(blen[0])		
#再从地址201读取指定长度的字符串
        ret = Psyunew6.YReadString(outstring, 200+1, blen[0], 'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath)
        if ret != 0 :
            print('读取字符串错误\n' )
        else:
            print('已成功读取字符串：%s\n'%(outstring.value))

#写二进制数据到锁中，使用默认的写密码:'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), 写入到加密锁中的第300个地址		
        InArray_2=c_ubyte*50
        InBuf=InArray_2()
        mylen=20#要写入的数据长度为20		
        for n in range(0,20):
            InBuf[n]=(n)
        
        #要写入的地址为300
        ret = Psyunew6.YWrite(byref(InBuf), 300, mylen,'ffffffff'.encode('utf-8'), 'ffffffff'.encode('utf-8'), KeyPath)
        if ret != 0 :
            print('写入二进制数据错误\n')  
        else:
            print('已成功读取二进制数据\n')

# 设置锁的读密码，注意设置锁的读密码，是输入原来的“写”密码，而不是原来的“读”密码
        if Psyunew6.SetReadPassword('ffffffff'.encode('utf-8'),'ffffffff'.encode('utf-8'),'ffffffff'.encode('utf-8'),'ffffffff'.encode('utf-8'),KeyPath)!=0:
            print( '设置读密码失败\n')
        else:
            print( '设置读密码成功\n')
	
	# 设置锁的写密码
	
        if Psyunew6.SetWritePassword('ffffffff'.encode('utf-8'),'ffffffff'.encode('utf-8'),'ffffffff'.encode('utf-8'),'ffffffff'.encode('utf-8'),KeyPath)!=0 :
            print( '设置写密码失败\n')
        else:
            print( '设置写密码成功\n')


#设置增强算法密钥一
#注意:密钥为不超过32个的0-F字符，例如:1234567890ABCDEF1234567890ABCDEF,不足32个字符的，系统会自动在后面补0
        Key='1234567890ABCDEF1234567890ABCDEF'.encode('utf-8')
        ret = Psyunew6.SetCal_2(Key, KeyPath)
        if ret != 0:
            print('设置增强算法密钥错误\n')
        else:
            print('已成功设置了增强算法密钥\n')

##使用增强算法一对字符串进行加密
        InString = '加密锁'.encode('utf-8')
        mylen = len(InString)+1
        if mylen < 8 :
            mylen = 8 
        outstring =create_string_buffer((mylen* 2+1))#//注意，这里要加1一个长度，用于储存结束学符串			
        ret = Psyunew6.EncString(InString, outstring, KeyPath)
        if ret != 0:
            print('加密字符串出现错误\n')  
        else:
            print('已成功对字符串进行加密，加密后的字符串为:%s\n' % outstring.value)
                        
##        //推荐加密方案:生成随机数，让锁做加密运算，同时在程序中端使用代码做同样的加密运算，然后进行比较判断。
##        //增强算法是一个标准的TEA算法，在该例子中有对应的解密函数StrDec,对应的加密函数我为StrEnc


#使用增强算法一对二进制数据进行加密		
		 
        InBufArray=c_ubyte*8
        OutBufArray=c_ubyte*8
        InBuf=InBufArray()
        OutBuf=OutBufArray()
        for n in range(0,8):
            InBuf[n]=(n)
        
        ret = Psyunew6.Cal(InBuf, OutBuf, KeyPath)
        if ret != 0:
            print('加密二进制数据失败\n')  
        else:
            print('已成功对二进数据进行加密，加密后结果是:%02X%02X%02X%02X%02X%02X%02X%02X\n'%(OutBuf[0],OutBuf[1],OutBuf[2],OutBuf[3],OutBuf[4],OutBuf[5],OutBuf[6],OutBuf[7]))
        
        #增强算法是一个标准的TEA算法，在该例子中有对应的源码
        #加密代码为EncBySoft及解密函数DecBySoft

#设置增强算法密钥二
#注意:密钥为不超过32个的0-F字符，例如:1234567890ABCDEF1234567890ABCDEF,不足32个字符的，系统会自动在后面补0
        if Psyunew6.NT_GetVersionEx(byref(verEx),KeyPath) != 0 :
            print( '返回加密锁扩展版本号错误\n')
            exit()
        if ver.value<32 :
            print( '锁的扩展版本少于32,不支持增强算法二')
        else:
            Key='ABCDEF1234567890ABCDEF1234567890'.encode('utf-8')
            ret = Psyunew6.SetCal_New(Key, KeyPath)
            if ret != 0:
                print('设置增强算法密钥错误\n')
            else:
                print('已成功设置了增强算法密钥\n')
		
	
	##使用增强算法二对字符串进行加密
        if Psyunew6.NT_GetVersionEx(byref(verEx),KeyPath) != 0 :
            print( '返回加密锁扩展版本号错误\n')
            exit()
        if ver.value<32 :
            print( '锁的扩展版本少于32,不支持增强算法二')
        else:
            InString = '加密锁'.encode('utf-8')
            mylen = len(InString)+1
            if  mylen < 8 :
                mylen = 8 
                outstring = create_string_buffer((mylen* 2+1))#//注意，这里要加1一个长度，用于储存结束学符串		
                ret = Psyunew6.EncString_New(InString, outstring, KeyPath)
                if ret != 0:
                    print('加密字符串出现错误\n')  
                else:
                    print('已成功对字符串进行加密，加密后的字符串为:%s\n' % outstring.value)

#使用增强算法二对二进制数据进行加密		 
        if Psyunew6.NT_GetVersionEx(byref(verEx),KeyPath) != 0:
            print( '返回加密锁扩展版本号错误\n')
            exit()
        if verEx.value<32:
            print( '锁的扩展版本少于32,不支持增强算法二')
        else:
            InBufArray_2=c_ubyte*8
            OutBufArray_2=c_ubyte*8
            InBuf=InBufArray_2()
            OutBuf=OutBufArray_2()
        for n in range(0,8):
            InBuf[n]=(n)
                
        ret = Psyunew6.Cal_New(InBuf, OutBuf, KeyPath)
        if ret != 0:
            print('加密二进制数据失败\n')  
        else:
            print('已成功对二进数据进行加密，加密后结果是:%02X%02X%02X%02X%02X%02X%02X%02X\n'%(OutBuf[0],OutBuf[1],OutBuf[2],OutBuf[3],OutBuf[4],OutBuf[5],OutBuf[6],OutBuf[7]))
			
        #增强算法是一个标准的TEA算法，在该例子中有对应的源码
        #加密代码为EncBySoft及解密函数DecBySoft			


        if ver.value < 33 :
            print('锁的版本少于33,不支持SM2算法')
            exit()
		 
#以下代码只支持智能芯片F2K
#返回芯片唯一ID
        chipid=create_string_buffer(33)
        ret = Psyunew6.GetChipID(chipid,KeyPath)
        if ret != 0:
            print('返回芯片唯一ID时出现错误')
            exit()
        print('已成功返回芯片唯一ID:%s'%(chipid.value))

        PriKey=create_string_buffer(SIGN_LEN)
        PubKeyX=create_string_buffer(SIGN_LEN)
        PubKeyY=create_string_buffer(SIGN_LEN)
        Sm2UserName=create_string_buffer(SM2_USENAME_LEN)
        OutString=create_string_buffer(SIGN_LEN)


#生成密钥对
        ret = Psyunew6.YT_GenKeyPair(PriKey, PubKeyX, PubKeyY, KeyPath)
        if ret!=0:
            print('生成密钥对时错误。')

        print('生成密钥对成功。PriKey：%s,PubKeyX:%s,PubKeyY:%s'%(PriKey.value, PubKeyX.value, PubKeyY.value))
#设置密钥对到锁中
        ret = Psyunew6.Set_SM2_KeyPair(PriKey, PubKeyX, PubKeyY, 'mysofkey', KeyPath)
        if ret!=0:
            print('设置密钥时错误。错误码')

        print('设置密钥成功。')
#设置Pin码
	
        ret = Psyunew6.YtSetPin('123'.encode('utf-8'),'123'.encode('utf-8'),KeyPath)
        if  ret!= 0:
            print('设置Pin码时出现错误')
            exit()
        print('已成功设置了设置Pin码.' )

#使用默认的PIN码
        Pin='123'.encode('utf-8')
	
	#对数据进行加密
        Instring='加密锁'.encode('utf-8')
        inlen = len(Instring) + 1

        ##分配空间
        outlen = (inlen / MAX_ENCLEN + 1) * SM2_ADDBYTE + inlen
        OutString = create_string_buffer((outlen * 2 + 1))

        ret = Psyunew6.SM2_EncString(Instring,OutString,KeyPath)
        if ret != 0:
                print('对数据进行加密时出现错误')  
                exit() 
        print('已成功对数据进行加密:%s', OutString.value)

#对数据进行解密,使用默认的PIN码
        inlen = len(OutString) / 2
        outlen = (inlen - (inlen / MAX_DECLEN + 1) * SM2_ADDBYTE + 1)
        OutString_Dec = create_string_buffer(outlen)
        ret = Psyunew6.SM2_DecString(OutString,OutString_Dec,Pin,KeyPath)
        if ret != 0 :
                print('对数据进行解时出现错误')
                exit()
        print('已成功对数据进行解密:%s'%(OutString_Dec.value))

        ret = Psyunew6.Get_SM2_PubKey(PubKeyX, PubKeyY, Sm2UserName, KeyPath)
        if ret!=0:
            print('从锁中获取公钥时错误。')
            exit
        print('从锁中获取公钥:PubKeyX:%s,PubKeyY:%s,Sm2UserName:%s'%(PubKeyX.value, PubKeyY.value, Sm2UserName.value))

#以下代码只支持iKey系列
        if Psyunew6.NT_GetVersionEx(byref(verEx),KeyPath) != 0:
            print( '返回加密锁扩展版本号错误\n')
            exit()
        if verEx.value < 38:
            print('锁的扩展版本少于38,不支持带U盘功能')
            exit()
        if Psyunew6.SetUReadOnly(KeyPath) != 0:
            print('设置iKey为只读模式时错误')
            exit()
        if Psyunew6.SetHidOnly(true, KeyPath) != 0:
            print('设置iKey不显示盘符时错误')
            exit()
        print('设置成功，需要重新插入iKey才生效。')

        if 'Linux' in platform.system():
            Psyunew6.CloseUsbHandle(KeyPath)#关闭USB设备
        
else:   
	print('未找到加密锁,请插入加密锁后，再进行操作。\n')





               
        
		
