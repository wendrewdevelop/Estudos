import asyncio
import time
import os
import pathlib


default_directory = pathlib.Path(__file__).parent.absolute()

async def get_file_extension():
    """
        docstring
    """

    try:
        extension = ''
        lst = [os.path.splitext(x)[1] for x in str(default_directory)]
        my_final_list = dict.fromkeys(lst)
        for ext in list(my_final_list):
            extension += ext
        print(extension)
    except Exception as error:
        print(error)

    await asyncio.gather()


async def get_filenames():
    """
        Função que obtém o nome do 
        arquivo submetido.
        return:
            filename -> nome dos arquivos
            não processados
    """

    try:
        filename = ''
        lst = [os.path.splitext(x)[0] for x in str(default_directory)]
        my_final_list = dict.fromkeys(lst)
        for ext in list(my_final_list):
            filename += ext
        print(filename)
    except Exception as error:
        print(error)

    await asyncio.gather()


def main():
    """
        docstring
    """

    loop = asyncio.get_event_loop()
    task_function1 = asyncio.ensure_future(get_file_extension())
    task_function2 = asyncio.ensure_future(get_filenames())
    loop.run_forever()


if __name__ == '__main__':
    main()
    
    