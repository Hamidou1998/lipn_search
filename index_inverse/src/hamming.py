# -*- coding: utf-8 -*-

# @param u : un mot de longueur n
# @param v : un mot de longueur n
# @contrainte Longueur de u et v dois être égale 
# @return -1 si longueur de u et v ne sont pas égale


def hamming(u,v):
	tmp=0
	if(len(u)!=len(v)):
		return -1
	for i in range(len(u)):
		if(u[i]!=v[i]):
			tmp=tmp+1
	return tmp
