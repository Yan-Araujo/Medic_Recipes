import re
from validate_docbr import CPF


def validated_nome(nome):
    if re.search('^[A-Za-z ]+$', nome):
        return nome


def validated_cpf(valid_cpf):
    cpf = CPF()
    return cpf.validate(valid_cpf)


