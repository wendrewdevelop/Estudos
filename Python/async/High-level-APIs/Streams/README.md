### Referencias ###

https://docs.python.org/3/library/asyncio-stream.html#asyncio-streams


### anotações ###

Streams são codigos assíncronos de alto nivel (high-level async/await-ready) para trabalhar com conexões de rede. Streams possibilita envios e recebimentos de dados sem usar callbacks ou protocolos de baixo nivel (low-level).

```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
```

### StreamReader ###

Representa o objeto de leitura que possibilida a API ler os dados da stream IO.

Não é recomendado instanciar *StreamReader* diretamente, use o *open_connection()* e *start_server()*.

<b>read:</b> Lê *n* bytes. Se *n* não for provido ou setado como -1, leia então EOF e retorne todos os bytes.

**EOF** -> End-of-file.

<b>readline:</b> Lê uma linha, sendo "linha" a sequencia de bytes terminando com *\n* (final da linha). 

Se EOF é recebido, mas *\n* não é encontrado, o metodo retorno parcialmente a leitura.

Se EOF é recebido e o buffer esta vazio, então retornará um objeto de bytes vazio.

<b>readexactly:</b> Lê um numero exato de bytes.

Retorna a exceção *IncompleteReadError* se o EOF for atingido antes do *n* ser lido.

Use a exceção *IncompleteReadError.partial* para obter a leitura parcial dos dados.

<b>readuntil:</b> Lê os dados da conexão onde o *separador* for encontrado.

Se bem sucessedido, o dado e o separador será remover do buffer (consumido). O separador será incluido no dado retornado no final.

Se o montante de dados lidos exceder o limite configurado na stream (conexão), a exceção *LimitOverrumError* é retornado, e o dado é deixado no buffer para ser lido novamente.

O EOF é chamado depois que o separador é encontrado, uma exceção *IncompleteReadError* é chamada, e o buffer é resetado. A exceção *IncompleteReadError.partial* contem uma porção do separador.

<b>at_eof:</b> Retorna *True* se o buffer estaiver vazio e o método *feed)eof()* é chamado.

### StreamWriter ###

Representa um objeto de escrita que possibilita que a API escreva dados IO.

Não é recomendado instanciar diretamente o *StreamWriter*, ao inves disso use *open_connection()* e o *start_server()*.

<b>write:</b> Esse método tenta escrever os dados para o socket subjacente imediatamente. Se ele falhar, o dado é colocado em fila (queued) em um buffer de escrita até que possa ser enviado.

O metodo deve ser usado junto com o método *drain()*

```
stream.write(data) 
await stream.drain()
```

<b>writelines:</b> O metodo escreve uma lista (ou qualquer iterador) de bytes no socket subjacente. Se falhar, o dado é colocado em fila no buffer de escrita até conseguir ser enviado.

O método deve ser usado juntamente com o método *drain()*

```
stream.writelines(data) 
await stream.drain()
```

<b>close:</b> O metodo fecha a stream e a camada de socket subjacente.

Esse método deve ser usado juntamente com o método *wait_closed()*

```
stream.close()
await stream.wait_closed()
```

<b>can_write_eof:</b> Retorna *True* se a camada subjancete de transporte suporta o método *write_eof()*, caso contrario retornará *False*.

<b>write_eof:</b> Fecha a escrita depois que o fluxo de dados de gravação no buffer estiverem finalizados.

<b>transport:</b> Retorna a camada subjacente assincrona de transporte.

<b>get_extra_info:</b> Obtém detalhes da camada de transporte.

<b>drain:</b> Espera até que a escrita possa ser feita.

```
writer.write(data)
await writer.drain()
```

Esse controle de fluxo interage com a camada subjacente IO do buffer de escrita. Quando o tamanho do buffer excede, o método espera até que o buffer tenha esvaziado e a escrita possa continuar. Quando não há nada para esperar, o método *drain()* retorna imediatamente.

<b>is_closing:</b> Retorna *True* se a conexão estiver fechada ou está no processo de fechamento.

<b>wait_closed:</b> Espera até que a conexão seja fechada.

Deve ser usado juntamente com o método *close()* para esperar até que a camada de conexão esteja fechada.

### Exemplos ###

- TCP mostrando os clients que estão usando a conexão

```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('Hello World!'))
```

- TCP mostrando os servers que estão usando a conexão

```python
import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
```

- Obtendo os headers (cabeçalhos) HTTP

```python
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')

    # Ignore the body, close the socket
    writer.close()

url = sys.argv[1]
asyncio.run(print_http_headers(url))
```

Modo de usar -> ``` python example.py http://example.com/path/page.html ```


- Registre um socket aberto para esperar por dados, usando streams.

```python
import socket

async def wait_for_data():
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets.
    rsock, wsock = socket.socketpair()

    # Register the open socket to wait for data.
    reader, writer = await asyncio.open_connection(sock=rsock)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    # Wait for data
    data = await reader.read(100)

    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()

    # Close the second socket
    wsock.close()

asyncio.run(wait_for_data())
```