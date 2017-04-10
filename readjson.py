import json
from pprint import pprint
import numpy as np
import os
import common

#extract text from JSON file "fileJ", then split 2 sentences with space
def ParseJsonText(fileJ):
	json_file = np.loadtxt(fileJ, delimiter='\n', dtype=str)
	text=''
	for i in range(len(json_file)):
		if(len(json_file[i])==0 or json_file[i][len(json_file[i])-1] != '}'):
			continue
		json_parsed = json.loads(json_file[i])
		text+=' '+json_parsed['text']
	return text

#extract all the text in a directory ("TopDir") of JSON files, then split 2 sentences with space
def ParseHpv(TopDir):
	dir1=os.listdir(TopDir)
	dir1.sort()
	TextTotal=''
	for i in range(len(dir1)):
		print('processing...'+str(i))
		dir2=os.listdir(TopDir+dir1[i])
		TextTotal+=' '+ParseJsonText(TopDir+dir1[i]+'/'+dir2[0])
	return TextTotal

#extract all the JSON files in directory "hpvtest" and sanitize it so that it could be appropriate for word2vec model training
if __name__ == '__main__':	
	txt = ParseHpv('./hpvtest/')
	txt = common.sanitize_text(txt)

	RawText = open('rawtext.txt','w+')
	RawText.write(txt)
	RawText.flush()
