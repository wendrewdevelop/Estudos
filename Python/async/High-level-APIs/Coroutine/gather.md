### anotações ###

Roda os *objetos awaitables* em uma sequencia aws concorrente.

se houver alguma corrotina, ela é automaticamente agendada como task.

se todos os objetos awaitables estão completos, o resultado é uma lista agregada de valores retornados. A ordem dos valores corresponde a ordem dos objetos na aws.

se o termo *return_exceptions* for *False* (padrão), A primeira exceção gerada é imediatamento propagada para a task no *gather()*. Outros awaitables na sequencia não serão cancelados e continuarão a rodar.

se o termo *return_exceptions* for *True*, as exceções são tratados como um retorno bem sucedido e agregado a lista de resultados.

se *gather()* for cancelado, todos os objetos submetidos (que não foram completados) são cancelados.

se alguma *task* ou *future* de uma sequencia for cancelada, as mesmas são tratadas como uma exceção **CancelledError**. a chamada do *gather()* não é cancelada nesse caso, isso é feito para prevenir cancelamentos de uma *task/future* feita para cancelar outras *tasks/futures*.

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24
```