# WebApp - Aplicación Web con Flask

Una aplicación web moderna desarrollada con Flask que incluye:

- ✅ **Registro de usuarios** con validaciones en tiempo real
- 🍞 **Navegación de migas de pan** (breadcrumbs)
- ⚠️ **Manejo robusto de excepciones**
- 🎨 **Diseño moderno y distintivo**
- 🔐 **Sistema de autenticación**

## Características Principales

### 1. Validaciones en Tiempo Real

El formulario de registro incluye validaciones exhaustivas:

- **Nombre de usuario**: Solo letras (sin espacios ni números)
- **Correo electrónico**: Debe contener @ y terminar en .com
- **Contraseña**: 
  - Mínimo 8 caracteres
  - Al menos una mayúscula
  - Al menos una minúscula
  - Al menos un número
- **Indicador de fortaleza** de contraseña visual
- **Confirmación de contraseña** con validación de coincidencia
- **Aceptación de términos** obligatoria

### 2. Navegación de Migas de Pan

Todas las páginas incluyen una barra de navegación contextual que muestra:
- Ruta actual en la aplicación
- Enlaces a páginas anteriores
- Resaltado de la página actual

### 3. Manejo de Excepciones

Sistema completo de captura de errores:
- Página personalizada para errores 404
- Página personalizada para errores 500
- Captura general de excepciones
- Botón para simular errores y ver el manejo

### 4. Páginas Incluidas

- **Inicio**: Landing page con características
- **Registro**: Formulario con validaciones en tiempo real
- **Login**: Autenticación de usuarios
- **Dashboard**: Panel de control (requiere login)
- **Perfil**: Información del usuario
- **Configuración**: Ajustes de cuenta
- **Error**: Página de manejo de excepciones

## Requisitos

- Python 3.7+
- Flask

## Instalación

1. **Clonar o descargar el proyecto**

2. **Crear un entorno virtual (recomendado)**

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install flask
```

## Ejecución

1. **Ejecutar la aplicación**

```bash
python app.py
```

2. **Abrir en el navegador**

Visita: `http://localhost:5000`

## Estructura del Proyecto

```
webapp/
│
├── app.py                      # Aplicación principal Flask
│
├── templates/                  # Plantillas HTML
│   ├── base.html              # Plantilla base
│   ├── index.html             # Página de inicio
│   ├── registro.html          # Formulario de registro
│   ├── login.html             # Formulario de login
│   ├── dashboard.html         # Panel de control
│   ├── perfil.html            # Perfil de usuario
│   ├── configuracion.html     # Configuración
│   └── error.html             # Página de errores
│
├── static/                     # Archivos estáticos
│   ├── css/
│   │   └── style.css          # Estilos CSS
│   └── js/
│       ├── main.js            # JavaScript principal
│       └── validaciones.js    # Validaciones del formulario
│
└── README.md                   # Este archivo
```

## Uso de la Aplicación

### 1. Registro de Usuario

1. Ve a la página de **Registro**
2. Completa el formulario:
   - **Nombre**: Solo letras (ejemplo: `juanperez`)
   - **Correo**: Formato válido con @ y .com (ejemplo: `juan@ejemplo.com`)
   - **Contraseña**: Cumplir requisitos de seguridad
   - **Confirmar contraseña**: Debe coincidir
   - **Aceptar términos**: Obligatorio
3. El botón se habilitará automáticamente cuando todos los campos sean válidos
4. Haz clic en **Crear cuenta**

### 2. Iniciar Sesión

1. Ve a la página de **Login**
2. Ingresa tu correo y contraseña
3. Serás redirigido al Dashboard

### 3. Probar el Manejo de Errores

- Ve a la página de inicio
- Haz clic en **"Simular un error"** en la sección de demostración
- Verás la página de error personalizada con opciones de navegación

### 4. Navegar por la Aplicación

- Usa la barra de navegación superior
- Las **migas de pan** te mostrarán tu ubicación actual
- El resaltado indica la página activa

## Características del Diseño

### Sistema de Colores

- **Primario**: Rojo coral (#ff6b6b)
- **Secundario**: Turquesa (#4ecdc4)
- **Terciario**: Amarillo (#ffd93d)
- **Éxito**: Verde (#6bcf7f)
- **Advertencia**: Naranja (#ffb347)

### Tipografía

- **Títulos**: Unbounded (bold, display)
- **Cuerpo**: DM Sans (legible, moderna)

### Animaciones

- Entrada suave de elementos
- Hover effects en tarjetas
- Transiciones fluidas
- Indicadores de estado animados

## Seguridad

⚠️ **Nota**: Esta es una aplicación de demostración. Para producción:

1. Usa una clave secreta segura y única
2. Implementa hash de contraseñas (bcrypt, argon2)
3. Usa HTTPS
4. Implementa CSRF protection
5. Valida datos en el servidor
6. Usa una base de datos real (PostgreSQL, MySQL)
7. Implementa rate limiting
8. Añade logging apropiado

## Personalización

### Cambiar Colores

Edita las variables CSS en `/static/css/style.css`:

```css
:root {
    --color-primary: #ff6b6b;
    --color-secondary: #4ecdc4;
    /* ... más colores ... */
}
```

### Modificar Validaciones

Edita las funciones en `/static/js/validaciones.js`:

```javascript
// Ejemplo: cambiar requisitos de contraseña
const longitudMinima = valor.length >= 10; // Cambiar de 8 a 10
```

### Añadir Nuevas Páginas

1. Crea una nueva ruta en `app.py`
2. Crea la plantilla HTML correspondiente
3. Actualiza las migas de pan (breadcrumbs)

## Problemas Comunes

### El servidor no inicia

- Verifica que Flask esté instalado: `pip list | grep Flask`
- Verifica que el puerto 5000 esté disponible

### Las validaciones no funcionan

- Verifica que el archivo JavaScript esté cargando
- Abre la consola del navegador para ver errores
- Verifica que los IDs de los elementos HTML coincidan

### Los estilos no se aplican

- Limpia la caché del navegador (Ctrl+Shift+R)
- Verifica la ruta del archivo CSS en `base.html`

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Fuentes**: Google Fonts (Unbounded, DM Sans)
- **Diseño**: CSS Grid, Flexbox, Animaciones CSS

## Próximas Mejoras

- [ ] Implementar base de datos real
- [ ] Añadir recuperación de contraseña
- [ ] Sistema de roles y permisos
- [ ] API REST
- [ ] Tests automatizados
- [ ] Modo oscuro
- [ ] Internacionalización (i18n)

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Contacto

Para preguntas o sugerencias, no dudes en contactar.

---

**¡Disfruta usando WebApp! 🚀**
