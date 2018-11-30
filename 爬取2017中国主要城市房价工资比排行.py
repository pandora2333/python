import re
import requests
import bs4
import openpyxl
def open_url(url):
    headers={'Accept':'text/html, application/xhtml+xml, image/jxr, */*','Accept-Encoding':'gzip, deflate','Cookie':'pgv_info=ssid=s6806615892; pgv_pvid=2293807192; pac_uid=0_5a991827022ed; ts_last=news.house.qq.com/a/20170702/003985.htm; ts_uid=4093458332; ad_play_index=13','Host':'news.house.qq.com','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
    res = requests.get(url)
    return res
def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    content = soup.find(id='cont')
    #print(content)
    targets = content.find_all('p',class_='text')
    targets = iter(targets)
    for each in targets:
        if each.text.isnumeric():
            data.append([re.search(r'\[(.*?)\]',next(targets).text).group(1),
                         re.search(r'\d.*',next(targets).text).group(),
                         re.search(r'\d.*',next(targets).text).group(),
                         re.search(r'\d.*',next(targets).text).group()])
    return data
def toexcel(data):
    wb = openpyxl.Workbook()
    wb.guess_types =True#让excel自动识别进入的数据是字符还是数字,(让字符数字转换成数字）

    ws = wb.active
    ws.append(['城市','平均房价','平均工资','房价工资比'])
    for each in data:
        ws.append(each)
    wb.save('e:/2017中国主要城市房价工资比排行榜.xlsx')
def main():
    url = 'https://xw.qq.com/c/housenews/20170702003985'
    res = open_url(url)
    data = find_data(res)
    toexcel(data)
if __name__ == '__main__':
    main()
    
                    
