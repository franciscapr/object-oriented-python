def orderPizza(size, style='regular', topping=None):
    # Realizar algunos cálculos basados en el tamaño y el estilo
    # Verificar si se especificó un ingrediente adicional
    PRICE_OF_TOPPING = 1.50  # precio de cualquier ingrediente adicional

    if size == 'small':  # pequeño
        price = 10.00
    elif size == 'medium':  # mediano
        price = 14.00
    else:  # grande
        price = 18.00

    if style == 'deepdish':  # estilo deepdish (masa gruesa)
        price = price + 2.00  # cobrar extra por deepdish

    line = 'Has ordenado una pizza ' + size + ' de estilo ' + style + ' con '
    if topping is None:  # verificar si no se pasó un ingrediente adicional
        print(line + 'sin ingredientes adicionales')
    else:
        print(line + topping)
        price = price + PRICE_OF_TOPPING

    print('El precio es $', price)
    print()

# Puedes ordenar una pizza de las siguientes maneras:
orderPizza('large')  # grande, por defecto estilo regular, sin ingredientes adicionales
orderPizza('large', style='regular')  # igual que la anterior
orderPizza('medium', style='deepdish', topping='champiñones')
orderPizza('small', topping='champiñones')  # el estilo por defecto es regular
