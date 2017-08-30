#Script to connect to an API and get the output

from suds.client import Client

client=Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')

result = client.service.ConvertSpeed(800,'kilometersPerhour','milesPerhour')
print (result) 
