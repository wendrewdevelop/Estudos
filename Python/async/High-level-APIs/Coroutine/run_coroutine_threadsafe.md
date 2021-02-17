### anotações ###

Envia um corrotina para o loop de eventos fornecidos. 

Thread safe.

Retorna uma *concurrent.futures.Future* para esperar (wait) o resultado de outro OS thread.

Essa função deve ser chamada a partir de uma thread de um sistema operacional diferente daquele em que o loop de eventos esta sendo executado.

```python
# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
```

Se uma exceção for gerada na corrotina, o *Future* retornado será notificado. Isso pode ser usado para cancelar a task no loop de eventos.

```python
try:
    result = future.result(timeout)
except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')
```