nicknames = ['Cincoo','FiveTwo','Damiano','Daktari','Senior','Esq','MD',\
    'Washi','Damish']
print(nicknames)

short = list(filter(lambda x: len(x) < 7, nicknames))
print(short)
