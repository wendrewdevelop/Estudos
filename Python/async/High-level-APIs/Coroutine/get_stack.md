### anotações ###

Retorna uma lista de stacks frames para essa task.

Se a corrotina envolvida não esta finalizada, o metodo era retornar a stack que esta suspensa. Se a corrotina foi completada com sucesso ou cancelada, o metodo retornará uma lista vazia. Se a corrotina foi finalizada com uma exceção, o metodo retornará uma lista de traceback.

Os frames são sempre organizados do mais velho ao mais novo.

Apenas uma stack frame é retornada para cada corrotina suspendida.

O argumento *limit* é opicional, responsavel por setar o maximo de numeros de frames que será retornado. Por padrão todos os frames disponiveis são retornados. A ordem dessa lista depende de como a stack ou o traceback é retornado.