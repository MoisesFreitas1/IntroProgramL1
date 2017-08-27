import json
import requests
r = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=USD&alt=json')
if r.status_code == 200:
    quote_data = json.loads(r.content)
    quote = quote_data['valores']['USD']['valor']
print("DÓLAR HOJE")
print("$1 = R$%.2f"%quote)
print("\nConversão USD/BRL")
dolar = float(input("$"))
real = dolar*quote
print(" -> R$%.2f"%real)