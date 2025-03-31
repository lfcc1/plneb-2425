from bs4 import BeautifulSoup
import requests
import json 

response = requests.get("https://www.atlasdasaude.pt/doencasAaZ")

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

doencas = {}
for div_row in soup.find_all("div", class_="views-row"):
    designacao = div_row.div.h3.a.text.strip()
    desc_div = div_row.find("div", class_="views-field-body")
    desc = desc_div.div.text
    #if desc_div.div.p:
    #    desc = desc_div.div.p.text
    #elif desc_div.div.div:
    #    desc = desc_div.div.div.text
    doencas[designacao] = desc.strip().replace(" "," ")

f_out = open("doencas.json", "w")

json.dump(doencas,f_out, indent=4, ensure_ascii=False)
f_out.close()
    


