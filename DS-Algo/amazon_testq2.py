# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:30:24 2019

@author: Shubham
"""

def retrieveMostFrequentlyUsedKeywords(literatureText, wordsToExclude):
	d = dict()
	ans = []
	text = literatureText.split()
	for word in text:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	keys = d.keys()
	values = d.values()
	val = list(set(text) - set(wordsToExclude))
	d1  = {key:d[key] for key in val}
	d1 = sorted(d1.items(), key=lambda x: x[1], reverse=True)
	n = len(d); c = 1
	for i in range(1, n):
		if d1[i][1] == d1[i-1][1]:
			c += 1
		else:
			break
	for ele in d1[:c]:
		if ele[0] not in wordsToExclude:
			ans.append(ele[0])
	return d1[:c], c, d, ans, val

literatureText = "jack and jill went to the market to buy bread and cheese cheese is jack favorite food"
wordsToExclude = ["and", "he", "the", "to", "is"]

str1= "rose is a flower rose is pond a flower rose flower in garden garden garden pond pond rose is a rose is a rose is a rose is a"
w = ["rose", "is", "a"]


ans,a, d, f, v = retrieveMostFrequentlyUsedKeywords(str1, w)