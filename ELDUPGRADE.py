def upgrade(MaxHp,MaxSp,Attack):
    #Welcome message
    print("Welcome to my humble shop hero, My Name is Nadakan, how may I help you today")
    #Sells 3 upgrades only
    U = 3
    while U > 0:
        x = int(input(f"To upgrade health press 1 / To upgrade Stamina press 2 / To upgrade Attack Power press 3/ remaining upgrades {U} : "))
        if x == 1:
            MaxHp += 25
            print("Health upgraded")
        elif x == 2:
            MaxSp += 15
            print("Stamina upgraded")
        elif x == 3:
            Attack += 0.1
            print("Attack Power increased")
        else:
            print("Sorry Hero I don't have what you are looking for")
            U +=1
        U -= 1
    return MaxHp,MaxSp,Attack

