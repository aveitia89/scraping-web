# -*- coding: utf-8 -*-
__author__ = 'Juan Jose López Martínez'

from bs4 import BeautifulSoup
import requests
import re
import json
import datetime
import mimetypes
from new import New, NewDetails
import uuid
from category import Category

class CrawlerMenu:
    
    #Se obtiene el BeatifutSoup object de la url
    def getPage(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3'}
            req = requests.get(url, headers = headers)
        #     req =  open("view.html")
        # except Exception as ex:
        #     print(ex)
        #     return None
        # return BeautifulSoup(req.read(), 'html.parser')
        except requests.exceptions.RequestException:
            print("getPage method error")
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def getElement(self, bs, tag, element = 'div'):
        return bs.find(element,tag)

    def getElementText(self, bs, tag, element = 'div'):
        try:
            return bs.find(element,tag).getText()
        except:
            return ""
    
    def parseAllPages(self):
        """
        Extract content from a given page URL
        """
        bs = self.getPage('https://vanguardia.com.mx/')
        if bs is not None:
            body = bs.find_all('span', {'class': 'mrf-listMenu__title mrf-listMenu__subsectionTitle'})
            print(len(body))
            for tag in body:
                #  print(tag.span.find_parent('a')['class'])
                category = Category()
                category_name = tag.span.getText()
                find = category.objects(Category = category_name)
                if find is not None:
                    category.category_name = 
                print(tag.span.getText())
                category_list = list(map(lambda elements: elements.getText(),tag.span.find_parent('a').findNext("ul").find_all("span")))
                print(list(filter(lambda sub_cat: sub_cat not in ['\n\n\n\n\n\n\n\n','\nDESCARGADO\n\n', '\nACTUALIZACIÓN DISPONIBLE\n', ''],category_list)))

crawler = CrawlerMenu()
crawler.parseAllPages()
