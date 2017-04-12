#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

if __name__ == '__main__':
	raw_txt = open('vectors.txt')
	raw_txt = raw_txt.read()
	raw_txt = raw_txt.split('\n')
	raw_txt = [x.split() for x in raw_txt]
	raw_txt.pop()

	name = []
	vectors =[]

	for element in raw_txt:
		name.append(element[0])
		vector = element[1:]
		vector = [float(x) for x in vector]
		vectors.append(vector)

	hash_map = dict()
	for index in range(len(name)):
		hash_map.update({name[index]:vectors[index]})

	print(hash_map['they'])