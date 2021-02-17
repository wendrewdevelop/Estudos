### anotações ###

Espera pelo objeto awaitable completar no tempo limite.

Se *aw* for uma corrotina, automaticamente é marcada como uma task.

*Timeouts* pode receber *None* ou *float* ou *int* (numeros em segundos). Se o *timeout* for *None*, a proxima task só executará quando a anterior for finalizada.

Se o *timeout* ocorrer, ele cancela a task e retorna **asyncio.TimeoutError**

Para evitar cancelamento da task, use a função *shield()*.

A função vai esperar o objeto *future* estar cancelado, então o tempo total esperando pode exceder o *timeout*. Se uma exceção acontecer durante o cancelamento, a mesma é propagada.

Se a espera é cancelada, o *future aw* é cancelado também.

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
```

