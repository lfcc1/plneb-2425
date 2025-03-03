import re

file = open("../../data/dicionario_medico.txt", encoding="utf8")
texto = file.read()

#limpeza
texto = re.sub(r"\f","",texto)

#colocar marca
texto = re.sub(r"\n\n","\n\n@",texto)

# extrair conceitos
conceitos_texto = re.split(r"\n\n@",texto)

conceitos_list = []
for c in conceitos_texto:
    conceito_raw = re.split(r"\n", c, maxsplit=1)
    if len(conceito_raw) > 1:
        designacao, descricao = conceito_raw
        descricao = re.sub(r"\n"," ",descricao)
        conceitos_list.append((designacao,descricao))
    else:
        pass
        #FIXME

print(conceitos_list)
file.close()

