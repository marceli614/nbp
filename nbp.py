import requests

import time

import sys

import logging

import jsonschema

import json

from jsonschema import validate

#Dodanie logowania do pliku.

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

n = len(sys.argv)
if (n>1):
    sysx=int(sys.argv[1])
    sysy=int(sys.argv[2])
else:
    sysx=10
    sysy=5

print(sysx)
print(sysy)

#Funkcja

def marfun(x,y):
  for i in range(0, x):
    host = 'http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json'


    logging.info("Wyslam zadanie Get na zadany host:")
    logging.info(host)

    #1. Wysla zadanie Get na zadany host

    x = requests.get(host)

    logging.info("Sprawdzenie Czasu:")
    logging.info(x.elapsed)

    #2. Mierzyl czas od wyslania zadania do czasu odpowiedzi.
    print(x.elapsed)

    logging.info("Sprawdzenie Status Code:")
    logging.info(x.status_code)

    #3. Sprawdzal kod odpowiedzi HTTP
    print(x.status_code)

    print(x.headers)

    #4. Sprawdzal czy odpowiedz to JSON content-type
    contentType = x.headers['content-type']

    logging.info("Sprawdzenie Content type:")
    logging.info(contentType)

    print(contentType)

    # Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)

    print(x.json())

    schema = {
      "type": "object",
      "required": [],
      "properties": {
        "table": {
          "type": "string"
        },
        "currency": {
          "type": "string"
        },
        "code": {
          "type": "string"
        },
        "rates": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [],
            "properties": {
              "no": {
                "type": "string"
              },
              "effectiveDate": {
                "type": "string"
              },
              "mid": {
                "type": "number"
              }
            }
          }
        }
      }
    }

    # s=jsonschema.validate(x.json, schema)

    #5. Walidował czy JSON z odpowiedzi ma prawidłową składnię
    print(validate(instance=x.json(), schema=schema))
    logging.info("Sprawdzenie struktury JSONa:")
    logging.info(validate(instance=x.json(), schema=schema))

    t = 3
    time.sleep(y)

#6. Wykonywał X sprawdzeń, co Y sekund

marfun(sysx,sysy)




kurs = {
    "table": "A",
    "currency": "euro",
    "code": "EUR",
    "rates": [
        {
            "no": "045/A/NBP/2024",
            "effectiveDate": "2024-03-04",
            "mid": 4.3201
        },
        {
            "no": "046/A/NBP/2024",
            "effectiveDate": "2024-03-05",
            "mid": 4.3228
        }
    ]
}

#[Zadanie dodatkowe]

host = 'http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json'

x = requests.get(host)

z=x.json()
print(x)
print(x.json())


lasteuro = z
wartosc='NIE'
if 'rates' in lasteuro:
    #print("MAR1")
    for item in lasteuro['rates']:
        #print("MAR3")
        print(item['mid'])
        if item['mid'] > (4.5) and item['mid'] < (4.7):
            wartosc='TAK'
            logging.info(wartosc)
            logging.info(item['effectiveDate'])
            logging.info(item['mid'])


print(wartosc)