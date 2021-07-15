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
import directory
from website import Website
from awsS3 import upload_file
import slug
import urllib
from file_uploader import file_upload

class Crawler:
    
    #Se obtiene el BeatifutSoup object de la url
    def getPage(self, url):
        print("Url:"+url)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            req = requests.get(url, headers = headers)
        except requests.exceptions.RequestException:
            print("getPage method error")
            return None
        return BeautifulSoup(req.text, 'html.parser')

    #Download source in especific pathfileName
    def downloand(self, url, object_name):
        try:
            print("Entro al metodo")
            
            #El link de la imagen
            imagen = requests.get(url).content
            img_name = url.split('/')
            pos = len(img_name) - 1
            dirUrl = "download/"+img_name[pos]
            with open(dirUrl, 'wb') as handler:
                handler.write(imagen)
            #img = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
            #img = urllib.request.urlretrieve(url, object_name)
            #file_img = img.raw
            file_upload(dirUrl, img_name[pos])
            #return upload_file(file_img, object_name)
        except Exception as ex:
            print("Entro a la excepcion")
            print(ex)
            return ''
        #img = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        #file_img = img.raw
        #return upload_file(file_img, object_name)
        # # with open(fileName, "wb") as file:
        # #     response = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        # #     file.write(response.content)

    def getElement(self, bs, tag, element = 'div'):
        return bs.find(element,tag)

    def getElementText(self, bs, tag, element = 'div'):
        try:
            return bs.find(element,tag).getText()
        except:
            return ""

    def getAtributeText(self, bs, tag, atribute, element='div'):
        try:
            return bs.find(element,tag)[atribute]
        except:
            return None

    #Get new date field
    def getDateElement(self, bs):
        tempDate = self.getAtributeText(bs, Website.dateTag, "title", "span")
        if tempDate is not None:
            stringDate = tempDate.split('T')[0] + " " + tempDate.split('T')[1].split('-')[0]
            return datetime.datetime.strptime(stringDate,'%Y-%m-%d %H:%M:%S')
        else:
            return None

    def getLastPageElementValue(self, bs):
        try:
            lastPage = self.getElement(bs, pagesTag,'li')
            return int(lastPage.a['href'].split('=')[1])
        except:
            return 16676

    def getImage(self, url, file1x):
        try:
            url1 = url.split(' ')[0]
            name = uuid.uuid1()
            file_img = file1x + '/' + str(name) + '.' + mimetypes.guess_type(url1)[0].split('/')[1]
            result = self.downloand(url1, file_img)
            return file_img if result else ""
        except:
            print("getImage method error")
            return ""
    
    #Get photo autor with diferent dimension
    def getImagesInSrcset(self, url,file1x, file2x):
        try:
            url1= url.split(',')[0].split(' ')[0]
            url2= url.split(' 1x, ')[1].split(' ')[0]
            name = uuid.uuid1()
            file_img1 = file1x + '/' + str(name) + "." + mimetypes.guess_type(url1)[0].split('/')[1]
            file_img2 = file2x + '/' + str(name) + "." + mimetypes.guess_type(url2)[0].split('/')[1]
            result1 = self.downloand(url1, file_img1)
            result2 = self.downloand(url2, file_img2)
            return [file_img1 if result1 else "", file_img2 if result2 else ""]
        except Exception as e:
            print(e)
            print("getImageAutor method error")
            return ["",""]

    def getTags(self, bs):
        try:
            tags = [tag.a.getText() for tag in self.getElement(bs.contents[1],Website.tagstag).find_all('div')]
            return tags
        except:
            print("getTags method error")
            return []

    def getDescriptionBody(self, bs):
        try:            
            descripcion = bs.contents[1].select(Website.descriptionContentTag)
            #Filtrando pr los bloques de descripcion que no sean links internos
            newDescripcion = list(filter(lambda element: element.div['class'] != [Website.internalLinkTag], descripcion))
            return list(map(str, newDescripcion))
            # return ''.join(map(str,newDescripcion))
        except:
            print("getDiscptionBody method error")
            return []

    def getDescriptionSource(self, bs, especial):
        if especial:
            try:                
                source = bs.find('div',Website.imagenTag)
                print(source)
                if source is not None:
                    imagenes = []
                    try: 
                        downloadFolders = [
                            ("paragraph_image_large_desktop_1x","paragraph_image_large_desktop_2x"),
                            ("paragraph_image_desktop_1x","paragraph_image_desktop_2x"),
                            ("paragraph_image_table_1x","paragraph_image_table_2x"),
                            ("paragraph_image_phone_1x","paragraph_image_phone_2x")]
                        for i in range(4):
                            images = self.getImagesInSrcset(source.find_all('source')[i]['srcset'], downloadFolders[i][0],downloadFolders[i][1])
                            print(images)
                            imagenes.append(images[0])
                            imagenes.append(images[1])
                    except Exception as e:
                        print(e)

                    try:
                        imagenSource = self.getElementText(bs.div.div.div, Website.ImageDescriptionSourceTag)
                    except Exception as e:
                        print(e)
                        imagenSource = ""

                    return imagenes, imagenSource
                else:
                    return [bs.div.div.div.div.div.div.iframe["src"]], ""
            except:
                print("getDescriptionSource method error")
                return [], ""
        else:
            try:
                if bs.div.div.div.div["class"] == [Website.photoTag]:
                    imagenes = []
                    try:
                        downloadFolders = [
                            ("paragraph_image_large_desktop_1x","paragraph_image_large_desktop_2x"),
                            ("paragraph_image_desktop_1x","paragraph_image_desktop_2x"),
                            ("paragraph_image_table_1x","paragraph_image_table_2x"),
                            ("paragraph_image_phone_1x","paragraph_image_phone_2x")]
                        for i in range(4):
                            images = self.getImagesInSrcset(bs.div.div.div.div.find_all('source')[i]['srcset'], downloadFolders[i][0],downloadFolders[i][1])
                            imagenes.append(images[0])
                            imagenes.append(images[1])
                    except Exception as e:
                        print(e)

                    try:
                        imagenSource = self.getElementText(bs.div.div.div, Website.ImageDescriptionSourceTag)
                    except Exception as e:
                        print(e)
                        imagenSource = ""

                    return imagenes, imagenSource
                else:
                    return [bs.div.div.div.div.div.div.iframe["src"]], ""
            except:
                print("getDescriptionSource method error")
                return [], ""

    def analyzeDescription(self, url, especial, imagen):
        bs = self.getPage(url)
        if bs is not None:
            body = bs.find(id=Website.bodyIdTag)

            #Buscando Subcategoria
            subCategoria = self.getElementText(self.getElement(bs, Website.subCategoriaTag),{},'span')

            #Obteniendo Categoria
            try:
                categoria = Website.subCategoriesDict[subCategoria]
            except:
                print("analyzeDescription method error")
                categoria = subCategoria
            
            #Obteniendo Imagenes y ImageSource 
            imagesDescription, imageSource = self.getDescriptionSource(body, especial)
            # print(imagesDescription)

            #obteniendo foto Autor
            try:
                imagesAutor = self.getElement(bs, Website.photoAutorTag).find_all('source')
                url = imagesAutor[0]['srcset']
                fotosAutor = self.getImagesInSrcset(url, 'avatar_1x', 'avatar_2x')
            except Exception as e:
                print(e)
                print("analyzeDescription method(foto Autor) error")
                fotosAutor = []
            
            # Obteniendo foto Autor en caso que el tipo de descripcion no sea con foto
            if imagen:
                try:
                    imagen = bs.find('div',{'class', 'group-highlight field-group-div'}).find('source')
                    url = imagen['srcset']
                    fotosAutor = self.getImagesInSrcset(url, "avatar_thumb_1x", "avatar_thumb_2x")
                except:
                    print("analyzeDescription method(foto Autor2) error")
                    fotosAutor = []    
            # print(fotosAutor)  
                                    
            # Obteniendo tags
            tags = self.getTags(body)

            #Obteniendo el cuerpo de la descripcion
            descripcion = self.getDescriptionBody(body)
            return tags, imagesDescription, descripcion, fotosAutor, categoria, subCategoria, imageSource
        else:
            print("La url de descripcion de la noticia" + url + " es None")
            return [], "", "", "", "", "",""

    #TODO: Arreglar el return por default del lastPageVAlue cuando lo ptuebe
    def newAnalyzer(self, bs, currentPage):
        noticias = []
        try:
            noticias = bs.find_all('div',Website.noticiasTag)
        except:
            print("newAnalizer methid error")
        i=0
        for noticia in noticias:

            new = New()
            newDetails = NewDetails()
            
            new.Date = self.getDateElement(noticia)
            new.Title = self.getElementText(noticia, Website.titleTag)

            dbNew = New.objects(Date = new.Date, Title = new.Title).first()  
            print(dbNew)
            if dbNew is None:
                new.Autor = self.getElementText(noticia, Website.autorTag)
                new.DateFormat = self.getElementText(noticia, Website.dateFormatTag)
                new.Sumary = self.getElementText(noticia, Website.summaryTag)
                new.Especial = self.getElement(noticia, Website.especialTag) is not None

                dateElement = self.getElement(noticia, Website.descripcionUrlTag)
                descripcionUrl = self.getAtributeText(dateElement, {}, 'href', 'a')
                
                try:
                    imagenes = self.getElement(noticia, Website.imagenTag).find_all('source')
                    url = imagenes[0]['srcset']
                    # print("url de descarga lista:" + url)
                    new.Images = self.getImagesInSrcset(url, "list_medium_1x", "list_medium_2x")
                    new.Images.append(self.getImage(url, "list_large_1x"))
                except Exception as e:
                    print(e)
                    new.Images = []

                new.Tags, newDetails.SourceDescription, newDetails.Description, newDetails.ImagesAutor, new.Category, new.SubCategory, newDetails.SourceDescriptionText = self.analyzeDescription(descripcionUrl, new.Especial, len(new.Images) == 0)

                # print("")
                # print("""    
                #     Description: %s \n       
                #     SourceDescriptionText: %s \n 
                #     ImagesAutor: %s \n 
                #     SourceDescription: %s \n
                #     """\
                #     %(
                        
                #     # newDetails.Description,
                #     "",
                #     newDetails.SourceDescriptionText,
                #     newDetails.ImagesAutor, 
                #     newDetails.SourceDescription))
                # return
                # print( """
                #     Autor: %s \n 
                #     Images: %s \n 
                #     Sumary: %s \n 
                #     Date: %s \n 
                #     Title: %s \n
                #     Tags: %s \n 
                #     Category: %s \n 
                #     SubCategory: %s \n
                #     DateFormat: %s \n 
                #     Especial: %s \n
                #     """\
                #     %(new.Autor,
                #     new.Images, 
                #     new.Sumary, 
                #     new.Date,
                #     new.Title, 
                #     new.Tags, 
                #     new.Category,
                #     new.SubCategory,  
                #     new.DateFormat,  
                #     new.Especial))       
                try:     
                    new.LinkUrl = slug.slug(new.Title)                  
                    newDetails.save()
                    new.Details = newDetails
                    new.save()
                    print("Noticia "+str(i)+" guardada con exito")
                except Exception as e:
                    print(e)

    def parseFirtsPage(self):
        bs = self.getPage(Website.url + str(Website.firstPageValue))
        if bs is not None:
            body = bs.find(id = Website.bodyIdTag)
            self.newAnalyzer(body, Website.firstPageValue)                        
        else:
            print("Is None First Pages in Timer")

    def parseAllPages(self):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(Website.url + str(Website.firstPageValue))
        if bs is not None:
            body = bs.find(id = Website.bodyIdTag)
            lastPageValue = self.getLastPageElementValue(body.ul)
            for currentPage in reversed(range(lastPageValue)):
                print(currentPage)
                if currentPage != 0:
                    bs = self.getPage(Website.url + str(currentPage))
                    if bs is not None:
                        body = bs.find(id = Website.bodyIdTag)
                        self.newAnalyzer(body, currentPage)
                    else:
                        print("Error leyendo pagina" + str(currentPage))
                else:                    
                    self.newAnalyzer(body, currentPage)                        
        else:
            print("Is None")
