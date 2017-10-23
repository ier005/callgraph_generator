#!/usr/bin/python
#coding=utf-8

import r2pipe
import json
import numpy as np

def collectFuncs(js):
    funcs = []
    for j in js:
        if j['name'] not in funcs:
            funcs.append(j['name'])
    return funcs

def findIndex(f, js):
    for i in range(len(js)):
        if js[i]['name'] == f:
            return i

def generateMat(js):
    funcs = collectFuncs(js)
    l = len(funcs)
    mat = np.zeros((l, l))
    for i in range(l):
        ind1 = findIndex(funcs[i], js)
        fs = js[ind1]['imports']
        for f in fs:
            ind2 = findIndex(f, js)
            mat[ind1][ind2] = 1
    return (funcs, mat)

def anaCg(filename):
    proj = r2pipe.open(filename)
    proj.cmd('aa')
    cgj = proj.cmd('agCj')
    proj.quit()
    
    j = json.loads(cgj)
    return generateMat(j)



if __name__ == '__main__':
    res = anaCg('a1.exe')
    print res[0]
    print res[1]
