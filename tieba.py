#coding:utf-8

import requests
import sys


class Tieba(object):
    # 初始化
    def __init__(self, tieba_name, pn):
        # 保存贴吧名，为了构建文件名
        self.tieba_name = tieba_name
        # 字符串格式化
        self.base_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(tieba_name)

        # 列表表达式
        self.url_list = [self.base_url + str(i*50) for i in range(pn)]

        # 构建请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

        # 测试是否获取到值
        # print (self.url_list)
        # print (self.base_url)

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def save_data(self, response, number):
        # 拼接文件名
        filename = self.tieba_name + "_" + str(number) + ".html"
        # 写入文件
        with open(filename, 'w')as f:
            f.write(response.content.decode())

    def run(self):
        pass
        # 1 构建一个url列表
        # 2 构建请求头
        # 3 遍历列表
        for url in self.url_list:
            # 对每一个url发送请求获取响应
            response = self.get_page(url)
            # 将响应数据写入文件
            # 获取索引值
            number = self.url_list.index(url)
            self.save_data(response, number)

if __name__ == '__main__':
    tieba = Tieba("美食", 2)
    tieba.run()
