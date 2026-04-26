# This file is the main code for the application
import requests
import os
from dotenv import load_dotenv
from pdfgen import generator

# Grab the api key
load_dotenv()
api_key = os.getenv('API_KEY')

# Perform the webrequest
headers={
  "Authorization": f"Bearer ${api_key}"
}
res = requests.get()

# If the response is good then generate the pdf file
if res.ok():
  print("The request works")
else:
  print("The request has failed or your api key is invalid")

# Then save it in a the specified directory
