import re
from dbfread import DBF
from checker import ean_validation

file = r"c:\users\matheus\desktop\produtos.dbf"

dbf_produtcts = DBF(file, encoding="cp437", load=True)

index = 0

wrong_ean = []


for record in dbf_produtcts:

    ean = dbf_produtcts.records[index]["CODFAB"]
    ean = re.sub(u"[':!# ]", ' ', ean)
    ean = ean.strip()

    ean_bar = dbf_produtcts.records[index]["CODBARRA"]
    ean_bar = re.sub(u"[':!# ]", ' ', ean)
    ean_bar = ean.strip()

    product = dbf_produtcts.records[index]["DESCRICAO"]

    code = dbf_produtcts.records[index]["CODIGO"]

    if len(ean) == 12 and ean.isnumeric():
        if ean != ean_validation(ean):
            info = f"{code:6}||{product:40}||{ean:13}||{ean_validation(ean):13}"
            wrong_ean.append(info)

    if len(ean_bar) == 12 and ean_bar.isnumeric():
        if ean_bar != ean_validation(ean_bar):
            info = f"{code:6}||{product:40}||{ean_bar:13}||{ean_validation(ean_bar):13}"
            wrong_ean.append(info)

    if len(ean) == 13 and ean.isnumeric():
        if ean != ean_validation(ean):
            info = f"{code:6}||{product:40}||{ean:13}||{ean_validation(ean):13}"
            wrong_ean.append(info)

    if len(ean_bar) == 13 and ean_bar.isnumeric():
        if ean_bar != ean_validation(ean_bar):
            info = f"{code:6}||{product:40}||{ean_bar:13}||{ean_validation(ean_bar):13}"
            wrong_ean.append(info)

    index += 1

    wrong_ean = list(set(wrong_ean))

with open(r"c:\users\matheus\desktop\ean.txt", "w") as file:
    file.write("CODIGO||             PRODUTO                    ||  Incorreto  ||   Correto  \n")
    file.write("==============================================================================\n")
    for item in wrong_ean:
        file.write(f"{item}\n")
