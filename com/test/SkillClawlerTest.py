from com.xuzc.clawler.Clawler import ClawlerByUrl
from com.xuzc.htmlparser.HtmlParserUtil import HtmlParserFromString

if __name__ == '__main__':
    print("抓取技能")
    url = "http://skill-map.stuq.org/"
    clawler = ClawlerByUrl()
    page = clawler.main(url)
    print(str(page).lstrip("b"))
    tag = "script"
    parser = HtmlParserFromString(tag)
    data = parser.feed(str(page))
    print(parser.resdata)
    parser.close()
