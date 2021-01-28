import csv


def read_file(filename: str) -> str:
    """
        lendo os dados do arquivo
    """

    try:
        with open('batch.csv') as file:
            read_file = csv.reader(file)
        return read_file
    except Exception as error:
        print(error)
    
    
if __name__ == "__main__":
    read_file('batch.csv')