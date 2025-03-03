import re
import json 

file = open("../../data/dicionario_medico.xml", encoding="utf8")
texto = file.read()
file.close()

#limpar
texto = re.sub(r"</?page.*>", "", texto)
#texto = re.sub(r"</page>", "", texto)
texto = re.sub(r"</?text.*?>","", texto)

#extrair
conceitos = re.findall(r"<b>(.*)</b>\n([^<]*)", texto)

def limpa_descricao(desc):
    desc = desc.strip()
    desc = re.sub(r"\n"," ",desc)
    return desc

#conceitos_dict = {designacao : limpa_descricao(descricao) for designacao, descricao in conceitos}
conceitos_dict = {}
for designacao, descricao in conceitos:
    if designacao in conceitos_dict:
        conceitos_dict[designacao] += " @ " + limpa_descricao(descricao)
    else:
        conceitos_dict[designacao] = limpa_descricao(descricao) 


file_out = open("conceitos.json","w", encoding="utf8")

json.dump(conceitos_dict,file_out, ensure_ascii=False, indent= 4)
file_out.close()

#print(conceitos_dict)







