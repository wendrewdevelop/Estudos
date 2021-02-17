### anotações ###

Um *Future* é um objeto especial **low-level** que representa um **eventual resultado** de uma operação assíncrona.

Quando um objeto future esta *aguardando* quer dizer que a corrotina será finalizada mais tarde em outro lugar.

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

Um bom exemplo de objeto *Future* é o **loop.run_in_executor()**