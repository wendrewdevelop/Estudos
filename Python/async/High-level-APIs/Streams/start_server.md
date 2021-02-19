### anotações ###

Inicia um socket.

O callback *client_connection_cb* é chamado sempre que uma nova conexão de client é estabelecida.

O argumento *loop* é opicional e pode ser chamado automaticamente sempre que um método esta aguardando uma corrotina.

*limit* determina o tamanho do buffer retornado por *StreamReader*. Por padrão o tamanho é **64KiB**.

O resto dos argumentos são passados diretamente para *loop.create_server()*.