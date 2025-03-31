from bs4 import BeautifulSoup
import requests
import json 

def get_doenca_info(url_href):
    url_doenca = "https://www.atlasdasaude.pt" + url_href 
    response = requests.get(url_doenca)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    div_content = soup.find("div", class_="node-doencas")
    return {"url": url_doenca, "content": str(div_content)}

def doencas_letra(letra):
    url = "https://www.atlasdasaude.pt/doencasaaz/" + letra
    print(url)
    response = requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    doencas = {}
    for div_row in soup.find_all("div", class_="views-row"):
        designacao = div_row.div.h3.a.text.strip()
        doenca_url = div_row.div.h3.a["href"]
        doenca_info = get_doenca_info(doenca_url)
        desc_div = div_row.find("div", class_="views-field-body")
        desc = desc_div.div.text
        doenca_info["resumo"] = desc.strip().replace(" "," ")
        doencas[designacao] = doenca_info  
            
    return doencas

res = {}
for a in range(ord("a"), ord("z") + 1):
    letra = chr(a)
    res = res | doencas_letra(letra)
    
print(res)
f_out = open("doencas_3.json", "w")

json.dump(res,f_out, indent=4, ensure_ascii=False)
f_out.close()
    


