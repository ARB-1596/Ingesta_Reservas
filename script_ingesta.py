import boto3
import pandas as pd
import requests

URL_vuelos = "http://IP_PRIVADA:PUERTO/ENDPOINT"

response = requests.get(URL_vuelos)
data = response.json()

df = pd.DataFrame(data)
df.to_csv("reservas.csv", index=False)

ficheroUpload = "ingesta/reservas/reservas.csv"
nombreBucket = "tickets-aereo"

s3 = boto3.client('s3')
response = s3.upload_file("reservas.csv",nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")
