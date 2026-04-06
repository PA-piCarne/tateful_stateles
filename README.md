# Stateful + Stateless con Django

Esta aplicación demuestra dos comportamientos en un mismo sistema:

## 1) Parte stateful (con estado)

- Ruta: `/login/` y `/dashboard/`
- Usa autenticación de Django con sesión (`sessionid`).
- Flujo:
  1. El usuario inicia sesión en `/login/`.
  2. Si las credenciales son válidas, Django crea sesión.
  3. El usuario entra a `/dashboard/` y ve: `Bienvenido [usuario]`.

## 2) Parte stateless (sin estado)

- Endpoint: `/api/products/`
- No requiere login ni sesión.
- Devuelve JSON en cada request de forma independiente.

Respuesta ejemplo:

```json
[
  {"name": "Laptop", "price": 1200},
  {"name": "Mouse", "price": 25}
]
```

## Ejecutar

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Migrar base de datos:
   ```bash
   python manage.py migrate
   ```
3. Crear usuario admin/prueba:
   ```bash
   python manage.py createsuperuser
   ```
4. Correr servidor:
   ```bash
   python manage.py runserver
   ```
