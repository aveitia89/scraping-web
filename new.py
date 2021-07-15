# -*- coding: utf-8 -*-
__author__ = 'Juan Jose López Martínez'

import mongoengine

mongoengine.connect('reportero_vanguardia', host='127.0.0.1', port=27017)
#mongoengine.connect('vanguardia_web', host='74.208.207.49', port=8003)

class NewDetails(mongoengine.Document):
    Description = mongoengine.ListField(mongoengine.StringField())
    SourceDescriptionText = mongoengine.StringField()
    ImagesAutor = mongoengine.ListField(mongoengine.StringField())
    SourceDescription = mongoengine.ListField(mongoengine.StringField())
    meta={'collection': 'newsdetails'}

class New(mongoengine.Document):
    LinkUrl = mongoengine.StringField()
    Title = mongoengine.StringField()
    Autor = mongoengine.StringField()
    Category = mongoengine.StringField()
    SubCategory = mongoengine.StringField()
    Sumary = mongoengine.StringField()
    Date = mongoengine.DateTimeField() 
    DateFormat = mongoengine.StringField()
    Tags = mongoengine.ListField(mongoengine.StringField())
    Especial = mongoengine.BooleanField()
    Images = mongoengine.ListField(mongoengine.StringField())   
    Details = mongoengine.ReferenceField(NewDetails)
    meta = {
        'collection': 'news',
        'indexes': ['Autor', 'Category', 'Tags', 'SubCategory', 'LinkUrl']
    }