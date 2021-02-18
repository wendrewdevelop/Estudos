### Referencias ###

https://docs.python.org/3/library/asyncio-queue.html#asyncio-queues


### anotações ###

FIFO (First in, first out).

Se o *maxsize* é menor ou igual a zero, o tamanho da queue é infinito. Se for um inteiro maior que zero, então aguarda o bloco *put()* atingir o *maxsize* até que um item seja removido por *get()*.

Diferente da *queue* padrão da lib de threading, o tamanho da fila sempre conhecido e pode ser retornado chamando pelo método *qsize()*.

Essa classe não é Thread-Safe.

<b>LIFO Queue:</b> Uma variante da classe *Queue*que recupera as entradas adicionadas mais recentemente (last in, first out)

<b>Exceptions - QueueEmpty:</b> Essa exceção é retornada quando a função *get_nowait()* é chamada numa fila vazia.

<b>Exceptions - QueueFull:</b> A exceção retorna quando a função *put_nowait()* é chamada em uma fila sem espaço.

<b>Examplos</b>

- Filas podem ser usadas para distribuir cargas de trabalho (workload) entre tarefas (tasks) severas.

```python
import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())
```