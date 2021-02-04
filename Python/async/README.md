## Tópicos ##

- A programação assincrona multiplas requisições podem ser feitas simultaneamente de forma *concorrente* ou em *paralelo*;

**Paralelismo:** é onde as tarefas são executadas exatamente ao mesmo tempo, por meio de threads (gerenciamento de *cores*);
**Concorrencia:** é um conjunto de tarefas executando de forma sumultânea, sendo concluidas de forma pacial, até que tudo esteja finalizado.

- Corrotinas (em ingles, Corroutines) realizam mudança de contextos, mas essa mudança é feita por meio da ocorrencia de uma espera e não por uma interrupção;

- O loop de eventos é responsavel por gerenciar a concorrência e a execução das tarefas;

- Tarefas são, tecnicamente, chamadas de corrotinas, quando são executadas, elas retornam *awaitable objects*;

**awaitable objects:** São objetos que estão na espera, que podem ser retornados em forma de Task ou corrotina. Esses objetos ficam disponiveis para a aplicação no momento em que são criados, mas o resultado deles só estão disponiveis no futuro (Objetos dos tipo future).



## Referencias ##

https://medium.com/@edytarcio/async-await-introdu%C3%A7%C3%A3o-%C3%A0-programa%C3%A7%C3%A3o-ass%C3%ADncrona-em-python-fa30d077018e