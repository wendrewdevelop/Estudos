### anotações ###

Envolve a corrotina dentro de uma *task* e agenda a sua execução.

A task é executado no loop retornado por **get_running_loop()**, um *Runtime Error* é retornado se não houver loops executando na thread.

Essa função foi adicionado na versão 3.7 do python e funciona a partir dessa versão. Caso queira uma solução generica use a função **asyncio.ensure_future()**

```python
async def coro():
    ...

# In Python 3.7+
task = asyncio.create_task(coro())
...

# This works in all Python versions but is less readable
task = asyncio.ensure_future(coro())
...
```