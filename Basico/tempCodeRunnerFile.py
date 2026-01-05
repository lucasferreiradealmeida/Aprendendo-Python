import re

# cpf_enviado_usuario = '321.543.534-76'.replace('.','') \
# .replace('-','') 
# print(cpf_enviado_usuario)

cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    '321.543.534-76'
)
print(cpf_enviado_usuario)