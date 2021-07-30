#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
''' Este script genera tablas para Mediawiki según la tipología:
    * Tabla de lista simple.
    * Tabla lista de perfiles de usuarios.
    * Tabla lista de marcas comerciales.
'''
import os
import sys
import operator
import optparse

def profile(profile='', color={}):
    filelist_r = open(profile, 'r')
    filelist_w = open(r'tab_%s' % profile, 'w')
    header = '{|'
    footer = '|}'
    content = ''
    profile = {}
    profiles = []
    name = ''
    desc = ''
    col = 0
    if filelist_r:
        line = filelist_r.readline()
        content += header
        while line:
            l = line.split(';;')
            profile = {
                'web': l[0].strip(),
                'name': l[1].strip(),
                'desc': l[2].strip()
            }
            profiles.append(profile)
            line = filelist_r.readline()
        filelist_r.close()
        lprofiles = len(profiles)
        l = 1
        for p in sorted(profiles, key=operator.itemgetter("name")):
            col += 1
            name += '\n|style="padding: 2px 5px 5px 5px;width:100px;text-align:left;"|[[Archivo:icon_profile_24px.png]] [%s %s]' % (p['web'] or '', p['name'] or '')
            desc += '\n|style="padding: 2px 5px 15px 5px;width:200px;vertical-align:top;margin-right:20px;"|%s' % p['desc'] or ''
            if col == 4 or l == lprofiles:
                name += '\n|-'
                desc += '\n|-'
                content += name
                content += desc
                name = ''
                desc = ''
                col = 0
            l += 1
        content += '\n%s' % footer
        filelist_w.write(content)
        filelist_w.close()
    else:
        print ("Debe ingresar un archivo con datos para generar tabla Mediawiki")
    return True

def trademark(trademark='', color={}):
    filelist_r = open(trademark, 'r')
    filelist_w = open(r'tab_%s' % trademark, 'w')
    header = '{|'
    footer = '|}'
    content = ''
    mark = {}
    marks = []
    icon = ''
    web = ''
    name = ''
    desc = ''
    col = 0
    if filelist_r:
        line = filelist_r.readline()
        content += header
        while line:
            l = line.split(';;')
            mark = {
                'icon': l[0].strip(),
                'web': l[1].strip(),
                'name': l[2].strip(),
                'desc': l[3].strip()
            }
            marks.append(mark)
            line = filelist_r.readline()
        filelist_r.close()
        lmarks = len(marks)
        l = 1
        for p in sorted(marks, key=operator.itemgetter("name")):
            col += 1
            icon += '\n|style="padding: 2px 5px 5px 5px;width:100px;text-align:center;"|[[Archivo:%s]]' % p['icon']
            web += '\n|style="padding: 2px 5px 5px 5px;width:100px;text-align:center;"|[%s %s]' % (p['web'] or '', p['name'] or '')
            desc += '\n|style="padding: 2px 15px 15px 15px;width:200px;vertical-align:top;margin: 0 10px 0 10px;text-align:center;"|%s' % p['desc'] or ''
            if col == 4 or l == lmarks:
                icon += '\n|-'
                web += '\n|-'
                desc += '\n|-'
                content += icon
                content += web
                content += desc
                icon = ''
                name = ''
                web = ''
                desc = ''
                col = 0
            l += 1
        content += '\n%s' % footer
        filelist_w.write(content)
        filelist_w.close()
    else:
        print ("Debe ingresar un archivo con datos para generar tabla Mediawiki")
    return True

def category(trademark='', color={}):
    filelist_r = open(trademark, 'r')
    filelist_w = open(r'tab_%s' % trademark, 'w')
    header = '{|'
    footer = '|}'
    content = ''
    mark = {}
    marks = []
    icon = ''
    web = ''
    name = ''
    desc = ''
    col = 0
    if filelist_r:
        line = filelist_r.readline()
        content += header
        while line:
            l = line.split(';;')
            mark = {
                'icon': l[0].strip(),
                'web': l[1].strip(),
                'name': l[2].strip(),
                'desc': l[3].strip()
            }
            marks.append(mark)
            line = filelist_r.readline()
        filelist_r.close()
        lmarks = len(marks)
        l = 1
        for p in sorted(marks, key=operator.itemgetter("name")):
            col += 1
            if p['icon']:
                icon += '\n|style="padding: 2px 5px 5px 5px;width:100px;text-align:center;"|[[Archivo:%s]]' % p['icon']
            web += '\n|style="padding: 2px 5px 5px 5px;width:100px;text-align:center;"|[[:Category:%s|%s]]' % (p['web'] or '', p['name'] or '')
            desc += '\n|style="padding: 2px 5px 15px 5px;width:200px;vertical-align:top;margin-right:20px;"|%s' % p['desc'] or ''
            if col == 4 or l == lmarks:
                icon += '\n|-'
                web += '\n|-'
                desc += '\n|-'
                content += icon
                content += web
                content += desc
                icon = ''
                name = ''
                web = ''
                desc = ''
                col = 0
            l += 1
        content += '\n%s' % footer
        filelist_w.write(content)
        filelist_w.close()
    else:
        print ("Debe ingresar un archivo con datos para generar tabla Mediawiki de categorías")
    return True


