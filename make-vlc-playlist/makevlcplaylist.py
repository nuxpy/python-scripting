#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import os
import sys
import re
import optparse

def content():
    body = '''\n        <track>
            <location><![CDATA[file://%s/%s]]></location>
            <extension application="http://www.videolan.org/vlc/playlist/0"><vlc:id>%s</vlc:id></extension>
        </track>'''
    lst = '''<vlc:item tid="%s"/>'''
    head = '''<?xml version="1.0" encoding="UTF-8"?>
<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">
    <title>%s</title>
    <trackList>'''
    foot = '''\n    </trackList>
    <extension application="http://www.videolan.org/vlc/playlist/0">
        %s
    </extension>
</playlist>'''
    content = {
        'body': '%s' % body,
        'head': '%s' % head,
        'list': '%s' % lst,
        'foot': '%s' % foot
    }
    return content

def main(opts):
    file_title = '%s.xspf' % opts.title.lower().replace(' ','_').replace('.','_')
    lista_xml = open(file_title, 'w')
    count = 0
    lista = ''
    cont = content['head'] % opts.title
    for d in opts.dirs:
        for path, dname, fname in os.walk(d):
            for f in fname:
                if re.match(r'(.*.ogg|.*.mp3|.*.wma)', f, re.I):
                    cont += content['body'] % (os.path.abspath(path), f, count)
                    lista += content['list'] % count
                    count += 1
    cont += content['foot'] % lista
    lista_xml.write(cont)
    lista_xml.close()
    return True

if __name__ == '__main__':
    opt = sys.argv[1:]
    opts = optparse.OptionParser()
    opts.add_option('-t', '--title', default=False, dest='title', type="string", nargs=1, help="Title of list.")
    opts.add_option('-d', default=[], dest='dirs', type="string", action="append", help="Directories.")
    options, args = opts.parse_args()
    if options.title and options.dirs:
        content = content()
        main(options)
    else:
        print ("There is no title.")

