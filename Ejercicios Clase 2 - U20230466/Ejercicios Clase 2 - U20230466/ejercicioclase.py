# Ejercicio de la clase: Bolitas de colores
Azul = 0.05
Rojo = 0.15
Negro = 0.0
Rosado = 0.75

print("\n--------TIENDA DE BOLITAS--------")
print("\n-------COLORES DISPONIBLES-------")
print("\n--- Azul, Rojo, Negro, Rosado ---")

colorbolita = input("\n¿Qué color de bolita desea comprar? ")
preciobolita = float(
    input("\n¿Cuánto pagará por la bolita de color " + colorbolita + "? "))

descuento = 0.0
total_a_pagar = preciobolita

if colorbolita == "Azul":
    descuento = preciobolita * Azul
elif colorbolita == "Rojo":
    descuento = preciobolita * Rojo
elif colorbolita == "Negro":
    descuento = preciobolita * Negro
elif colorbolita == "Rosado":
    descuento = preciobolita * Rosado
else:
    print("Color de bolita no valido, no se aplicará descuento.")

total_a_pagar -= descuento

print("\nDetalles de la compra:")
print("Color de bolita: " + colorbolita)
print("Precio de bolita: $" + str(preciobolita))
print("Porcentaje de descuento: " + str(descuento * 100) + "%")
print("Valor del descuento: $" + str(descuento))
print("Total a pagar: $" + str(total_a_pagar))
