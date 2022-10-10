import LAB_PROJECT4
from ELDUPGRADE import upgrade
from time import sleep

print("Hello there hero my name is Wu ")
sleep(1)
print("I see that you have arrived on the right Time")
sleep(1)
print("A portal to the Land of the dead has appeared out of no where")
sleep(1)
print("The Dead I am reffering to are Dead Memes from the internet")
sleep(1)
print("We sent our scout to check what is behind this portal")
sleep(1)
print("But Sadly he didn't make it back")
sleep(1)
print("And that is where we need you to go in an find the evil behind this Mess")
V = False
x = 'n'
while x != 'y':
    x = input("When you are ready Let me know (Enter y to start the game) ")
if x == 'y':
    print("Good luck hero, come back safe please")
    while V == False:
        Boss_IMAGE, Boss_IMAGE2 = LAB_PROJECT4.chooseboss(1) 
        MaxHp , MaxSp, Attack, V = LAB_PROJECT4.main('Among Us' , 100 , 1, 100 , 100, 1, Boss_IMAGE, Boss_IMAGE2)
    #LAB_PROJECT4.draw_window(MaxHp,MaxSp,5,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
    V = False
    print("Good Job Hero")
    sleep(3)
    print("I See You have 3 Upgrade Points")
    sleep(1)
    print("Make Sure to give nadakan a visit to upgrade yourself")
    sleep(1)
    MaxHp,MaxSp,Attack = upgrade(MaxHp,MaxSp,Attack)
    print("I see you are stronger now")
    sleep(1)
    print("Now Hero you are ready to fight, come back safe")
    while V == False:
        Boss_IMAGE, Boss_IMAGE2 = LAB_PROJECT4.chooseboss(2)
        #LAB_PROJECT4.draw_window(MaxHp,MaxSp,5,150,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
        MaxHp , MaxSp, Attack, V= LAB_PROJECT4.main('Big Floppa' , 200 , 1, MaxHp , MaxSp, Attack , Boss_IMAGE, Boss_IMAGE2)
    V = False
    MaxHp,MaxSp,Attack = upgrade(MaxHp,MaxSp,Attack)
    
    while V == False:
        Boss_IMAGE, Boss_IMAGE2 = LAB_PROJECT4.chooseboss(3)
        MaxHp , MaxSp, Attack, V = LAB_PROJECT4.main('Big Chungus' , 200 , 1.2, MaxHp , MaxSp, Attack , Boss_IMAGE, Boss_IMAGE2)
    V = False
    MaxHp,MaxSp,Attack = upgrade(MaxHp,MaxSp,Attack)
    #LAB_PROJECT4.draw_window(MaxHp,MaxSp,5,150,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
    while V == False:
        Boss_IMAGE, Boss_IMAGE2 = LAB_PROJECT4.chooseboss(4)
        MaxHp , MaxSp, Attack,V = LAB_PROJECT4.main('Armstrong' , 300 , 1.3, MaxHp , MaxSp, Attack , Boss_IMAGE, Boss_IMAGE2)
    V = False
    print("Welcome Back Hero")
    sleep(1)
    print("I see you defeated Armstrong")
    sleep(1)
    print("Sadly we have got no answers out of him")
    sleep(1)
    print("But rest for now, tomorrow is a new day and we hope to finally find the answers we need")
    sleep(1)
    quit()
    
