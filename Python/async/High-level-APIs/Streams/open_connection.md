### anotações ###

Cria uma conexão de rede e retorna par de objetos (reader, writer)

O *reader* e *writer* retornado são instancias das classes *StreamReader* e *StreamWriter*.

O argumento *loop* é opicional e pode sempre ser determinado automaticamente quando a função esta aguardando (awaited) uma corrotina.

O argumento *limit* determina o tamanho do buffer retornado por *StreamReader*. Por padrão o limite é definito por **64KiB**.

O restante dos argumentos são apssados diretamente para *loop.create_connection()*.

