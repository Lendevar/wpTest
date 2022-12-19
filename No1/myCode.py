# Здарова! Короче, сам разберёшься чё по чём
# Вот допуски: 
# видеокарта от 2 до 3 кг
# телефон от 0.5 до 0.7 
# телик от 3 до 7
# энергос от от 0.48 до 0.52
# хавчик от 0.95 до 1.05 

myFile = open("check.txt", "r", encoding='utf-8')
content = myFile.readlines()
fileLength = len(content)
counter = 1

while counter != fileLength:
    ware = content[counter].split(" ")[0]   # Тут типа название товара в посылке
    weight = content[counter].split(" ")[1] # Тут типа его вес

    # Нашамань чёнить отседова
    


    # Доседова

    counter += 1

