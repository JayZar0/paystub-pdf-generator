# This file will contain the pdf generator

class generator:
  def __init__(self, filename):
    self.filename = filename
    pass

  # This function will be used to generate a pdf file with all the data passed
  # into the constructor
  def generatePdf(paydata):
    raise NotImplementedError("Function currently not implemented")

  # This function will be used to save the pdf file to the passed in directory
  def savePdf(directory):
    raise NotImplementedError("Function currently not implemented")

