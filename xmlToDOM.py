#!/usr/bin/python
# -*- coding: UTF-8 -*-
############################################################################
# Author: Diego Viniegra
# email: diego.viniegra@gmail.com
############################################################################

''' El objetivo de este módulo es recibir un documento xml (text/html por
ejemplo) y crear un DOM con sus funcionalidades. '''

import re, urllib, random




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
        self.childrens = self.parseHtml(self.innerHTML)

    def parseHtml(self, texthtml):
        # Encuentra hijos en una lista[contenido][nombre]
        exp = """(<(?P<etiq>[a-z][^>\s]*).*?>.*?</(?P=etiq)>)"""
        hijos = re.findall(exp, texthtml, re.S|re.I)
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
            attr = {}
            for n_attr in atrib:
                attr[n_attr[0]] = n_attr[2]

            #listElem[n] = element(self.idCount, ele[1], cnt[0], attr, self.id)
            x = element(types=ele[1], html=cnt[0], attr=attr, parent=self.id)
            #self.nodes.extend(x.childrens)
            self.nodes.extend(x.nodes)
            listElem.append(x)
            y = x.tree
            yy.append(y)
            n += 1
        self.nodes.extend(listElem)
        self.tree['childrens'] = yy
        return listElem

class newDOM(element):
    """docstring for newDOM"""
    def __init__(self, html):
        super(newDOM, self).__init__()
        self.id = str(random.randint(0, 10000)) + 'DOM'
        self.__name__ = 'DOM'
        self.tree = {
            "type": "DOM"
        }
        self.nodes = []
        self.childrens = self.parseHtml(html)

    def getElementById(self, id):
    	for ele in self.nodes:
            try:
                ele.attr['id']
            except KeyError:
                continue
            if ele.attr['id'] == id:
                return ele
        return None
