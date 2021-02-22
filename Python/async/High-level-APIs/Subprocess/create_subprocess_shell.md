### anotações ###

Executa um comando *cmd shell*.

O argumento *limit* organiza o buffer para a classe *StreamReader* envolvida para *proccess.stdout* e *proccess.stderr*.

Retorna uma instancia do processo.


<b>Importante:</b> É a responsabilidade dessa aplicação garantir que todos os espaços em branco (whitespace) e caracteres especiais serão citados apropriadamente para evitar **shell injection**. O *shlex.quote()* pode ser usado.