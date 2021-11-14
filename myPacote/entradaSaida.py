def escreva(qualTipo=None):
    val = input('\n\t Escreva um valor: ')
    if qualTipo == 'flutuante':
        return float(val)
    if qualTipo == 'inteiro':
        return int(val)
    if qualTipo == 'txt':
        return val
