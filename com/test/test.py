# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        test
# Purpose:
#
# Author:      Lagou
#
# Created:     2016/12/7
# Copyright:   (c) Lagou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import html.parser as h

class MyHTMLParser(h.HTMLParser):
    a_t=False
    def handle_starttag(self, tag, attrs):
        #print("开始一个标签:",tag)
        print()
        if str(tag).startswith("title"):
            print(tag)
            self.a_t=True
            for attr in attrs:
                print("   属性值：",attr)

    def handle_endtag(self, tag):
        if tag == "title":
            self.a_t=False
            #print("结束一个标签:",tag)

    def handle_data(self, data):
        if self.a_t is True:
            print("得到的数据: ",data)



p=MyHTMLParser()

p.feed("<html> <title id='main' mouse='你好'>我是标题</title><body>我是内容</body>   </html>")

p.close()