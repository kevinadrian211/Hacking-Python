import os
import shutil

def crear_backup_archivos_importantes(directorio_origen, directorio_backup, extension='.log'):
    if not os.path.exists(directorio_backup):
        os.makedirs(directorio_backup)
    
    for raiz, _, archivos in os.walk(directorio_origen):
        for archivo in archivos:
            if archivo.endswith(extension):
                archivo_origen = os.path.join(raiz, archivo)
                archivo_destino = os.path.join(directorio_backup, os.path.relpath(archivo_origen, directorio_origen))
                directorio_destino = os.path.dirname(archivo_destino)
                
                if not os.path.exists(directorio_destino):
                    os.makedirs(directorio_destino)
                
                shutil.copy2(archivo_origen, archivo_destino)

directorio_origen = '/ruta/al/directorio'
directorio_backup = '/ruta/al/directorio_de_backup'
crear_backup_archivos_importantes(directorio_origen, directorio_backup)