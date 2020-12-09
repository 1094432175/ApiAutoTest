'''
Cookie;
http协议:无状态,无连接,媒体独立
每个请求都是独立的,有一些接口登录后才能访问,需要使用Cookie验证用户是否登录
account/dashboard 用户没有登录时,返回登录的页面
account/dashboard 如果登录了,返回用户的详细信息,浏览器登录后,获取到的Cookie直接放到自动化来用
如果Cookie失效或者换其他用户登录,就不能继续访问了
'''
import requests
#百格网站,有一些接口登录之后才能访问
print("未登录时,返回的结果为:")
url="https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

#用fiddler抓到的包,将里面的头设置到这里
head = {
    "Cookie":'Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606977451; MEIQIA_TRACK_ID=1l8Sw6lzTVeswMSx63s7HMgl1uK; MEIQIA_VISIT_ID=1l8Sw5MHp5g7soTBlY8YiFJd4JZ; __auc=ad665d141762751fb621abcb056; _ga=GA1.2.304704225.1606977454; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; BAGSESSIONID=ec5bad20-09d9-4bf2-82ad-68c2e2e78962'
}
print("登录后,返回结果为:")
r = requests.get(url,headers = head)
print(r.text)





















