import csv

file_name = "videogames_tab.tsv"  # Saved using tab separator

# Open CSV and write with tab delimiter
with open(file_name, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter="\t")  # <---- TAB SEPARATOR
    writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])  # Header

    while True:
        print("\nIngrese los datos del videojuego:")

        nombre = input("Nombre: ")
        genero = input("Género: ")
        desarrollador = input("Desarrollador: ")
        clasificacion = input("Clasificación ESRB: ")

        writer.writerow([nombre, genero, desarrollador, clasificacion])

        continuar = input("¿Desea agregar otro videojuego? (si/no): ").strip().lower()
        if continuar != "si":
            break

print("\nArchivo guardado correctamente como:", file_name)