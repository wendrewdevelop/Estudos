import pandas as pd
import requests
import io
import json


def request_core_file_origin(url: str, client_id: str):

    session = requests.session()

    r = session.get(
        url, 
        # auth=(f'104480526', '9335ba372597413da2ac9d4827e07671'), 
        auth=(f'{client_id}', '9335ba372597413da2ac9d4827e07671'),
        # params = {'pageNumber': page}
        stream=True
    )

    return r


if __name__ == "__main__":
    x = []
    for request_date in pd.date_range(start='2021-04-07', end='2021-04-07'):
        data_movimento = request_date.strftime('%Y-%m-%d')
        response = request_core_file_origin(
            url=f'https://api.r2tec.com/edi/v1/2.00/movimentos?dataMovimento={data_movimento}&tipoMovimento=1',                        
            client_id='89980232'
        )
        unparsed = json.loads(response.text)
        for process in unparsed['detalhes']:
            df = pd.DataFrame.from_dict([process])
            x.append(df)
            # df.to_csv('teste.csv', index=True)
            new = pd.concat(x, ignore_index=True)
            new.to_csv('teste.csv')
            response.close() # Fechando sessão da requisição
