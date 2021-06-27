#! python3
"""
Task 12 - Challenge Time! -> https://tryhackme.com/room/introtopython

O arquivo "encodedflag.txt" possui uma flag que foi codificada na seguinte ordem:
Codificado 5 vezes usando base64
Codificado 5 vezes usando base32
Codificado 5 vezes usando base16

Logo, a decodificação deve ser feita na ordem reversa, indo do base16 até chegar no base64
e consequentemente na Flag.
"""

import base64

texto_codificado = ''
flag = ''

with open('encodedflag.txt', 'r') as arquivo:
    texto_codificado = arquivo.read()

    # Decodificando de base16 para base32
    for i in range(0, 5):
        texto_codificado = base64.b16decode(texto_codificado)
        print(f'{i+1}° Iteração base16: ' + str(texto_codificado))
        print("-----//-----")

    # Decodificando de base32 para base64
    for i in range(0, 5):
        texto_codificado = base64.b32decode(texto_codificado)
        print(f'{i+1}° Iteração base32: ' + str(texto_codificado))
        print("-----//-----")

    # Decodificando de base64 até obter a flag
    for i in range(0, 5):
        texto_codificado = base64.b64decode(texto_codificado)
        print(f'{i+1}° Iteração base64: ' + str(texto_codificado))
        print("-----//-----")


flag = str(texto_codificado)  # Nesse ponto, o texto está completamente desofuscado
print("Flag encontrada: " + flag)
