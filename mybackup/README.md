### mybackup

Script para crear respaldos o backup de bases de datos _MySQL_.

<a href="https://wiki.nuxpy.com/index.php/Respaldar_bases_de_datos_MySQL_con_python">Información general del <i>script</i></a>

### Contenido

Está compuesto por dos ficheros, uno de configuración: **mybackup.conf**; donde se guardan las instancias y bases de datos que se desean respaldar.

El segundo fichero es el script ejecutable para realizar los respectivos procesos de respaldo o limpieza de históricos. Se puede copiar en una ruta donde pueda ejecutarse desde cualquier ruta del sistema operativo.

El fichero de configuración pudiera copiarse en el propio directorio de configuraciones de _MySQL_.

### Funcionamiento

Funcionamiento básico:

* Crear respaldo:

```
    ./mybackup.py -d mybackup.conf
```

* Limpiar histórico de respaldos:

```
    ./mybackup.py -c mybackup.conf
```

Autor
-----
Félix Urbina
