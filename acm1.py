import boto3
import sys
print('Pegue el cuerpo del certificado.Presiona una vez enter, luego presiona Ctrl-D para guardar.')
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
print('Pegue la clave privada del certificado.Presiona una vez enter, luego presiona  Ctrl-D para guardar.')
keys = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    keys.append(line)
privateKey= '\n'.join([str(elem) for elem in keys])
print('Pegue la cadena de certificados.Presiona una vez enter, luego presiona  Ctrl-D para guardar.')
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
