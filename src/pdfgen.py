from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader

# This file will contain the pdf generator

class generator:
  def __init__(self, path):
    self.path = path
    pass

  # This function will be used to generate a pdf file using the data that is
  # passed in during the call
  def generatePdf(self, paydata):
    # organize the data
    statement = paydata.statement
    company = paydata.company
    employee = paydata.employee
    balance = paydata.balance
    earning = paydata.earning
    deduction = paydata.deduction
    summary = paydata.summary

    # grab the layout and store it in a variable for later use
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('pdflayout.html')

    # map the data to its variable and then place it in the html template
    data = {
      
    }
    rendered_html = template.render(data)

    # writeout the pdf file and then save it.
    with open(self.path, "r+w") as pdf:
      pisa_status = pisa.CreatePDF(rendered_html, dest=pdf)
    
    if not pisa_status.err:
      print(f', saved to ${self.path}')
