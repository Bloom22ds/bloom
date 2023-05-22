from random import shuffle
spisog_omg = ['вода', 'магия','волшебство']
triks = input('Введи ингридиент (харош - стоп):')
while triks != 'хорош':
    if triks in spisog_omg:
        print('Этот ингридиент ужэ есть')
    else:
        spisog_omg.append(triks)
    triks = input('Введи ингридиент (харош - стоп):')

spisog_blender = []
nums = int(input('Сколько месим ингридиентов:'))
for i in range (nums):
    shuffle(spisog_omg)
    spisog_blender.append(spisog_omg[0])
    spisog_omg.remove(spisog_omg[0])

print('Приготовь что-нибудь из:')
for i in range (nums):
    print(spisog_blender[i])