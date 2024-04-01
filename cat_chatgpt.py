class Gato:
    def __init__(self, nombre, tipo_maullido):
        self.nombre = nombre
        self.tipo_maullido = tipo_maullido

    def expresar_sentimiento(self):
        if self.tipo_maullido == 'feliz':
            return f"{self.nombre} está contento y ronronea."
        elif self.tipo_maullido == 'triste':
            return f"{self.nombre} se siente triste y maúlla suavemente."
        elif self.tipo_maullido == 'enojado':
            return f"{self.nombre} está enojado y maúlla fuerte."
        elif self.tipo_maullido == 'asustado':
            return f"{self.nombre} está asustado y maúlla nerviosamente."
        elif self.tipo_maullido == 'curioso':
            return f"{self.nombre} está curioso y emite maullidos cortos."
        else:
            return f"{self.nombre} no reconoce este tipo de maullido."

# Crear un objeto gato
mi_gato = Gato('Garfield', 'feliz')

# Llamar al método expresar_sentimiento con un tipo de maullido
sentimiento = mi_gato.expresar_sentimiento()
print(sentimiento)  # Salida: "Garfield está contento y ronronea."
