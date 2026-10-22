# Publicar FluxTime en PyPI

Este repositorio está configurado para construir distribuciones de Python y publicarlas en PyPI mediante GitHub Actions y **Trusted Publishing**. El paquete se llama `fluxtime-clock`; el comando instalado es `fluxtime`.

## 1. Preparar las cuentas

1. Crea/verifica tu cuenta en [PyPI](https://pypi.org/account/register/) y activa la verificación en dos pasos si está disponible.
2. Inicia sesión en PyPI y abre [Publishing](https://pypi.org/manage/account/publishing/).
3. Añade un **pending publisher** con estos datos:
   - PyPI project name: `fluxtime-clock`
   - Owner: `programador777lolxddd-dot`
   - Repository name: `FluxTime`
   - Workflow name: `publish-pypi.yml`
   - Environment name: `pypi`
4. En GitHub, abre **Settings → Environments** del repositorio y crea un entorno llamado `pypi`. Configura protección/aprobación manual para la publicación si está disponible.

Trusted Publishing evita guardar un token de PyPI como secreto en el repositorio. La primera publicación con el pending publisher puede crear el proyecto en PyPI.

## 2. Probar el paquete localmente (opcional, recomendado)

Con Python 3.8 o posterior:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

Instala el paquete localmente para comprobar el comando:

```bash
python -m pip install .
fluxtime
```

En Windows, utiliza `py` en lugar de `python` si ese es el lanzador configurado en tu sistema.

## 3. Publicar la primera versión

1. Confirma que el nombre `fluxtime-clock` está disponible en PyPI y que la metadata es correcta.
2. Actualiza la versión `0.1.0` en `pyproject.toml` si necesitas otra versión. PyPI no permite reutilizar una versión ya publicada.
3. Crea y publica un **GitHub Release** con una etiqueta como `v0.1.0`.
4. GitHub Actions construirá los archivos y ejecutará el flujo de publicación a PyPI. Revisa la ejecución en la pestaña **Actions**.

También se puede iniciar el workflow manualmente desde **Actions**, pero la publicación real requiere que Trusted Publishing esté configurado correctamente.

## 4. Instalar después de publicar

```bash
python -m pip install fluxtime-clock
fluxtime
```

Para actualizar:

```bash
python -m pip install --upgrade fluxtime-clock
```

## Notas

- FluxTime usa la biblioteca estándar de Python y no declara dependencias de ejecución externas.
- El proyecto es una aplicación de terminal; en Windows, ejecútala desde PowerShell, CMD o Windows Terminal.
- La publicación no se realiza automáticamente al añadir estos archivos: debes configurar PyPI y crear el release inicial.
- Guía oficial: [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/) y [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
