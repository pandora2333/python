
from urllib import request
from urllib.error import URLError
import re
import os
import time
import threading
'''
多线程实现版
'''

class spider(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        if not os.path.exists('bt集合'):
            os.mkdir('bt集合')
    '''
        定义一个种子下载的爬虫类
    '''
    def run(self):
        '''
            爬虫类的主要执行函数
        '''
        print('Starting'+self.name)
        #处理函数handle_fun()
        threadLock.acquire()
        self.handle_fun()
        print('Working:'+self.name,self.counter)
        threadLock.release()
    def load_page(self, url):
        '''
            加载页面，并返回页面内容html
        '''
        response = request.urlopen(url)
        return response.read().decode()

    def download_file(self, url):
        '''
            下载处理函数
        '''
        html = self.load_page(url)
        pattern = re.compile(r'<a href="(.*?)"target="_blank">')
        match = pattern.search(html)
        if match:
            dl_url = 'http://www.mxroom.com/' + match.group(1)
            html = self.load_page(dl_url)
            pattern_name = re.compile(r'<font color="#008000">(.*?)</font>')
            match_name = pattern_name.search(html)
            pattern = re.compile(r'<a href="(.*?)"><font size="4">')
            match = pattern.search(html)
            print('正在下载' + match_name.group(1) + '...')
            keep_request = True
            while keep_request:
                try:
                    dl_file = request.urlopen(match.group(1))
                except URLError as err:
                    print('error: ', err)
                    print('正在重新下载...')
                    time.sleep(1)
                else:
                    with open('bt集合/' + match_name.group(1), 'wb') as fp:
                        fp.write(dl_file.read())
                    keep_request = False
                    print('已下载')
        else:
            print('None')

    def handle_fun(self):
        '''
            处理函数
        '''
        area = 52 #暂时保留扩展性 417
        for i in range(2,4):
            print('正在下载第' + str(i) + '页种子...')
            content = self.load_page('http://www.mxroom.com/forum-'+str(area)+'-' + str(i) + '.html')
            with open('bt集合/' +str(i)+'.html', 'wb') as fp:
                fp.write(str(content))
            


#main函数
if __name__ == '__main__':
    startTime = time.time()
    threads = []
    threadLock = threading.Lock()
    for i in range(10):
        myspider = spider(str(i),'spider-'+str(i),str(i))
        myspider.start()
        threads.append(myspider)
    for t in threads:
        t.join()
    endTime = time.time()
    print('all over!','用时:',str(startTime-endTime),'s')
    input()
    '''
    pattern = re.compile(r'<a href="(.*?).html" onclick="atarget')
            match = pattern.findall(content)
            for url in match:
                self.download_file(url + '.html')
    '''
