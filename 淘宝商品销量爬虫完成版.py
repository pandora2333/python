import requests
import re
import json
import traceback
def open_url(keyword,page=1):
    #&s=0,表示从第一个商品开始显示，由于一页是44个商品，所以&s=44表示第2页
    #&sort—sale-desc 表示按照商品销量降序排列
    payload = {'q':keyword,'s':str((page-1)*44),'sort':'sale-desc'}
    url = 'https://s.taobao.com/search'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
    res = requests.get(url,params=payload,headers=headers)
    return res
#获取列表页的所有商品
def get_items(res):
    g_page_config = re.search(r'g_page_config = (.*?);\n',res.text)
    page_config_json = json.loads(g_page_config.group(1))
    page_items = page_config_json['mods']['itemlist']['data']['auctions']
    result = []#整理出我们关注的信息（id，标题，链接，售价，销量和商家）
    for each_item in page_items:
        dict1 = dict.fromkeys(('nid','title','detail_url','view_price','view_sales','nick'))
        dict1['nid'] = each_item['nid']
        dict1['title'] = each_item['title']
        dict1['detail_url'] = each_item['detail_url']
        dict1['view_price'] = each_item['view_price']
        dict1['view_sales'] = each_item['view_sales']
        dict1['nick'] = each_item['nick']
        result.append(dict1)
    return result
#统计该页面所有商品的销量
def count_sales(items,keyname):
    count =0
    for each in items:
        if keyname in each['title']:
            count+=int(re.search(r'\d+',each['view_sales']).group(0))
    return count
def main():
    keyword = input('请输入搜索的关键字：')
    num = int(input('请输入查询的页数：'),base=10)
    keyname = input('请输入定位关键字：')
    length = num
    total = 0
    for each in range(length):
        res = open_url(keyword,each+1)
        try:
            items = get_items(res)
            total += count_sales(items,keyname)
        except:
            break
    print('总销量；',total)
if __name__=='__main__':
    try:
        main()
        input()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        input()

