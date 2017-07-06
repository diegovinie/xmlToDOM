import re, urllib, random

objects = []


class newDOM(object):
    """docstring for newDOM"""
    def __init__(self, html):
        super(newDOM, self).__init__()
        self.id = str(random.randint(0, 10000)) + 'DOM'
        self.__name__ = 'DOM'
        self.tree = {
            "type": "DOM"
        }
        self.nodes = []
        self.hijos = self.parseHtml(html)

    def parseHtml(self, html):
        # Encuentra hijos en una lista[contenido][nombre]
        exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
        hijos = re.findall(exp, html, re.S|re.I)
        #listElem = range(0, len(hijos))
        listElem = []
        n = 0
        yy = []
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
            #listElem[n] = element(self.idCount, ele[1], cnt[0], attr)

            x = element(types=ele[1], html=cnt[0], attr=attr, parent=self.id)

            y = x.tree

            yy.append(y)
            listElem.append(x)
            objects.append(x)
            n += 1
        self.tree['childrens'] = yy
        return listElem


class element(object):
    def __init__(self, types='', html='', attr='', parent=''):
        self.__str__ = types
        self.id = str(random.randint(0, 10000)) + types
        self.innerHTML = html
        self.type = types
        self.attr = attr
        self.parent = parent
        self.nodes = []
        self.tree = {
            "id": self.id,
            "type": self.type,
            "attr": self.attr,
            #"innerHTML": self.innerHTML,
            "parent": self.parent,
            #"childrens": []
        }
        self.childrens = self.parseHijos()


    def parseHijos(self):
        # Encuentra hijos en una lista[contenido][nombre]
        exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
        hijos = re.findall(exp, self.innerHTML, re.S|re.I)
        #listElem = range(0, len(hijos))
        listElem = []
        n = 0
        yy = []
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
            #listElem[n] = element(self.idCount, ele[1], cnt[0], attr, self.id)
            x = element(types=ele[1], html=cnt[0], attr=attr, parent=self.id)
            self.nodes.extend(x.childrens)
            listElem.append(x)
            objects.append(x)
            y = x.tree
            yy.append(y)
            n += 1
        self.nodes.extend(listElem)
        self.tree['childrens'] = yy
        return listElem