def tablist(simplelist='', color={}):
    filelist_r = open(simplelist, 'r')
    filelist_w = open(r'tab_%s' % simplelist, 'w')
    header = '{|style="text-align:left; background-color:%s; width:auto;"' % color['bgtabcolor']
    footer = '|}'
    initab = False
    content = ''
    ll = 0
    th = """!style="background-image: linear-gradient(%s, %s 60%%, %s); padding:5px 5px 5px 5px; color:%s"|""" % (color['bggradHmin'], color['bggradHmed'], color['bggradHhig'], color['fontheader'])
    tr = ''
    if filelist_r:
        line = filelist_r.readline()
        content += header
        while line:
            l = line.split(';;')
            if initab == False:
                initab = True
                for c in l:
                    content += '\n%s%s' % (th, c)
            else:
                if ll % 2 == 0:
                    tr = '|style="background-color:%s;padding: 3px 5px 3px 5px;"|' % color['bgrowitem1']
                else:
                    tr = '|style="background-color:%s;padding: 3px 5px 3px 5px;"|' % color['bgrowitem2']
                for c in l:
                    content += '\n%s%s' % (tr, c)
            content += '|-'
            ll += 1
            line = filelist_r.readline()
        content += '\n%s' % footer
        filelist_r.close()
        filelist_w.write(content)
        filelist_w.close()
    else:
        print ("Debe ingresar un archivo con datos para generar tabla Mediawiki")
    return True

def main():
    ''' ##################   Variables globales   ###################
        * Estas variables DEBEN SER PERSONALES según los colores que se desean usar.
    '''
    color = {
        'fontheader': '#FFFFFF',    # Color de texto de cabecera
        'bgtabcolor': '#F9F9F9',    # Color de fondo de la tabla
        'bggradHmin': '#F86003',    # Color tono bajo de cabecera de tabla
        'bggradHmed': '#E34E0D',    # Color tono medio de cabecera de tabla
        'bggradHhig': '#DD4812',    # Color tono intenso de cabecera de tabla
        'bgrowitem1': '#F9F9F9',    # Color 1 de línea de tabla
        'bgrowitem2': '#E5E6E6'     # color 2 de línea de tabla
    }
    ''' ############################################################ '''
    opts = sys.argv[1:]
    app = optparse.OptionParser()
    app.add_option('-l', '--list', default=False, dest='list', type="string", nargs=1, help="Make a simple list from a source file.")
    app.add_option('-p', '--profile', default=False, dest='profile', type="string", nargs=1, help="Make a simple profile list from a source file.")
    app.add_option('-t', '--trademark', default=False, dest='trademark', type="string", nargs=1, help="Make a simple trademark list from a source file.")
    app.add_option('-c', '--categ', default=False, dest='categ', type="string", nargs=1, help="Make a simple category list from a source file.")
    options, args = app.parse_args()
    if options.list:
        tablist(options.list, color)
    elif options.profile:
        profile(options.profile, color)
    elif options.trademark:
        trademark(options.trademark, color)
    elif options.categ:
        category(options.categ, color)
    else:
        print ("Debe seleccionar una opción:\n")
        print ("\twikitablecreate -l fichero_tabla_de_lista\n")
        print ("\twikitablecreate -p fichero_tabla_de_perfiles\n")
        print ("\twikitablecreate -t fichero_tabla_de_marcas_comerciales\n")
        print ("\twikitablecreate -c fichero_tabla_de_categorias\n")
    return True

if __name__ == '__main__':
    main()
