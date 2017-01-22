# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        HtmlParserUtil
# Purpose:
#
# Author:      Lagou
#
# Created:     2016/12/7
# Copyright:   (c) Lagou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import html.parser as h

class HtmlParserFromString(h.HTMLParser):
    resdata = []
    a_t=False
    def __init__(self, tag):
        self.tag = tag
        h.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        print("开始一个标签:",tag)
        print()
        if str(tag).startswith(self.tag):
            print(tag)
            self.a_t=True
            for attr in attrs:
                print("属性值：",attr)

    def handle_endtag(self, tag):
        if tag == self.tag:
            self.a_t=False
            #print("结束一个标签:",tag)

    def handle_data(self, data):
        if self.a_t is True:
            temp = data[data.find("var skills =")+13:data.find("var source")]
            temp = temp[:temp.rfind(";")]
            print("得到的数据: ",temp)
            if temp != None and temp != '' and temp.startswith('[{'):
                self.resdata.append(temp)