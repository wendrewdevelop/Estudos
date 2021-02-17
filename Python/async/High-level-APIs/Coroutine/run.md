### anotações ###

Executa a corrotina e retorna o resultado.

o *run()* executa a função referenciada, tomando cuidado com o loop de eventos, finalizando os geradores assíncronos e fechando as threads.

Essa função não pode ser chamada enquanto outro loop assíncrono esteja executando na mesma thread.

Se o *debug* for *True* o loop de eventos executará em modo de debug.

Essa função sempre criará um loop de eventos e o fechará no final. 

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())
```

