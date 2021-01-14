# Imports
import pandas as pd
from sqlalchemy import create_engine


# This CSV doesn't have a header so pass
# column names as an argument
columns = [
    'tipo_transicao',
    'documento',
    'empresa',
    'moeda',
    'valor_bruto',
    'valor_liquido',
    'taxa_adm',
    'adquirente',
    'bandeira',
    'parcela',
    'meio_captura',
    'filial',
]

# Load in the data
df = pd.read_csv(
    "VENDAS_CARTAO.csv",
    names=columns,
    index_col=False
)

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://postgres:6660@localhost:5432/postgres')
print(engine)

# Save the data from dataframe to
# postgres table "iris_dataset"
df.to_sql(
    'vendas_adquirente', 
    engine,
    index=False
)