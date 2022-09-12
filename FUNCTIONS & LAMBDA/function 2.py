def details(Name,roll):
    print("Name:",Name)
    print("Roll:",roll)
details('Nandhu',5)                 #required arguments


def details(name,roll):
    "For saving details"             #document string - mattullavar nokumbol program enthinaenn manasilavan
    print("Name:",name)
    print("Roll:",roll)
details(roll=5,name='Nandhu')          #keyword arguments