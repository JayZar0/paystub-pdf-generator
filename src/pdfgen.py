from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
import json

# This file will contain the pdf generator

class generator:
  def __init__(self, path):
    self.path = path
    pass

  # This function will be used to generate a pdf file using the data that is
  # passed in during the call
  def generatePdf(self, paydata):
    # organize the data
    statement = paydata['statements'][0]['statement']
    company = statement['company']
    employee = statement['employee']
    balance = statement['balance']
    earning = statement['earning']
    deduction = statement['deduction']
    summary = statement['summary']

    # grab the layout and store it in a variable for later use
    env = Environment(loader=FileSystemLoader('./resources'))
    template = env.get_template('pdflayout.html')

    # map the data to its variable and then place it in the html template
    data = {
      "date":company['paymentDate'],
      "name": f"{employee['lastName']}, {employee['firstName']}",
      "empNumber": employee['employeeNumber']
    }
    rendered_html = template.render(data)

    # writeout the pdf file and then save it.
    try:
      with open(self.path, "w+b") as pdf:
        pisa_status = pisa.CreatePDF(rendered_html, dest=pdf)
    except:
      print(f"Error occured while trying to open file, {self.path} doesn't exist")
      return

    if not pisa_status.err:
      print(f'Success! File saved to {self.path}')
