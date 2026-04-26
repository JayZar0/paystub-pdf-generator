# This file is the main code for the application
import requests
import os
from dotenv import load_dotenv
from pdfgen import generator

# Grab the api key
load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('PAYROLL_URL')

# Perform the webrequest
headers={
  "Authorization": f"Bearer ${api_key}",
  "accept":"application/json"
}
res = requests.get(url, headers=headers)

if res.ok:
  # If the response is good then generate the pdf file using the elements in the
  # web pay stub
  print("The request works")
  print(res.json())
  pdf = generator()

  # after generating the pdf file then save it in the 
else:
  print("The request has failed or your api key is invalid")
