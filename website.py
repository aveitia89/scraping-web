# -*- coding: utf-8 -*-
__author__ = 'Juan Jose López Martínez'

class Website:
    #urls for pagination and image download
    url = "https://vanguardia.com.mx/rss?page="
    serverUrl ="http://52.201.109.206:3600/"

    # Document list Tags
    bodyIdTag = "HOTWordsTxt"
    noticiasTag = {'class': 'views-row'}
    autorTag = {'class': 'field--autor'}
    summaryTag = {'class': 'field--abstract'}
    titleTag = {'class': 'field--title'}
    dateFormatTag = {'class': 'field--timeago'}
    dateTag = {'class': 'timeago'}
    imagenTag = {'class': 'field--image'}
    especialTag = {'class': 'especial-vanguardia'}
    descripcionUrlTag = {'class': 'field--link-node'}
    lastPageTag = {'title': 'Ir a la última página'}
    pagesTag = {'class': 'pager__item pager__item--last'}

    # Document description Tag
    photoTag = 'field--photo'
    photoAutorTag = {'class': 'field--autor'}
    videoTag = 'field--video'
    textTag = 'field--text'
    internalLinkTag = 'field--title-field'
    tagstag = {'class': 'group-tags'}
    tagTag = {'class': 'field--topics'}
    ImageDescriptionSourceTag = {'class': 'field--source-image'}
    descriptionContentTag = "div.ds-1col.entity.entity-paragraphs-item.view-mode-full.clearfix"
    descriptionTextTag = "field--text"
    subCategoriaTag = "field--section"
    authorImageTag = {'class', 'field--avatar--author'}

    # Document Especial description Tag

    # Variables for pagination
    firstPageValue = 0
    lastPageValue = 16670

    #categories dictionaries
    subCategoriesDict = {'Nacional': 'Noticias',
                        'Internacional': 'Noticias',
                        'Noticias': 'Noticias',
                        'Torreón': 'Coahuila',
                        'Monclova': 'Coahuila',
                        'Acuña': 'Coahuila',
                        'Sabinas': 'Coahuila',
                        'Piedras Negras': 'Coahuila',
                        'Saltillo': 'Coahuila',
                        'Coahuila': 'Coahuila',
                        'Cartones': 'Opinión',
                        'Politicón': 'Opinión',
                        'Opinión': 'Opinión',
                        'Dinero': 'Dinero',
                        'Fútbol': 'Deportes',
                        'Fútbol Internacional': 'Deportes',
                        'Béisbol': 'Deportes',
                        'Automovilismo': 'Deportes',
                        'Fútbol Americano': 'Deportes',
                        'Basquetbol': 'Deportes',
                        'Tenis': 'Deportes',
                        'Deportes': 'Deportes',
                        'Artes': 'Show',
                        'Cine': 'Show',
                        'Show': 'Show',
                        'Celures': 'Tech',
                        'Computadoras': 'Tech',
                        'Gadgets': 'Tech',
                        'Videojuegos': 'Tech',
                        'Tech': 'Tech',
                        'Bienestar': 'Buena Vida',
                        'Nutrición': 'Buena Vida',
                        'Gourmet': 'Buena Vida',
                        'Viajes': 'Buena Vida',
                        'Sexo': 'Buena Vida',
                        'Viral': 'Buena Vida',
                        'Buena Vida': 'Buena Vida',
                        'Autos': 'Motor',
                        'Suvs': 'Motor',
                        'Pick Up': 'Motor',
                        'Racing': 'Motor',
                        'Motos': 'Motor',
                        'Taller': 'Motor',
                        'Motor': 'Motor'
                        }