### anotações ###

Um objeto *future* rodará uma corrotina.

Não é thread-safe.

Tasks são usadas para executar corrotinas no loop de eventos. Se a corrotina estiver aguardando (await) um *future*, a task suspende a execução da corrotina e espera o *future* ser completado. Quando o *future* termina, a execução da corrotina é retornada.

Loops de eventos usa agendamento cooperativo: um loop de evento roda um task de cada vez. Enquanto uma task aguarda (await) pela finalização do *future*, o loop de eventos executa outra task, callbacks ou operações IO.

Use a função de alto nivel (high-level) *asyncio.create_task()* para criar tasks, ou de baixo nivel (low-level) *loop.create_task()* ou *ensure_future()*.

Para cancelar uma task use o método *cancel()*. Chamando ele irá fazer com que a task retorne uma exceção *CancelledError* na corrotina atual. Se a corrotina estiver aguardando (awaiting) por um objeto *future* durante o cancelamento, o objeto *future* será cancelado.

*cancelled()* pode ser usado para verificar se uma task foi cancelada. O metodo retorna True, se a corrotina envolvida esta aguardando um *future* durante o cancelamento, o objeto deverá ser cancelado.
