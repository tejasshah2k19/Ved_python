import json 
import requests 

# https://api.restful-api.dev/objects/7
#pip install requests 


#requests 

# print(json)
# print(requests)


url = "https://api.restful-api.dev/objects/7"

response = requests.get(url)
print(response.text)

ans  = response.text 

print(type(ans))

product = json.loads(ans)

print(product)
print(type(product))

print(product.get("name"))

with open("data.json","w") as file : 
    json.dump(product,file)
