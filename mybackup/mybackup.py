# -*- coding: utf-8 -*-
import os
import sys
import re
import json
import zipfile
from os import walk
import logging
from datetime import *
_logger = logging.getLogger(__name__)

def db_dump(db, args, bdir):
    date_today = date.today()
    #cmd_my_dump = 'C:/"Program Files"/MySQL/"MySQL Server"/bin/mysqldump.exe'      # Ejemplo para Windows
    cmd_my_dump = '/usr/bin/mysqldump'                                              # Ejemplo para Linux
    cmd_my_dump += " --host=%s --port=%s --user=%s --password=%s --databases %s " % (args['host'], args['port'], args['user'], args['passwd'], db)
    cmd_my_dump += " > %s/%s_%s.sql" % (bdir, db, date_today)
    try:
        os.system(cmd_my_dump)
    except:
        print ('No se realizó respaldo de base de datos: %s' % db)
    return True

def clean_dir(bdir, days, dayrestore):
    date_today = date.today()
    for path, dname, fname in os.walk(bdir):
        for f in fname:
            get_date = ''
            if re.match(r'.*.zip', f, re.I) and not re.match(r'.*\d{4}-\d{2}-%s.zip' % dayrestore, f, re.I):
                get_date = f.split('.')[0][-10:]
                date_issue = datetime.strptime(get_date, '%Y-%m-%d').date()
                result = str(date_today.__sub__(date_issue)).split(' ')[0]
                if result != '0:00:00':
                    result_raw = int(result)
                    if result_raw >= days:
                        os.remove('%s/%s' % (path, f))
    return True

def compress_files(bdir):
    date_today = date.today()
    for path, dname, fname in os.walk(bdir):
        len_path = len(path) + 1
        if os.path.isfile("%s/fullbackup_1_%s.zip" % (path, date_today)):
            fzip = "%s/fullbackup_2_%s.zip" % (path, date_today)
        else:
            fzip = "%s/fullbackup_1_%s.zip" % (path, date_today)
        with zipfile.ZipFile(fzip, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as myzip:
            for f in fname:
                if re.match(r'.*.sql$', f, re.I):
                    fsql = os.path.join(path, f)
                    myzip.write(fsql, fsql[len_path:])
                    os.remove(fsql)
    return True

def main():
    ''' Declaración y validación de variables para sistema operativo
    '''
    date_today = date.today()
    year = str(date_today.year)
    month = str(date_today.month).zfill(2)
    mysql_config = sys.argv[2] or []
    opt = sys.argv[:] or []
    if os.path.isfile(mysql_config):
        ''' Leer archivo y cargar variables de entorno e información de instancias
        '''
        fconf_r = open(mysql_config, 'r')
        line = fconf_r.readline()
        content = ''
        while len(line):
            l = line.strip()
            line = fconf_r.readline()
            content += l.replace("'",'"')
        gvals = json.loads(content)
        fconf_r.close()
        ''' Verificar que existe el directorio principal de respaldos
        '''
        backup_dir = gvals['backup_dir']
        if not os.path.exists(backup_dir):
            os.mkdir(backup_dir, mode=0o775)
        if '-d' in opt:
            ''' Función para realizar respaldo
            '''
            for i in gvals['instances']:
                backuphost = '%s/%s' % (backup_dir, i['host'])
                backupinst = '%s/%s' % (backuphost, i['instancia'].replace(' ','').strip())
                backupinst_year = '%s/%s' % (backupinst, year)
                backupinst_month = '%s/%s' % (backupinst_year, month)
                bdir = backupinst_month
                ''' Verificar que existen los directorios de copia
                '''
                if not os.path.exists(backuphost):
                    os.mkdir(backuphost, mode=0o755)
                if not os.path.exists(backupinst):
                    os.mkdir(backupinst, mode=0o755)
                if not os.path.exists(backupinst_year):
                    os.mkdir(backupinst_year, mode=0o755)
                if not os.path.exists(backupinst_month):
                    os.mkdir(backupinst_month, mode=0o755)
                ''' Recorrer y respaldar cada instancia con sus bases de datos
                '''
                for db in i['db']:
                    db_dump(db, i, bdir)
                compress_files(bdir)
        elif '-c' in opt:
            ''' Función para realizar limpieza de históricos
            '''
            clean_dir(backup_dir, gvals['days_clean'], gvals['day_restore'])
        else:
            print ("""Ingrese un argumento válido:\n
 mysql_backup -d\t\tRespaldar, hacer dump de todas las bases de datos.
 mysql_backup -c\t\tLimpiar o borrar archivos con más de 15 días de antiguedad.\n""")
    else:
        print ("""No existe el archivo: mysql_backup.conf\nGenere el archivo correspondiante para el usuario en cuestión.
Sino, ingrese como usuario postgres para usar las funciones de este comando.""")

if __name__ == '__main__':
    main()
