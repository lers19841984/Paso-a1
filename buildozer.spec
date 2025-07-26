[app]
title = PCmatplotlib
package.name = PCmatplotlib
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Incluir todas las dependencias necesarias
requirements = python3, kivy, numpy, matplotlib, pyparsing, kiwisolver, cycler, kivy_garden.matplotlib

orientation = portrait
fullscreen = 1

# Permisos Android
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.private_storage = False

# Arquitecturas Android soportadas
android.archs = arm64-v8a, armeabi-v7a

# Para compatibilidad con matplotlib
android.enable_androidx = 1
android.gradle_dependencies = androidx.appcompat:appcompat:1.2.0