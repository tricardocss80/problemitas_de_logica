bolas_azules = 21
bolas_rojas = 46

print(f'Ariel tiene inicialmente {bolas_azules} bolas azules y {bolas_rojas} bolas rojas')


def despues_de_cinco_dias_azules():
    nuevo_bolas_azules = 0
    for i in range(1, 6):
        nuevo_bolas_azules = bolas_azules + (i * 2)
    return nuevo_bolas_azules

def despues_de_cinco_dias_rojas():
    nuevo_bolas_rojas = 0
    for i in range(1, 6):
        nuevo_bolas_rojas = bolas_rojas + (i * -3)
    return nuevo_bolas_rojas

def despues_de_nueve_dias_azules():
    nuevo_bolas_azules = 0
    for i in range(1, 10):
        nuevo_bolas_azules = bolas_azules + (i * 2)
    return nuevo_bolas_azules

def despues_de_nueve_dias_rojas():
    nuevo_bolas_rojas = 0
    for i in range(1, 10):
        nuevo_bolas_rojas = bolas_rojas + (i * -3)
    return nuevo_bolas_rojas


print(f'Despues de 5 dias Ariel tiene {despues_de_cinco_dias_azules()} bolas azules y {despues_de_cinco_dias_rojas()} bolas rojas')
print(f'Y despues de 9 dias Ariel tiene {despues_de_nueve_dias_azules()} bolas azules y {despues_de_nueve_dias_rojas()} bolas rojas')
