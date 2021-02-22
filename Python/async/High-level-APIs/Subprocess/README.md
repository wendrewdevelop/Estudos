### Referencias ###

https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-subprocess

### Anotações ###

- Essa sessão descreve a API de alto nivel (high-level async/await) cria e gerencia sub-processos.

Segue um exemplo de como o asyncio roda um comando shell e obtém o resultado:

```python
[In]

import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))
```

```python
[Out]

['ls /zzz' exited with 1]
[stderr]
ls: /zzz: No such file or directory
```

Porque todos as funções de sub-processo asyncio são assíncronas e o asyncio provê varias ferramentas, tornando facil a execução e monitoramento de multiplos processos em paralelo.

```python
async def main():
    await asyncio.gather(
        run('ls /zzz'),
        run('sleep 1; echo "hello"'))

asyncio.run(main())
```

### constants ###

<b>PIPE:</b> Pode ser passado para os parametros *stdin*, *stdout* ou *stderr*.

Se o *PIPE* for passado para o argumento *stdin*, o atributo *Process.stdin* irá apontar para uma instancia *StreamWriter*.

Se o *PIPE* for passado para os argumentos *stdout* ou *stderr*, o processo *Process.stdout* e *Process.stderr* irão apontar para a instancia *StreamReader*.

<b>STDOUT:</b> Um valor especial que pode ser usado como o argumento *stderr* e indicar um erro padrão que deve ser redirecionado a uma saida padrão.

<b>DEVNULL:</b> Um valor especial que pode ser usado como *stdin*, *stdout* ou *stderr* para processsar a criação de funções. Indica que o arquivo especial *os.devnull* será usado para o fluxo de subprocessos correspondentes.

### Interagindo com sub-processos ###

Ambas as funções *create_subprocess_exec()* e *create_subprocess_shell()* retorna uma instancia da classe **Process**. A classe **Process** é um codigo de alto nivel (high-level) que permite a comunicação com subprocessos e visualização da conclusão.

<b>Process:</b> Um objeto que envolve os processos do S.O criado por *create_subprocess_exec()* e *create_subprocess_shell()*.

Essa classe foi designada para ter um função similiar a API do *subprocess.Popen* , mas com algumas diferenças notaveis:

- Diferente do *Popen*, a instancia *Process* não tem algo equivalente ao método *Poll()*;

- Os métodos *communicate()* e *wait()* não tem o parametro timeout: use a função *wait_for()*;

- O método *Process.wait()* é assíncrono, enquanto o método *subprocess.Popen.wait()* é implementado como um bloco de loop;

- O parametro *universal_newlines* não é suportado.

Essa classe não é *thread-safe*.

<b>wait:</b> Aguarda o processo filho finalizar.

Organiza e retorna o atributo *returncode*.

<b>communicate:<b> Interage com o processe:

1. Envia dados para *stdin* (se o input não for None);
2. Lê os dados do *stdout* e *stderr*, quando o EOF é alcançado;
3. Espera o processo terminar.

O argumento *input* (opicional) é um  objeto de dados (bytes) que serão enviados para o processo filho.

Retorna uma tupla (stdout_data, stderr_data).

Se cada vez que uma exceção *BrokenPipeError* ou *ConnectionResetError* é gerada, quando o *input* esta escrevendo dentro do *stdin*, a exceção é ignorada. Essa condição ocorre quando o processo sai antes de todos os dados serem escritos.

Se ela for destinada a enviar dados para o processo *stdin*, o processo precisa estar criado com *stdin=PIPE*. Igualmente, para obter qualquer outro resultado na tupla, o processo será criado com os argumentos *stdout=PIPE* e/ou *stderr=PIPE*.


<b>send_signal:</b> Envia um sinal para o processo filho.

<b>terminate:</b> Para o processo filho.

No POSIX esse método envia um *signal.SIGTERM* para o processo filho.

No Windows a função TerminateProcess() da API Win32 é chamada para parar o processo filho.

<b>kill:</b> Mata o processo filho.

No POSIX esse método envia um sinal *SIGKILL* para o processo filho.

No Windows esse método é um "apelido" (alias) para a função *terminate()*.

<b>stdin:</b> Input padrão do StreamWriter. Se o processo estiver criado como *stdin=None* retornará None.

<b>stdout:</b> Saida padrão do StreamReader, se o processo estiver criado como *stdout=None* retornará None.

<b>stderr:</b> Erro padrão do StreamReader, se o processo for criado com *stderr=None*, retornará None.

<b>pid:</b> Numero de identificação do processo.

<b>returncode:</b> Retorna o codigo do processo se ele existir.

None é retornado se o processo não foi finalizado.

Um valor negativo (-N) indica que o processo filho foi encerrado por um sinal (POSIX only).