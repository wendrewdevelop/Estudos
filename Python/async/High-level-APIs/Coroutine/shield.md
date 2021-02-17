### anotações ###

Previne que um objeto seja cancelado.

sintaxe: <code>res = await shield(something())</code>

A tarefa em execução não será cancelada, do ponto de vista da função o cancelamento nunca aconteceu. Embora o seu chamador ainda esteja cancelado, a expressão "await" gera um **CancelledError**.

Se a função é concelada por outros meios, isso também cancelará o *shield()*.

Se desejar ignorar completamente o cancelamento (não recomendado), a função shield() deve ser combina com uma clausula try/except:

```python
try:
    res = await shield(something())
except CancelledError:
    res = None
```