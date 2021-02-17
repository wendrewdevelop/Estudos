### anotações ###

Rodando *awaitables* simultaneamente e bloqueie até a condição especificada por um return_when.

Retorna um conjunto de *Tasks/Futures* (done, pending)

Uso:
<code>done, pending = await asyncio.wait(aws)</code>

Um *Timeout* (float ou int), se especificado, pode ser usado para controlar o maximo de numeros de segundos de espera antes de retornar.

Repare que essa função não retorna um **asyncio.TimeoutError**. *Futures* e *Tasks* não são realizados caso ocorra um *timeout* são simplesmente retornados no segundo conjunto.

*return_when* indica quando a função deve retornar. Deve ser uma das seguintes constantes:

<table class="docutils align-default">
    <colgroup>
        <col style="width: 42%">
        <col style="width: 58%">
    </colgroup>
    <thead>
        <tr class="row-odd">
            <th class="head"><p>Constante</p></th>
            <th class="head"><p>Descrição</p></th>
        </tr>
    </thead>
    <tbody>
        <tr class="row-even">
            <td>
                <p>
                    <code class="xref py py-const docutils literal notranslate">
                        <span class="pre">FIRST_COMPLETED</span>
                    </code>
                </p>
            </td>
            <td>
                <p>A função deve retornar quando algum *future* é finalizado ou cancelado.</p>
            </td>
        </tr>
        <tr class="row-odd">
            <td>
                <p>
                    <code class="xref py py-const docutils literal notranslate">
                        <span class="pre">FIRST_EXCEPTION</span>
                    </code>
                </p>
            </td>
            <td>
                <p>
                    A função deve retornar quando algum *future* finaliza ou gera uma exceção. Se não gerar exceção, o mesmo será equivalente a constante
                    <code class="xref py py-const docutils literal notranslate">
                        <span class="pre">ALL_COMPLETED</span>
                    </code>.
                </p>
            </td>
        </tr>
        <tr class="row-even">
            <td>
                <p>
                    <code class="xref py py-const docutils literal notranslate">
                        <span class="pre">ALL_COMPLETED</span>
                    </code>
                </p>
            </td>
            <td>
                <p>A função irá retornar quando todas as *futures* forem finalizadas ou canceladas.</p>
            </td>
        </tr>
    </tbody>
</table>

Diferente da função *wait_for()*, a função *wait()* não cancelará a *future* quando um *timeout* ocorrer.

```python
'''
    wait() agenda corrotinas como uma task automaticamente e depois retorna ela implicitamente como um objeto no conjunto (done, pending).
'''

async def foo():
    return 42

coro = foo()
done, pending = await asyncio.wait({coro})

if coro in done:
    # This branch will never be run!


'''
    Veja como o snippet acima pode ser corrigido:
'''

async def foo():
    return 42

task = asyncio.create_task(foo())
done, pending = await asyncio.wait({task})

if task in done:
    # Everything will work as expected now.
```



