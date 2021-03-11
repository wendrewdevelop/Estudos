import json
from pandas.io.json import json_normalize
import pandas as pd


header = [
    "cnpjManager",
    "nameManager",
    "cnpjCostumer",
    "nameCostumer",
    "orderUuid",
    "externalTransactionIdentifier",
    "typeFile",
    "createdAt",
    "totalAmountInCents",
    "transactionUuid",
    "paymentUuid",
    "status",
    "updatedAt",
    "paymentMethod",
    "operationType",
    "grossAmountInCents",
    "takeRateunit",
    "takeRate",
    "takeRateAmountInCents",
    "takeRateUnitGateway",
    "takeRateGateway",
    "takeRateAmountInCentsGateway",
    "netAmountInCents",
    "releaseInstallment",
    "numberOfInstallments",
    "releaseTime",
    "scheduledFor",
]
f = open(r'vendas.json')
data = json.load(f)
f.close()

df = pd.json_normalize(
   data['data'], 
   record_path=['orders', 'transactions'], 
  
   errors='ignore'
)
df.to_csv('teste.csv', index=False, sep=',')

    
    