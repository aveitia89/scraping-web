# -*- coding: utf-8 -*-
__author__ = 'Juan Jose López Martínez'

import mongoengine

mongoengine.connect('vanguardia_web', host='127.0.0.1', port=27017)

class Category(mongoengine.Document):
    Category = mongoengine.StringField()
    SubCategories = mongoengine.ListField(mongoengine.StringField())
