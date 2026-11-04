# Función para colocar un texto en negrita
def negrita(texto):
    return "\033[1m" + texto + "\033[0m"


# Función para subrayar un texto
def subrayado(texto):
    return "\033[4m" + texto + "\033[0m"
