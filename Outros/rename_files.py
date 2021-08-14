import os


files = os.path.join('/home/wendrew/Documentos/Trabalho/Concil/Docs/icones-adqs/adquirentes-favicons/')
try:
    for f in os.listdir(files):
        r = f.replace(" ","")
        if r != f:
            os.rename(f'{files}{f}', f'{files}{r}')
    print('renamed!')
except Exception as error:
    print(error)
finally:
    print(os.listdir(files))