# Contenido sugerido de main.py (guía; completa la lógica por tu cuenta):
# ------------------------------------
# main.py
# Meta: Leer CSV con open/close/read/... y construir una matriz (lista de listas)
# Usa: open: Abrir archivo, close: Cerrar archivo, for para recorrer líneas del archivo, rstrip, split
def leer_csv_a_matriz(nombre_archivo):
    matriz = []
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    for linea in archivo:
        lista_renglon = linea.rstrip("\n").split(",")
        matriz.append(lista_renglon)
    archivo.close()
    return matriz
def main():
    datos = leer_csv_a_matriz("titanic.csv")
    print("Encabezados:")
    print(datos[0])
    print("Primera línea:")
    print(datos[1])
# TODO:Agrega el çodigo requerido para imprimir lo siguiente:
# ¿Cuántos objetos hay? ¿Cuántas variables hay? ¿Cuál es el valor de la variable 2 del objeto 4?
    print("\nNúmero de objetos:", len(datos) - 1)  # menos 1 porque la primera fila son encabezados
    print("Número de variables:", len(datos[0]))
    print("Valor de la variable 2 del objeto 4:", datos[4][1])
main()

