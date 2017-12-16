from urllib import request
import re
class Spider():
    url = 'https://www.panda.tv/cate/kingglory'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        # this is a http request
        ret = request.urlopen(Spider.url)  
        htmls = ret.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        
        return anchors

    # 数据精炼 去除字符串空格，把列表变成字符串
    def __refine(self,anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]    
        }
        return map(l,anchors)
    
    # 数据排序
    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number    
        # return anchor['number']

    def __show(self,anchors):
        # for anchor in anchors:
        for rank in range(0,len(anchors)):
            print('rank-'+ str(rank+1)+' : '+anchors[rank]['name']+'   '+ anchors[rank]['number']+'人')
    
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)

spider = Spider()
spider.go()           