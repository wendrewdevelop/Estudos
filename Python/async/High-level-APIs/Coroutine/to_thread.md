### anotações ###


Assíncronamente executa uma função em uma thread separada.

Qualquer argumento (*args, **kwargs) fornecido para essa função são diretamente passadas para *func*. Então, o contexto atual *contextvars.Context* é propagado, habilitando as variaveis de contexto do loop de eventos da thread para serem acessados em threads separadas.

Retorna uma corrotina que pode ser awaited (esperada) para obter um eventual retorno de *func*.

Essa corrotina é primeiramente interpretada para ser usada como execução **IO-bound functions/methods** que, de outra forma, bloquearia o loop de eventos se eles fossem executados no thread principal.

```python
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54
```