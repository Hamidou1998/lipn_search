#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:11:24 2021


"""

class IndexInverse :

    """Classe pour l'index inverse : 
    - document_id:  C'est un dictionnaire de document_id (ici url est document_id)
    - docs_content: List de Contenu,le contenu de l'article sur chaque document_id
    - invert_index: Ceci est un index qui sera créé par notre classe. La valeur initiale est vide.
    - vocabulary:   C'est un dictionnaire qui contient des mots apparus dans tous les documents. 
                    Chaque mot a son ID. ex:{'I':0,'am':1} (Même ordre avec les mots qui sont dans invert_index )
    """

    docuCount=0 #Le nombre de documents dans la classe
    vocaCount=0 #Le nombre de mots dans le dictionnaire vocabulary
    def __init__(self,list_urls, list_content):
        '''Constructeur IndexInverse'''
        if len(list_urls)==len(list_content):  #données valides
            self.document_id = dict(zip(range(len(list_urls)), list_urls))
            doc= [c.lower().replace(",", "").replace("/n", "").split(" ") for c in list_content]
            for d in doc:
                while '' in d:
                    d.remove('')
            self.docs_content=doc 
            self.invert_index=dict()
            self.vocabulary=dict()
            IndexInverse.docuCount= len(list_urls)
        else:
            #erreur: la taille de list_url faut egale à la taille de list_contenu
            raise Exception("Invalid parameter!")
            

            print("je suis dans l'index")

        
    def create_index (self):
        ''' Créer le dictionnaire invert_index. 
            Dans ce dictionnaire, chaque mot qui apparaît dans les documents est une clé (key).
            La valeur correspondant à la clé est une liste, qui enregistre les documents (document_id) dans lesquels le mot apparaît.
        '''
        a=0
        for doc_id,article in zip(range(IndexInverse.docuCount),self.docs_content):
            for word in article:
                if word in self.invert_index:
                    if not doc_id in self.invert_index[word]:
                        self.invert_index.setdefault(word,[]).append(doc_id)
                else:
                    self.vocabulary[word]=a
                    a=a+1
                    self.invert_index.setdefault(word,[]).append(doc_id) 
        IndexInverse.vocaCount=len(self.vocabulary)
        print(IndexInverse.vocaCount)
                               
    
    def get_index(self):
        '''Obtenir le dictionnaire invert_index.
        '''
        return self.invert_index        
             
    def get_docs_with_keyword(self,word):
        ''' 
        Renvoyer une liste de document_id dans lesquels le mot (word) apparaît.
        '''
        if word in self.invert_index:
            return self.invert_index[word]
        else:
            print('Error keyword')
            return -1

    def get_nb_documents(self):
        '''Renvoyer le nombre de documents dans ce classe
        '''
        return IndexInverse.docuCount

    def get_nb_vocabularys(self):
        '''Renvoyer le nombre de mots dans le dictionnaire vocabulary
        '''
        return IndexInverse.vocaCount

    def get_vocabulary(self):
        '''Renvoyer le dictionnaire qui contient des mots 
        '''
        return self.vocabulary
    
    def get_document_id (self):
        '''Renvoyer le dictionnaire de document_id.
        '''
        return self.document_id
    
    def get_docs_content(self):

        '''Renvoyer la list de Contenu 
        '''
        return self.docs_content
    
    def show_index(self):

        '''Imprimer le dictionnaire invert_index.
        '''
        print ('NbDocument='+str(IndexInverse.docuCount))
        for word, IDs in self.invert_index.items():
            print('')
            print(word+':',end=' ')
            for ID in IDs:
                print (ID,end=' ')
        return  
    def search(self,request):
        
        ''' C est une fonction qui retourne juste la liste des chaines de caracteres 
        '''
        
        list_contenu=[]
        list_contenu.append("www."+str("".join(request))+".com")
        return list_contenu


