import json
import csv


f = open(r'vendas.json')
data = json.load(f)
f.close()
with open("output.csv", mode="w", newline='') as out:
    w = csv.writer(out)
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
    w.writerow(header)
    for asset in data["data"]:
        data_point = data["data"]
        orders_point = data_point['orders'][0]
        transactions_point = orders_point['transactions'][0]
        output = [data_point["cnpjManager"]]
        output.append(data_point["nameManager"])
        output.append(data_point["cnpjCustomer"])
        output.append(data_point["nameCustomer"])
        output.append(orders_point['orderUuid'])
        output.append(orders_point["externalTransactionIdentifier"])
        output.append(orders_point["typeFile"])
        output.append(orders_point["createdAt"])
        output.append(orders_point["totalAmountInCents"])
        output.append(transactions_point['transactionUuid'])
        output.append(transactions_point['paymentUuid'])
        output.append(transactions_point['status'])
        output.append(transactions_point['updatedAt'])
        output.append(transactions_point['paymentMethod'])
        output.append(transactions_point['operationType'])
        output.append(transactions_point['grossAmountInCents'])
        output.append(transactions_point['takeRateunit'])
        output.append(transactions_point['takeRate'])
        output.append(transactions_point['takeRateAmountInCents'])
        output.append(transactions_point['takeRateUnitGateway'])
        output.append(transactions_point['takeRateGateway'])
        output.append(transactions_point['takeRateAmountInCentsGateway'])
        output.append(transactions_point['netAmountInCents'])
        output.append(transactions_point['releaseInstallment'])
        output.append(transactions_point['numberOfInstallments'])
        output.append(transactions_point['releaseTime'])
        output.append(transactions_point['scheduledFor'])
        
        w.writerow(output)