from tokenize import Name
from unicodedata import name
import requests
import json
import sys

from requests.api import request

url = "https://api.bouyguestelecom.fr/ventes/mur-produits?type=phone"
url2 = "https://open.api.sandbox.bouyguestelecom.fr/ap4/customer-management/v1/customer-accounts"

payload={}
headers = {
  'Content-Type': 'application/json',
  'x-version': '4'
}
headers2 = {
  'x-banc': 'ap23',
  'x-version': '4',
  'TrackerId': 'aaed2799-fbcc-318a-e4de-b183966c2a89',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer at-0bece344-7983-4e2f-ad26-88fdcd877ed1'
}

response = requests.request("GET", url, headers=headers, data=payload)
output = response.json()


def iphoneHeight():
  Name = output['categories']['phone']['products']['4788']['name']
  price = output['categories']['phone']['products']['4788']['price']
  forfait = output['categories']['phone']['products']['4788']['prices']['premium']['plan_name']
  print("L'",Name, "Est disponible sur notre catalogue!")
  print("Il comporte plusieur caractéristique!")
  print("Ce téléphone s'élève au prix de ",price,"Euro")
  print("Il est disponible en plusieurs couleur différente: Rouge et Noir\n",)
  print("Nous pouvons suite à cela Pour l'",Name," vous proposez une Offre BoyguesTélecom",forfait,"\n")

def iphoneThirteen():
  Name = output['categories']['phone']['products']['7934']['name']
  price = output['categories']['phone']['products']['7934']['price']
  forfait = output['categories']['phone']['products']['7934']['prices']['premium']['plan_name']
  print("L'",Name, "Est disponible sur notre catalogue!")
  print("Il comporte plusieur caractéristique!")
  print("Ce téléphone s'élève au prix de ",price,"Euro")
  print("Il est disponible en plusieurs couleur différente: Rose, Bleu, Noir, Rouge\n",)
  print("Nous pouvons suite à cela Pour l'",Name," vous proposez une Offre BoyguesTélecom",forfait,"\n")

def samsungS20():
  Name = output['categories']['phone']['products']['6144']['name']
  price = output['categories']['phone']['products']['6144']['price']
  forfait = output['categories']['phone']['products']['6144']['prices']['premium']['plan_name']
  print("Le",Name, "Est disponible sur notre catalogue!")
  print("Il comporte plusieur caractéristique!")
  print("Ce téléphone s'élève au prix de ",price,"Euro")
  print("Il est disponible en plusieurs couleur différente: Noir, bleu et Rouge\n",)
  print("Nous pouvons suite à cela Pour le",Name,"vous proposez une Offre BoyguesTélecom",forfait,"\n")

def check_phone():
  if len(sys.argv) > 1:
    if sys.argv[1] == "iphone":
      if sys.argv[2] == "8":
        iphoneHeight()
      if sys.argv[2] == "13":
        iphoneThirteen()
    if sys.argv[1] == "samsung":
      samsungS20()
  else:
    print("Vous discuter avec le Service client BouyguesTélécom de Whatsapp ;)\nSi vous voulez consulter nos téléphone disponible sur notre catalogue\nentrez le model du téléphone et nous vous indiquerons si le téléphone est disponible à la vente!\nToute les caractéristique du téléphone vous serons aussi communiqués :)")
    print("pour une assistance plus poussée ou pour toute autres informations veuillez nous contactez au +33986010463")

def main():
  if len(sys.argv) == 2 :
    if sys.argv[1] == "iphone" :
      iphoneThirteen()
      iphoneHeight()
    elif sys.argv[1] == "samsung" :
      samsungS20()
    else :
      return()
  else :
    check_phone()
  print("Avez vous un compte un compte client?")
  haveAcompte = input()
  if (haveAcompte == "oui"):
    return()
  else :
    print("voulez vous un compte client ?")
    Want = input()
    if (Want == "oui"):
      birthday = input()
      birthDepart = input()
      emailAdresse = input()
      firstName = input()
      lastname = input()
      phonenumber = input()
      genre = input()
    else:
      return()

if __name__ == "__main__":
    main()