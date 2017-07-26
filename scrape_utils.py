# coding: utf-8
!/usr/bin/env python3

import html

def html_remove(text):
    for ent,repla in html.entities.html5.items():
        if ent in text:
            text=text.replace('&'+ent+';', repla)
    return text.replace('&#39;', "'")

import string
def remove_punct(word, _punkts=string.punctuation):
    return "".join(c for c in word if c not in _punkts)

from bs4 import BeautifulSoup
def remove_html(_text):
    return BeautifulSoup(_text, "lxml").text

class NameStemmer:
	def __init__(self):
		self.redundant_suffixes = ['Group', 'International','plc', "Ltd", "AG", "Limited", "Ltd", "Inc"]
		_replacements = {'Pharmaceutical':'(Ph|F)arma', 
		              'Biopharmaceutical':'Biopharma',
		              'Therapeutic':'Therap',
		              'Corporation':'Corp',
                'Technologie':'Techno',
                'Technology':'Techno',
                'Lab':'Lab',
                'Laboratorie':'Lab',
                'Laboratory':"Lab"}
		_patterns = {}
		import re
		for k,v in _replacements.items():
			_patterns[re.compile('.*?\\b'+k+'(s|\.)?'+'\\b.*?', re.I|re.U)]=v
		self.patterns = _patterns
		self.split_regex = re.compile(r'\W+')
	def stem(self, companyname):
		name = companyname
		name = name.split(",")[0].strip()
		name = name.split("(")[0].strip()
		name_arr = self.split_regex.split(name)
		for i in range(len(name_arr)):
			for pat,v in self.patterns.items():
				if pat.match(name_arr[i]):
						name_arr[i]=pat.sub(v, name_arr[i])
		print name_arr
		return "\\W+".join(filter(lambda st:len(st.strip())>0, name_arr))
