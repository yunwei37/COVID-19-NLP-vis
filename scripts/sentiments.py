# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os

def getsentimentslist(lines):
    sentimentslist = []
    for i in lines:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments-0.5)
    return sentimentslist
