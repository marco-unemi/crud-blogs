# CRUD de Blogs con Django, GitHub y Docker

## Descripción del proyecto

Este proyecto consiste en un sistema CRUD de blogs desarrollado con Django. El sistema permite registrar, visualizar, editar y eliminar publicaciones. Además, se aplican prácticas de gestión de configuración de software mediante GitHub y Docker.

## Objetivo

Aplicar conceptos de gestión de versiones, administración del cambio, gestión de entregas, gestión de código fuente, infraestructura como código y despliegue controlado utilizando GitHub y Docker.

## Tecnologías utilizadas

- Python
- Django
- GitHub
- Git
- Docker

## Ramas del repositorio

- `main`: contiene la versión estable del sistema.
- `develop`: contiene la versión de integración del equipo.
- `feature/dockerizacion`: contiene los cambios relacionados con Docker.

## Integrantes y roles

| Integrante | Rol |
|---|---|
| Marco David Arteaga Zambrano | Líder de proyecto / Backend |
| Diego Alejandro Neira Garcia | Frontend |
| Carlos Gabriel Carriel Macías | Operaciones / Despliegue |
| Victor Alejandro Celi Rivadeneira | Documentador |

## Ejecución local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver