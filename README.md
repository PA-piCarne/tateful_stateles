# Stateful + Stateless con Django

Esta aplicación demuestra dos comportamientos en un mismo sistema:

## 1) Parte stateful (con estado)

- Ruta de entrada: `/` (redirige a `/login/`).
- Registro de usuarios: `/register/`.
- Rutas principales: `/login/` y `/dashboard/`.
- Usa autenticación de Django con sesión (`sessionid`).
- Flujo:
  1. El usuario se registra en `/register/` (si no tiene cuenta).
  2. Inicia sesión en `/login/`.
  3. Si las credenciales son válidas, Django crea sesión.
  4. El usuario entra a `/dashboard/` y ve: `Bienvenido [usuario]`.

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

## Diseño

- La interfaz (login, registro y dashboard) está centrada en pantalla.
- Estilo simple y no tan profesional, como pediste.

## Ejecutar

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Migrar base de datos:
   ```bash
   python manage.py migrate
   ```
3. Correr servidor:
   ```bash
   python manage.py runserver
   ```

> Nota: si escribes `python mange.py sunserver` dará error por typo.
> El comando correcto es: `python manage.py runserver`.
