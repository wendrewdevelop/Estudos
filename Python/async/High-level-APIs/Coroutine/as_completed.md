### Anotações ###

Retorna um iterador da corrotina. Cada corrotina retornada pode ser esperada (awaited) para obter mais rapidamente o proximo resultado do iterador dos objetos remanescentes.

Retorna **asyncio.TimeoutError** se o *timeout* ocorrer antes de todas as *futures* finalizarem.

```python
for coro in as_completed(aws):
    earliest_result = await coro
    # ...
```

