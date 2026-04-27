# This file is the main code for the application
import requests
import os
from datetime import date
from dotenv import load_dotenv
from pdfgen import generator

# Grab the api key, then place it in the request header and also grab the url
load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('PAYROLL_URL')
headers={
  "Authorization": f"Bearer {api_key}",
  "accept":"application/json"
}


# Perform the webrequest
res = requests.get(url, headers=headers)

if res.ok:
  # If the response is good then generate the pdf file using the elements in the
  # web pay stub
  filename = f'payrolls/{date.today()}.pdf'
  print(f"Http request succeeded on {date.today()}")
  pdf = generator(f"{filename}")
  pdf.generatePdf(res.json())
else:
  # TODO: create other errors based on where generation failed
  print(f"The request has failed on {date.today()}")
