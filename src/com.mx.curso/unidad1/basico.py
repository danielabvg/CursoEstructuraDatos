##Guía práctica: Flujo completo de Git en un proyecto de Estructura de Datos

#Incluye:
#- Crear y cambiar ramas
#- Agregar código y subirlo
#- Significado de colores en VS Code
#- Errores comunes
#- Cómo verificar tus cambios en GitHub

# ------------------------------------------------------------------
# 1. Verificar el estado actual del repositorio
# ------------------------------------------------------------------
# Muestra en qué rama estás y si hay cambios pendientes por guardar.
print("git status -> muestra el estado actual del repositorio")

# ------------------------------------------------------------------
# 2. Crear una nueva rama y cambiarse a ella
# ------------------------------------------------------------------
# git checkout -b <nombre_rama> -> crea y mueve a la nueva rama
print("git checkout -b development/unidad1 -> crea y mueve a la rama 'development/unidad1'")

# ------------------------------------------------------------------
# 3. Cambiar a una rama existente
# ------------------------------------------------------------------
# Si la rama ya existe, solo necesitas:
print("git checkout development/unidad1 -> cambia a la rama 'development/unidad1'")

# ------------------------------------------------------------------
# 4. Ver las ramas existentes
# ------------------------------------------------------------------
# git branch -> lista las ramas locales, la actual aparece con '*'
print("git branch -> muestra todas las ramas locales y cuál estás usando")

# ------------------------------------------------------------------
# 5. Agregar cambios de un archivo al staging
# ------------------------------------------------------------------
# Después de modificar un archivo:
print("git add src/com.mx.curso/unidad1/basico.py -> agrega cambios al área de preparación")

# ------------------------------------------------------------------
# 6. Crear un commit con mensaje descriptivo
# ------------------------------------------------------------------
print('git commit -m "Agregué el código a basico.py" -> guarda los cambios en la historia local de Git')

# ------------------------------------------------------------------
# 7. Subir los cambios a GitHub
# ------------------------------------------------------------------
print("git push origin development/unidad1 -> sube los cambios de la rama al remoto")

# ------------------------------------------------------------------
# 8. Ver tus cambios en GitHub
# ------------------------------------------------------------------
# 1. Ir a tu repositorio en GitHub: https://github.com/danielabvg/EstructuraDatos
# 2. Cambiar a la rama correcta usando el menú desplegable que por defecto dice 'main'.
# 3. Seleccionar: development/unidad1
# 4. Navegar a src/com.mx.curso/unidad1/basico.py para ver tu código actualizado
print("En GitHub, cambia a la rama 'development/unidad1' y revisa tu archivo basico.py")

# ------------------------------------------------------------------
# 9. Colores de Git en VS Code
# ------------------------------------------------------------------
# U (verde)    = Untracked (archivo nuevo, Git no lo sigue todavía)
# M (amarillo) = Modified (archivo modificado, aún no agregado)
# A (verde)    = Added (archivo agregado y listo para commit)
# M (azul)     = Modificado y agregado (listo para commit)
print("VS Code: M amarilla = modificado, falta 'git add'")

# ------------------------------------------------------------------
# 10. Cómo actualizar un archivo ya existente
# ------------------------------------------------------------------
# Pasos:
# 1. Guardar el archivo modificado
# 2. git status -> confirmar que aparece como 'modified'
# 3. git add <archivo>
# 4. git commit -m "mensaje descriptivo"
# 5. git push origin <rama>
print("Para actualizar un archivo en GitHub: git add -> git commit -> git push")

# ------------------------------------------------------------------
# 11. Errores comunes
# ------------------------------------------------------------------
# "fatal: a branch named 'development/unidad1' already exists"
# -> Solución: git checkout development/unidad1
#
# "dquote>" (comillas abiertas)
# -> Solución: cerrar comillas o Ctrl+C
#
# "nothing to commit, working tree clean"
# -> Significa que no hay cambios nuevos que guardar
print("Mensajes comunes: revisa si hay cambios pendientes o si ya todo está en Git")
