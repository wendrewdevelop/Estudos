### anotações ###

Retorna o resultado da task

Se a task foi finalizada, o resultado da corrotina envolvida é retornado (ou uma exceção).

Se a task for cancelada com sucesso, esse metodo gera uma exceção *CancelledError*.

Se a o resultado da task ainda não estiver disponivel, o metodo retorna uma exceção *InvalidStateError*

