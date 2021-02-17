### Referencias ###

https://docs.python.org/3/library/asyncio-task.html#coroutine


### Anotações ###

Para executar uma corrotina, temos os três meios principais a seguir:

- Usando o método *asyncio.run()*;
- Criando "esperas" na função, fazendo com que o codigo execute um trecho de cada vez;

```python
[In]

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

```python
[Out]

started at 17:13:52
hello
world   
finished at 17:13:55
```
- Utilizando o método *asyncio.create_task()* criaremos corrotinas concorrentes.


```python
[In]

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```

```python
[Out]

started at 17:14:32
hello
world
finished at 17:14:34
```