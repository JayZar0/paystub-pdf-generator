# Paystub PDF Generator
This application will be used to generate a pdf file of your payroll automatically if your employer
publishes a new one under your name. The purpose for this is to remove the need for
authentication to your payroll service and instead will use a single authentication for
gathering your api key. This service can be used depending on if your jobs paystub
service allows for the creation of an api key.

## Setup
To set up the application you must:
1. log in into your account for your paystub
2. generate or request for an api key
3. go to the application and place your authentication key into the http request header
4. launch the application and it will run persistently

## Usage
Once the application is started, then it will open a prompt that will ask the user for
their api key and the url of their applications endpoint. Once the user submits their
credentials then it will perform a verification, and if it fails then it will repromt
the user stating that the provided information is invalid. If it succeeds then a
background process will start that will open a listener that will wait for your
employer to publish a payroll. Once published then it will generate a pdf and then
save it to your dedicated directory.

## Customization
If you wanna customize the layout of the pdf file, go to the pdfgen.py file and then
search for the generate_template function. Then search for the html string that generates
the pdf file and edit it to your liking. Make sure to save the changes if your editor
doesn't have autosave.

## Closing the application
1. Open task manager
2. The process name will just be named paystubgenerator and will be a background process
3. Kill it, terminate it, close it, end it do whatever the os wants you to do to close it.

## Open on start up
WILL BE WRITTEN SOON. iykyk.

## Disclaimer
This service does not require a connection to any other services other than your
paystub service therefore we do not collect any information on your salary.