'''Una tienda ofrece un porcentaje de descuento sobre el importe de la compra de los cuatro tipos de productos cuyos códigos, precios unitarios y descuentos se muestran en las siguientes tablas. 
Desarrolle el programa que determine el importe de la compra, el descuento y el total a pagar por la compra de cierta cantidad de unidades de un mismo tipo de producto. 
Código Precio Unitario  Unidades Descuento 
 101 17   1 a 10 5 % 
102 25  11 a 20 8 % 
103 16  21 a 30 10 % 
104 27  31 a mas 13 %'''


codigo = int(input("Ingrese codigo de producto: "))

if codigo == 101 :
    precio = 17
elif codigo == 102 :
    precio = 25
elif codigo == 103 :
    precio = 16
elif codigo == 104 :
    precio = 27

else :
    print("ingrese un codigo correcto")
    exit()


cantidad = int(input("Ingrese cantidad de producto: "))


importe = cantidad * precio


if codigo == 101 and cantidad > 0 and cantidad <=10 :
    descuento = importe * 0.05

elif codigo == 102 and cantidad >= 11 and cantidad <=20 :
    descuento = importe * 0.08

elif codigo == 103 and cantidad >= 21 and cantidad <=30 :
    descuento = importe * 0.10

elif codigo == 104 and cantidad >= 31 :
    descuento = importe * 0.13

else :
    descuento = 0


total_compra = importe - descuento

print("DETALLE DE COMPRA:")
print("----------------------------")
print(f"El codigo del producto es: {codigo}")
print(f"La cantidad es: {cantidad}")
print(f"El importe de la compra es: {importe:.2f} PEN")
print(f"El decuento es: {descuento:.2f} PEN")
print(f"El monto a pagar es : {total_compra:.2f} PEN")







