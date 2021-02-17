### anotações ###

Dizemos que um objeto é um **awaitable**, quando antecedemos o mesmo com o termo *await*;

- O tres principais tipos de objetos awaitables, são:
    - Coroutines;
    - Tasks;
    - Futures.

1. Coroutines

Corrotinas são objetos awaitables, portanto podem ser "aguardados" por outras corrotinas.

```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```

**Importante:** Na documentação, o termo corrotina se refere exclusicamente a dois conceitos:
- *uma função corrotina:* uma função **async def**;
- *um objeto corrotina:* Um objeto retornado por uma *função corrotina*.

2. Tasks

Tasks são usadas para agendar corrotinas concorrentemente.

Quando uma função esta envolvida com uma função com tasks, como *asyncio.create_task()* a corrotina é agendada automaticamente para rodar em seguida.

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```

