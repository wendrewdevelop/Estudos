### anotações ###

Mostra todos os itens que foram recebidos e processador corretamente.

A contagem de tasks não finalizada sobe sempre que um item é adicionado à fila. A contagem desce sempre que uma corrotina chama *task_done()* para indicar que o item foi recuperado e o todo o trabalho dele foi completado. quando a contagem de itens não finalizados chega a zero, a função *join()* ocorre.