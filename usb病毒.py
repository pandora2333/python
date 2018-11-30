'''
适用于Windows
by pandora
由于多线程版本存在种种问题，所以暂不加入多线程
2018/5/31
'''
import os,shutil
from time import sleep
import re
usb_path = 'f://'
#print(os.path.isdir("f://"))#判断usb文件夹位置
print('开始运行中...')
temp = input('输入你的将要新建存储文件夹名称:')
#print(os.path.isdir(temp))
if not os.path.isdir(temp):
    try:
        os.makedirs(temp)
        print('新文件夹创建完毕!')
    except:
        print('路径出错,请重试!')
else:
    print('已经存在该文件夹，将继续使用老的文件夹')
#选择性复制文件
target_folder = temp
#指定文件类型
typefile = input('请输入想要复制文件类型,如：txt,默认复制zip,rar,docx,ppt,xls,txt这些类型文件,直接回车则使用默认值:')
regex_filename =""
if typefile == "":
    regex_filename = re.compile('(.*zip$)|(.*rar$)|(.*docx$)|(.*ppt$)|(.*xls$)|(.*txt$)')
else:
    regex_filename = re.compile('(.*'+typefile+'$)')
filesize = input("请设置一个文件复制的最大容量:(ps:不支持运算表达式，单位:字节,默认5m,直接回车则使用默认值):")
if filesize=="":
    filesize = 5*1024*1024
else:
    try:
        filesize = int(filesize)
    except:
        print('数据不规范,请重试!')

print("开始扫描u盘是否插入...")
while True:
    if os.path.isdir("f://"):
        new_content = os.listdir(usb_path)#每隔一定时间扫描一次f://
        content = os.listdir(temp)#用于返回路径下所有文件及其文件夹的名称
    #if new_content != content:#如果发现该更目录下存在内容，说明u盘已插入
        break;
    sleep(3)
#找到U盘文件夹,返回包括新文件夹string类型名称的列表
#print(x)
print('u盘已插入，开始复制中...')
x = [item for item in new_content if item not in content]
'''#shutil.copytree，把目录下的所有东西全复制到e:/temmpusb/文件夹下
    shutil.copytree(os.path.join(usb_path,x[0]),'e:/tempusb/')'''
for i in range(len(x)):
    if os.path.isdir(os.path.join(usb_path,x[i])):#x[i]
        for root,dirs,files in os.walk(os.path.join(usb_path,x[i])):
            for name in files:
                file = os.path.join(root,name)
                if os.path.getsize(file) < filesize and regex_filename.match(file):
                    print('以复制文件:',name)
                    shutil.copy2(file,target_folder)
    else:
        if os.path.getsize(os.path.join(usb_path,x[i])) <  filesize and regex_filename.match(os.path.join(usb_path,x[i])):
            print('以复制文件:',os.path.join(usb_path,x[i]))                                                                               
            shutil.copy2(os.path.join(usb_path,x),target_folder)
    
print('程序运行完毕!')
#input()#用于暂停命令行窗口
