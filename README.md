# SIGETP desktop
Versión para crear una aplicación portable del proyecto SIGETP usando pyinstaller

# 1 Crear Ejecutable

   - ~$ pyinstaller --name=sigetp --additional-hooks-dir=hooks manage.py

# 2 Ejecutar Ejecutable

   - ~$ ./sigetp runserver

# Notas

   - Antes de realizar el paso 1, es recomendable ejecutar el servidor y hacer todas las migraciones y creación de usuarios
     porque hacerlo con el ejecutable siempre da problemas. Para seguir con el paso 2 es bueno ya tener todo listo

   - Por alguna razon pyinstaller no copia todos los archivos cuando crea el ejecutable, debido a esto hay que copiar manualmente
     las carpetas de templates y templatetags de las respectivas app que tenga el proyecto, así como tambien la carpeta static

   - En la carpeta build se encuentra el ejecutable para windows

   - En la carpeta dist se encuentra el ejecutable para linux

   - Para generar el ejecutable en x86 o x64, se debe compilar en la respectiva distribución

   - Esto usa el mismo entorno virtual que usa __SIGETP__
