def birthday(s, d, m):
    """
    s: lista de enteros (la barra de chocolate)
    d: suma objetivo (el día de cumpleaños)
    m: longitud del subarreglo (el mes de cumpleaños)
    """
    count = 0
    
    # Recorremos todos los posibles subarreglos de longitud m
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
            
    return count

s = [1, 2, 1, 3, 2]
d = 3   # sum
m = 2   # length

print(birthday(s, d, m))  
