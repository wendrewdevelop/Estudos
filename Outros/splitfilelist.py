files = [
    'teste.csv',
    'teste.txt',
    'teste.xlsx'
]

for index, f in enumerate(files):
    ext = f.split('.')[1]
    print(f'Index: {index}')
    print(f'File: {f}') # f['filename'].split('.')[1]
    print(f'Extensão: {ext}')