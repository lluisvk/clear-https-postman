import json
import os
def find_urls(items):
    for item in items:
        request = item.get("request")
        if request and "url" in request:
            raw = (request["url"]["raw"])
            if raw.startswith('http://{{host}}') or raw.startswith('http://localhost:8080') :
                raw =raw.replace('http://{{host}}','{{host}}').replace('http://localhost:8080','{{host}}')
                request["url"]["raw"] = raw
                print(raw)
        if "item" in item:
            find_urls(item["item"])

if not os.path.exists('ERP Vockan.postman_collection.json'):
    raise FileNotFoundError('Não foi encontrado um arquivo com este nome e extensão')

with open('ERP Vockan.postman_collection.json','r',encoding="utf-8") as f:
    data = json.load(f)

find_urls(data.get("item", []))

with open('ERP Vockan.postman_collection.json', "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
