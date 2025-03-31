from bs4 import BeautifulSoup
import requests
import json 

def doencas_letra(letra):
    url = "https://www.atlasdasaude.pt/doencasaaz/" + letra
    print(url)
    response = requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    doencas = {}
    for div_row in soup.find_all("div", class_="views-row"):
        designacao = div_row.div.h3.a.text.strip()
        desc_div = div_row.find("div", class_="views-field-body")
        desc = desc_div.div.text
        doencas[designacao] = desc.strip().replace(" "," ")
    return doencas

res = {}
for a in range(ord("a"), ord("z") + 1):
    letra = chr(a)
    res = res | doencas_letra(letra)


f_out = open("doencas_.json", "w")

json.dump(res,f_out, indent=4, ensure_ascii=False)
f_out.close()
    


