#!/usr/bin/env python
#coding: utf-8
import requests

headers = {
    User-Agent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    Referer: 'https://accounts.douban.com'
}

def login():
    response = requests.get('https://www.douban.com/misc/captcha',
        headers = headers)
    result = response.json()
    captchaUrl = result['url']
    captchaToken = result['token']
    print(captchaUrl, captchaToken)
    response = requests.get('https:' + captchaUrl, headers = headers)
    codeImg = response.content
    fm = open('code.png', 'wb')
    fm.write(codeImg)
    fm.close()
    # data = {
    #     source: 'index_nav',
    #     redir: 'https://www.douban.com/',
    #     form_email: '18126015210',
    #     form_password: 'nokia0505615',
    #     captcha-solution: 'spade',
    #     captcha-id: 'IkETilS80tCCbD9xfA4yiZ9q:en',
    #     login: '登录'
    # }
    # response = requests.post('https://accounts.douban.com/login',
    #     data = data, headers = headers)
    # print(response.url)
    # print(response.text)


login()