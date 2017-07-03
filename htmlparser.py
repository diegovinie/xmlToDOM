import re, urllib

class element(object):
    def __init__(self, name='', html='', attr=''):
        self.html = html
        self.name = name
        self.attr = attr
    def __str__(self):
        return self.name

url = 'http://localhost/index.html'

body = element()

html = urllib.urlopen(url).read()

body.html = re.findall('''<body[^>]*>(.*)</body>''', html, re.I|re.S)

html2 = body.html

html3 = re.findall('''<[^>]+>''', html2[0], re.I|re.S)

regObj = re.search('''<(?P<tag>[^\s\n>]+)>(.*)</(?P=tag)''', html2[0], re.S)



v = re.findall('''<([^/>\s\n]+)''', html2[0], re.S)
ele = []
dic = {}
lis = []
n = 0
for name in v:
    attr = re.findall('<[^\s>]+(.*)>', html2[0], re.S)
    reExp = '<'+name+'[^>]*>(.*)</'+name
    res = re.findall(reExp, html2[0], re.S)
    if res == []:
        res.append('')
    ob = element(name, res[0], attr)
    ele.append(ob)
    dic[name] = [attr, res[0]]
    lis.append({'nombre': name, 'attributos': attr, 'html': res[0]})
    
