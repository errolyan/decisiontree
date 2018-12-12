#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# __Date__: 18-12-10
# __Describe__ = "决策树ID3算法算法Python实现版本”
import Node

data = [[]]
f = open('./DataSet/Buyhouse.csv')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'\xe5\xb9\xb4\xe9\xbe\x84': {'A': {'\xe6\x80\xa7\xe5\x88\xab': {'\xe5\xa5\xb3': '\xe5\x90\xa6', '\xe7\x94\xb7': {'\xe6\x94\xb6\xe5\x85\xa5\xe7\xad\x89\xe7\xba\xa7': {'\xe9\xab\x98': '\xe6\x98\xaf', '\xe4\xbd\x8e': '\xe5\x90\xa6'}}}}, 'C': {'\xe6\x80\xa7\xe5\x88\xab': {'\xe5\xa5\xb3': '\xe6\x98\xaf', '\xe7\x94\xb7': {'\xe6\x94\xb6\xe5\x85\xa5\xe7\xad\x89\xe7\xba\xa7': {'\xe4\xb8\xad': '\xe5\x90\xa6', '\xe9\xab\x98': '\xe6\x98\xaf'}}}}, 'B': '\xe5\x90\xa6'}}
attributes = ['\xe5\xb9\xb4\xe9\xbe\x84', '\xe6\x80\xa7\xe5\x88\xab', '\xe6\x94\xb6\xe5\x85\xa5\xe7\xad\x89\xe7\xba\xa7', '\xe5\xa9\x9a\xe5\xa7\xbb\xe7\x8a\xb6\xe5\x86\xb5', '\xe6\x98\xaf\xe5\x90\xa6\xe4\xb9\xb0\xe6\x88\xbf']
count = 0
for entry in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.value)
		value = entry[index]
		if(value in tempDict.keys()):
			child = Node.Node(value, tempDict[value])
			result = tempDict[value]
			tempDict = tempDict[value]
		else:
			print "can't process input %s" % count
			result = "?"
			break
	print ("entry%s = %s" % (count, result))
