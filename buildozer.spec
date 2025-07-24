[app]
# Básicos
title = PCmatplotlib
package.name = PCmatplotlib
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Inclusión de matplotlib y kivy_garden.matplotlib en requisitos
requirements = python3, kivy, matplotlib, kivy_garden.matplotlib

orientation = portrait

# Permisos para almacenamiento externo (si los necesitas)
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.private_storage = False

fullscreen = 1

# Arquitecturas Android soportadas
android.archs = arm64-v8a, armeabi-v7a

# Log level para más detalles de depuración
log_level = 2
warn_on_root = 1
