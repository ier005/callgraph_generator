#!/usr/bin/python
#coding=utf-8

import r2pipe
import json

funcs = [u'entry0']

def collectFuncs(l, js):
    global funcs
    for j in js:
        if j['name'] == l:
            for s in j['imports']:
                if s not in funcs:
                    funcs.append(s)
                    collectFuncs(s, js)

proj = r2pipe.open('a1.exe')
proj.cmd('aa')
cgj = proj.cmd('agCj')
proj.quit()


j = json.loads(cgj)

collectFuncs('entry0', j)
print funcs
