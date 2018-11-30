import requests
import json

def get_comments(url):
    name_id = url.split('=')[1]  #用等号分割然后获取第一个元素

    
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'
               ,'referer': "https://music.163.com"
        }


    # 这个查询命令是POST形式，需要给服务器一个data才会返回需要的内容。
    # 通过审查元素我们可以发现Form Data就是我们要发给服务器的内容
    params = "bz9+6pfMsMK/mU90aEg3Oq921z9WKZ1jBgPriPvHwYW9Y/gFv+MN5JFegr3jgbRAiMwm50a8LWBEoQ0FPe9xq0PBuODa45o2N16omn5MTxUxHRHg0At4OUSbMv3jQghxKyNmpVqxvRxTFVyKMBst2RNr+vILDi4kCYE1CIRnJjn4miJ3+ZYWbJtf8fX3h9/w"

    encSecKey = "546b96385bff312329af31e012a44bea4d1aa53390462148762ead569f529a1a15be9e9d5013a297e4e80ab7ba78d434652122aee4156b015b46c367b0bb39874d805cc2038e2b75253d44b9c9a4d35e35864213c04003ffd64ef4044931485a78073e31e5e8515976eabb10909bf5416fe2f65cecc1b9f293e1324edf52ac98"

    data = { "params" : params,
             "encSecKey": encSecKey
        }# 以字典形式传递这两个参数
    

    # 注意这个URL不是网页的URL，而是具有hotcomments的URL，这两个不是一个URL
    '''
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_4466775?csrf_token="
    注意到最后那一串数字实际上是歌曲的编号，为了可以获取任意一首歌曲的评论，我们可以用name_id参数
    来获取网页URL中的歌曲编号，然后传给target_url
    

    '''
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    
    res = requests.post(target_url, headers=headers, data=data)

    return res


def get_hot_comments(res):
    # res.text得到的是一个JSON的格式
    comments_json = json.loads(res.text)   #将字符串还原为Python的数据结构
    hot_comments = comments_json["hotComments"]
    with open("e:\\hot_comments.txt", "w", encoding="utf-8") as file:
        for each in hot_comments:
            file.write(each["user"]["nickname"]+ ":\n\n")
            file.write(each["content"]+ ":\n")
            file.write("-----------------------------------------------------\n")


    

def main():
    url = input('请输入链接地址：')
    res = get_comments(url)
    get_hot_comments(res)
    #print(res.encoding)
    #with open('e:\\data.txt','w',encoding = 'utf-8') as  file :
     #   file.write(res.text)    

if __name__ == "__main__" :
    main()
