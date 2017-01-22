import urllib.request


class ClawlerByUrl:
    def getPageFromUrl(self, url):
        response = urllib.request.urlopen(url)
        content = response.read()
        return content

    def main(self, url):
        print("开始抓取···")
        print(url)
        page = self.getPageFromUrl(url)
        print("抓取结束 END")
        return page
