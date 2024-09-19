personas = {
    "Manoli": 49,
    "Ermenegildo": 33,
    "Pepe": 12,
    "Azir": 8,
    "Zofi": 35,
    "Kike": 7,
    "Carlos": 99,
    "Ivan": 2,
    "Jaume": 29,
    "Alex": 24
}

for nombre, edad in personas.items():
    if edad > 20:
        print(f"{nombre} tiene {edad} años.")