### anotações ###

Indica que uma tarefa enfileirada anteriormente foi finalizada.

Usada por consumidores de filas. Para cada *get()* usada na task, a chamada subsequente será *task_done()* diz para a fila se o processo da task foi finalizado.

Se o *join()* esta atualmente bloqueado, ele será retomado quando todos os itens forem processados (significando que uma chamada *task_done()* foi recebida para cada item que foi *put()* na fila).

Retorna *ValueError* se for chamado mais vezes do que há de itens na fila.