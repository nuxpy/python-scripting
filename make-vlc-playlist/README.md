### makevlcplaylist

Este _script_ permite generar fichero de una lista o _playlist_ para reproducir en el reproductor de medios **VLC**.

Escoge principal ficheros de tipo: **.mp3**, **.ogg** y **.wma**.

<a href="https://wiki.nuxpy.com/index.php/Generar_lista_musical">Referencia principal</a>

### Configuración

Luego de descargarse, como usuario **root** se puede copiar en una ruta de directorio donde cualquier usuario pueda usarlo:
```
    cp makevlcplaylist.py /usr/local/bin/makevlcplaylist
```

Posteriormente se le da permisos de ejecución:
```
    chmod 755 /usr/local/bin/makevlcplaylist
```

### Funcionamiento

Para usarse, se puede hacer de la siguiente manera:
```
    makevlcplaylist -t titulo_lista -d directorio\ 1 -d directorio\ 2
```

Posteriormente, se genera un fichero llamado: **titulo_lista.xspf**

Tener en cuenta que la lista se debe generar si se tiene un directorio especial de archivos musicales y el fichero de lista musical quedar en el fichero raíz de donde están guardados todos los directorios de música.

Si se mueve el fichero o directorio original de los ficheros musicales, entonces el fichero **.xspf** no tendría la relación o vinculación acorde a la ruta o _path_ original con el que se creó, pero el fichero **.xspf** sí se puede mover de lugar y tener en otro directorio diferente.

---
### Autor
Félix Urbina
