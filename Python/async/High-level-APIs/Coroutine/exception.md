### anotações ###

Retorna a exceção da task.

Se a corrotina envolvida gerar um exceção, essa exceção é retornada. Se a corrotina retornar normalmente seu resultado, esse metodo ira retornar None.

Se a task for cancelada com sucesso, o metodo retornará a exceção *CancelledError*.

Se o resultado da task ainda não estiver disponivel, esse metodo retornará a exceção *InvalidStateError*.