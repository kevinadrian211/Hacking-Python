import os

def listar_archivos_sensibles(directorio):
    extensiones_sensibles = ('.db', '.sql', '.key', '.pem')
    archivos_sensibles = []

    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extensiones_sensibles):
                archivos_sensibles.append(os.path.join(raiz, archivo))
    
    return archivos_sensibles

directorio = '/ruta/al/directorio'
archivos = listar_archivos_sensibles(directorio)
for archivo in archivos:
    print(archivo)
