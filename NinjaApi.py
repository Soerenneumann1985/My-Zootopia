import requests

api_key = "JhHpehCghmuA5akW8Jal2GvlzbuEtzsbdCIFFnrv"

url = "https://api.api-ninjas.com/v1/animals"

tiername = "elephant"



headers = {
    "X-Api-Key": api_key
}



responce = requests.get(url=f"{url}?name={tiername}", headers=headers)



print(responce.status_code)
print(responce.json())