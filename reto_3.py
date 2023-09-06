num_categorias = int(input("Ingrese la cantidad de categorías: "))
categorias = []


for i in range(1, num_categorias + 1):
    id_categoria = i
    nom_categoria = input("Ingrese el nombre de la categoría: ")

    categoria = {
        "id": id_categoria,
        "nom_categoria": nom_categoria
    }

    categorias.append(categoria)

num_productos = int(input("Ingrese la cantidad de productos: "))
productos = []


for i in range(1, num_productos + 1):
    id_producto = int()
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = int(input("Ingrese el precio del producto: "))

   
    print("Categorías disponibles:")
    for categoria in categorias:
        print(f"{categoria['id']}: {categoria['nom_categoria']}")

    
    id_categoria = int(input("Seleccione la categoría del producto: "))

    producto = {
        "id": id_producto,
        "nombre": nombre_producto,
        "precio": precio_producto,
        "id_categoria": id_categoria
    }

    productos.append(producto)


diccionario_resultante = {
    "id_producto": {producto["id"]: {"nombre": producto["nombre"], 
    
    "categoria": categorias[producto["id_categoria"] - 1]["nom_categoria"]} for producto in productos}
}


print("\nResultante:")
print(diccionario_resultante)
