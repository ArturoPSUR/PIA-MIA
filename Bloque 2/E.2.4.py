"""“E2.4 · Frecuencia de palabras de un texto: normaliza, separa y
cuenta; muestra el top 5."""

texto = input("Introduce un texto: ")

texto = texto.lower()
for signo in [".", ",", ";", "!", "?", "¡", "¿"]:
    texto = texto.replace(signo, "")

palabras = texto.split()

frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print("\n5 palabras más usadas: ")
for i in range(5):
    if not frecuencias:
        break

    max_palabra = None

    for palabra in frecuencias:
        if max_palabra is None or frecuencias[palabra] > frecuencias[max_palabra]:
            max_palabra = palabra
            
    print(f"- '{max_palabra}'= {frecuencias[max_palabra]} veces")
    del frecuencias[max_palabra]