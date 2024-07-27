
### Instalación de Odoo 15

#### 1. Instalar Python
Sigue la [documentación oficial de Odoo](https://www.odoo.com/documentation/15.0/administration/on_premise/source.html#python) para instalar Python en tu sistema.

#### 2. Crear un entorno virtual Python
Para mantener las dependencias de tu proyecto organizadas y separadas, es recomendable crear un entorno virtual.

```bash
# Navega al directorio de tu proyecto Odoo
cd /ruta/a/tu/proyecto/odoo_15

# Crea el entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Windows
.\venv\Scripts\activate

# En Unix o MacOS
source venv/bin/activate
```

#### 3. Instalar dependencias necesarias dentro del entorno virtual

Una vez que el entorno virtual esté activado, instala las dependencias requeridas usando `pip`.

```bash
pip install setuptools wheel
pip install -r requirements.txt
```

#### 4. Instalar PostgreSQL

Sigue la [documentación oficial de Odoo para PostgreSQL](https://www.odoo.com/documentation/15.0/administration/on_premise/source.html#postgresql) para instalar y configurar PostgreSQL.

#### 5. Ejecutar Odoo

Después de la instalación de PostgreSQL, puedes ejecutar Odoo utilizando el siguiente comando. Asegúrate de reemplazar `usuario`, `contraseña`, `nombreDB` y las rutas a los addons según tu configuración:

```bash
python odoo-bin -r usuario -w contraseña --addons-path=addons -d nombreDB -i base
```

#### 6. Acceder a Odoo

Una vez que Odoo esté en ejecución, puedes acceder a la interfaz web de Odoo en tu navegador usando la siguiente URL:

[http://localhost:8069/](http://localhost:8069/)

Las credenciales por defecto son:
- **Usuario:** `admin`
- **Contraseña:** `admin`

---

### Notas adicionales

- **Activación del entorno virtual**: Recuerda que debes activar el entorno virtual cada vez que empieces a trabajar en tu proyecto Odoo. En Windows, usa `.\venv\Scripts\activate` y en Unix o MacOS, usa `source venv/bin/activate`.

- **Archivos de configuración**: Asegúrate de configurar correctamente el archivo `odoo.conf` si es necesario. Este archivo suele contener información sobre rutas, bases de datos y otras configuraciones importantes.

- **Migración y actualización**: Si estás actualizando desde una versión anterior de Odoo, asegúrate de seguir los pasos de migración adecuados para evitar pérdida de datos o incompatibilidades.

Si necesitas más detalles o tienes alguna pregunta adicional, no dudes en pedir ayuda.

**Contacto:** brayanstivens@gmail.com

---

¡Buena suerte con tu instalación de Odoo 15!