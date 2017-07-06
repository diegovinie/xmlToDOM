import re, urllib



class element(object):
    def __init__(self, oid='', types='', html='', attr='', parent=''):
        self.id = oid
        self.idCount = 0
        self.innerHTML = html
        self.type = types
        self.attr = attr
        self.parent = parent
        self.childrens = self.parseHijos()

    def parseHijos(self):
        # Encuentra hijos en una lista[contenido][nombre]
        exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
        hijos = re.findall(exp, self.innerHTML, re.S|re.I)
        listElem = range(0, len(hijos))
        n = 0
        for ele in hijos:
            exp1 = '<' + ele[1] + '[\s?](.*)>'
            cab = re.findall(exp1, ele[0], re.I)
            # innerHTML
            exp2 = """<[a-z][^>]*?>(.*)</"""
            cnt = re.findall(exp2, ele[0], re.S|re.I)
            # Encuentra los atributos y los guarda como lista[dic]
            exp3 = '''([a-z][^=]*)=(?P<e>['"])(.+?)(?P=e)'''
            try:
                atrib = re.findall(exp3 , cab[0])
            except IndexError:
                atrib = ''
            j = 0
            attr = range(0, len(atrib))
            for n_attr in atrib:
                attr[j] = {n_attr[0]: n_attr[2]}
                j += 1
            listElem[n] = element(self.idCount, ele[1], cnt[0], attr, self.id)
            self.idCount += 1
            n += 1
        return listElem

    def __str__(self):
        return self.type

def parseHtml(html):
    # Encuentra hijos en una lista[contenido][nombre]
    exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
    hijos = re.findall(exp, html, re.S|re.I)
    listElem = range(0, len(hijos))
    n = 0
    for ele in hijos:
        exp1 = '<' + ele[1] + '[\s?](.*)>'
        cab = re.findall(exp1, ele[0], re.I)
        # innerHTML
        exp2 = """<[a-z][^>]*?>(.*)</"""
        cnt = re.findall(exp2, ele[0], re.S|re.I)
        # Encuentra los atributos y los guarda como lista[dic]
        exp3 = '''([a-z][^=]*)=(?P<e>['"])(.+?)(?P=e)'''
        atrib = re.findall(exp3 , cab[0])
        j = 0
        attr = range(0, len(atrib))
        for n_attr in atrib:
            attr[j] = {n_attr[0]: n_attr[2]}
            j += 1
        listElem[n] = element(ele[1], cnt[0], attr)
        n += 1
    return listElem

def parseHijos(padre):
    html = padre.innerHTML
    listElem = parseHtml(html)
    return listElem

class newDOM(object):
    """docstring for newDOM"""
    def __init__(self, html):
        super(newDOM, self).__init__()
        self.idCount = 0
        self.hijos = self.parseHtml(html)
        self.__name__ = 'DOM'
        #self.todosHijos = self.recurs(self.hijos)

    def parseHtml(self, html):
        # Encuentra hijos en una lista[contenido][nombre]
        exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
        hijos = re.findall(exp, html, re.S|re.I)
        listElem = range(0, len(hijos))
        n = 0
        for ele in hijos:
            exp1 = '<' + ele[1] + '[\s?](.*)>'
            cab = re.findall(exp1, ele[0], re.I)
            # innerHTML
            exp2 = """<[a-z][^>]*?>(.*)</"""
            cnt = re.findall(exp2, ele[0], re.S|re.I)
            # Encuentra los atributos y los guarda como lista[dic]
            exp3 = '''([a-z][^=]*)=(?P<e>['"])(.+?)(?P=e)'''
            atrib = re.findall(exp3 , cab[0])
            j = 0
            attr = range(0, len(atrib))
            for n_attr in atrib:
                attr[j] = {n_attr[0]: n_attr[2]}
                j += 1
            listElem[n] = element(self.idCount, ele[1], cnt[0], attr)
            self.idCount += 1
            n += 1
        return listElem

    def parseHijos(self, padre):
        html = padre.innerHTML
        # Encuentra hijos en una lista[contenido][nombre]
        exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
        hijos = re.findall(exp, html, re.S|re.I)
        listElem = range(0, len(hijos))
        n = 0
        for ele in hijos:
            exp1 = '<' + ele[1] + '[\s?](.*)>'
            cab = re.findall(exp1, ele[0], re.I)
            # innerHTML
            exp2 = """<[a-z][^>]*?>(.*)</"""
            cnt = re.findall(exp2, ele[0], re.S|re.I)
            # Encuentra los atributos y los guarda como lista[dic]
            exp3 = '''([a-z][^=]*)=(?P<e>['"])(.+?)(?P=e)'''
            atrib = re.findall(exp3 , cab[0])
            j = 0
            attr = range(0, len(atrib))
            for n_attr in atrib:
                attr[j] = {n_attr[0]: n_attr[2]}
                j += 1
            listElem[n] = element(self.idCount, ele[1], cnt[0], attr, padre.id)
            self.idCount += 1
            n += 1
        return listElem

    def recurs(self, hijos):
        lista = []
        for ele in hijos:
            nieto = self.parseHijos(ele)
            lista.append(nieto)
        return lista


a = open('prueba.xml', 'r').read()

#her = parseHtml(a)

#otr = parseHijos(her[0])


url = 'http://localhost/index.html'

body = element()

html = urllib.urlopen(url).read()

#fer = parseHtml(html)

body.html = re.findall('''<body[^>]*>(.*)</body>''', html, re.I|re.S)

html2 = body.html

html3 = re.findall('''<[^>]+>''', html2[0], re.I|re.S)

regObj = re.search('''<(?P<tag>[^\s\n>]+)>(.*)</(?P=tag)''', html2[0], re.S)
