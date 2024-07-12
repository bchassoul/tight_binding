# Uso

Esta sección proporciona información sobre cómo utilizar los scripts proporcionados.

## tight_binding.py

Este script implementa el modelo de Tight Binding de manera serial.

```python
{% include "../tight_binding.py" %}
```
## tight_binding_parallel.py

Este script implementa el modelo de Tight Binding de manera paralela utilizando multiprocessing.

```python
{% include "../tight_binding_parallel.py" %}
```

Después de clonar el repositorio, puedes ejecutar los scripts de la siguiente manera:

```shell
python tight_binding.py
python tight_binding_parallel.py --cores 4
```