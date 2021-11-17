filetxt = open('filtro_media21x21.txt', 'w')
razao = 1/(21*21)

for _ in range(0, 21):
    for _ in range(0, 21):
        filetxt.write(f'{razao} ')
    filetxt.write('\n')

filetxt.close()
