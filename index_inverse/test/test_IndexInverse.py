#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:41:56 2021


"""
import sys
sys.path.append('../src')
from IndexInverse import IndexInverse
import unittest

class TestIndexInverse(unittest.TestCase):
    def test_IndexInverse_1(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_docs_with_keyword('i')
            self.assertEqual(result,[0,1,2]) 
            
    def test_IndexInverse_2(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_docs_with_keyword('like')
            self.assertEqual(result,-1) 
			
    def test_IndexInverse_3(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_nb_documents()
            self.assertEqual(result,3) 
            
    def test_IndexInverse_4(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_nb_vocabularys()
            self.assertEqual(result,15) 

    def test_IndexInverse_5(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_vocabulary()
            self.assertEqual(result,    {'i': 0, 'love': 1, 'shanghai': 2, 'am': 3, 'from': 4, 'now': 5, 'study': 6, 'in': 7, 'tongji': 8, 
     'university': 9, 'lanzhou': 10, 'of': 11, 'science': 12, 'and': 13, 'technolgy': 14}) 

    def test_IndexInverse_6(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_document_id()
            self.assertEqual(result,{0: 'lipn.fr_1', 1: 'lipn.fr_2', 2: 'lipn.fr_3'})

    def test_IndexInverse_7(self):
            doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
            textes=['I love shanghai','i am from shanghai now i study in tongji university',
                    'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
            index=IndexInverse(doc,textes)
            index.create_index()
            result=index.get_docs_content()
            self.assertEqual(result,[['i', 'love', 'shanghai'], ['i', 'am', 'from', 'shanghai', 'now', 'i', 
                'study', 'in', 'tongji', 'university'], ['i', 'am', 'from', 'lanzhou', 'now', 'i', 'study', 
                    'in', 'lanzhou', 'university', 'of', 'science', 'and', 'technolgy']]) 



if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    