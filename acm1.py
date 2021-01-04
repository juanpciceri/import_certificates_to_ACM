""" 
This script uses boto3 library from python, it allows an external user that does not have AWS console access
to import certificates to an AWS account if he has regular CLI access keys and proper role to interact with AWS certificate manager. 
Progam will ask to input three times, the first time user must input the .pem body, the second one, user must input  .key body and 
finally the third one user must include .crt body. The program will return the ARN of the certificate.

"""
import boto3
import sys
print('Paste body certificate -must be PEM hardcoded).to continue, press one time enter and then Ctrl-D to save.')
contents = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    contents.append(line)
certificate = '\n'.join([str(elem) for elem in contents])
#f=open('/home/utilunix/certificate_load/file.txt','a+')
#f.write(certificate)
#f.close
print('Paste certificate private keys -must be PEM hardcoded).to continue, press one time enter and then Ctrl-D to save.')
keys = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    keys.append(line)
privateKey= '\n'.join([str(elem) for elem in keys])
print('Paste certificate chain -must be PEM hardcoded).to continue, press one time enter and then Ctrl-D to save.')
chains = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    chains.append(line)
chain= '\n'.join([str(elem) for elem in chains])
print('Ingrese el nombre que desea colocar de etiqueta/tag')
llave=input("")
print('Ingrese el valor que desea colocar de etiqueta/tag')
valor=input("")

# print(listToStr)

#certificate = \
#    open('/home/utilunix/certificate_load/file1.txt'
#         , 'rb').read()
#privatekey = \
#   open('/home/utilunix/certificate_load/inspecciones-dev.libertyseguros.co.key'
#         , 'rb').read()
#chain = \
#    open('/home/utilunix/certificate_load/chain.crt'
#         , 'rb').read()

acm=boto3.client('acm')
test=acm.import_certificate(
Certificate=certificate,
PrivateKey=privateKey,
CertificateChain=chain,
Tags=[
{
'Key': llave,
'Value': valor
},
]
)
print(test['CertificateArn'])

#print (listToStr)
