import re
import json
import requests
def open_url(keyword):
    payload = {'q':keyword,'sort':'sale-desc'}
    url = 'https://s.taobao.com/search'
    res = requests.get(url,params=payload)
    return res
    
def get_space_end(level):
    return '  '*level+'-'
def get_space_expand(level):
    return '  '*level+'+'
def find_keys(targets,level):
    keys = iter(targets)
    for each in keys:
        if type(targets[each]) is not dict:
            print(get_space_end(level)+each)
        else:
            print(get_space_expand(level)+each)
            find_keys(targets[each],level+1)
def main():
    keyword = input('请输入搜索关键字')
    res = open_url(keyword)
    with open('e:/items.txt','w',encoding='utf-8') as file:
        file.write(res.text)
    with open('e:/items.txt','r',encoding='utf-8') as f:
        g_page_config = re.search(r'g_page_config = (.*?);\n',f.read())
        page_config_json =json.loads(g_page_config.group(1))
        find_keys(page_config_json,1)
if __name__=='__main__':
    main()
