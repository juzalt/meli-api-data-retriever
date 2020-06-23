#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
	MeLi-api-data-retriever - 01.02.20 - Julian Zaltron (juzalt)
------------------------------------------------------------------------------
"""

## # LIBRARIES # ##
import requests, json

## # CONTEXT VARIABLES # ##
version = 1.0

## # MAIN FUNCTIONS # ##
def banner():
	global version
	b = '''
         ___   ____   __
        | _ \_/   |  | |      
        | |\   /| |  | |      
        | | \_/ | |  | |____ 
        |_|     |_|e |______|i Api Data Retriever 
	
    Version {v}
    Made by Noah Pomilio

    Usage: python3 main.py -r <region> -q <search query> [-o outputFile.txt]
    Example: python3 main.py -r MLA -q samsung_tv -o argentine-samsung-tv.txt

    Check for possible regions @ https://api.mercadolibre.com/sites/
	'''.format(v=version)
	print(b)

def parse_args():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('-o', '--output', type=str, help="Output file.")
  parser.add_argument('-r', '--region', type=str, required=True, help="Region.")
  parser.add_argument('-q', '--query', type=str, required=True, help="Search Query.")
  return parser.parse_args()

def save_products(product,output_file):
  fileContent = json.dumps(product)
  with open("./results/{o}".format(o=output_file),"a") as file:
    file.write(fileContent)
    file.close()

def main():
  banner()
  args = parse_args()

  products = []
  output = args.output
  query = args.query
  siteID = args.region

  req = requests.get("https://api.mercadolibre.com/sites/{}/search?q={}".format(siteID, query))

  if req.status_code != 200:
    print("Something went wrong. Check https://status.mercadolibre.com/")
    exit(1)

  response_data = req.json()

  for product in response_data["results"]:
    products.append(product)

  for product in products:
    print("\n {p}".format(p=product))
    if output is not None:
      save_products(product,output)

  print("\n\n That's all folks!")

main()