import pygame
from engi1020.arduino.api import*
import os # os is the oberating system and it used to help find the path to the image
import Buttons
import random
from time import sleep
from pygame import mixer
pygame.init()
pygame.font.init()
mixer.music.load(os.path.join("Assets","MT.mp3"))
mixer.music.play(-1)
WIDTH, HEIGHT = 1800, 1000
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('EXPEDETION TO THE LAND OF THE DEAD!')#this changes the name of the window or the name caption 
WHITE=(225,225,225)
GREEN=(0,225,0)
RED=(225,0,0)
BLUE=(0,0,255)
Button_W, Button_H=300,150
FPS=60#this is used to define how quiqly the game will update at
B_WIDTH,B_HEIGHT=1800,1000
Boss1_WIDTH,Boss1_HEIGHT=300,400
B_IMAGE= pygame.image.load(os.path.join('Assets','B_K.jpg'))
B_IMAGE= pygame.transform.scale(B_IMAGE,(B_WIDTH,B_HEIGHT))#this is to resize the the image
STATUS_FONT = pygame.font.SysFont("comicsans",40)
lose_FONT = pygame.font.SysFont("algerian",100)
Victory_FONT = pygame.font.SysFont("algerian",60)
def chooseboss(Choice):
    if Choice == 1:
        Boss_IMAGE2= pygame.image.load(os.path.join('Assets','Boss1_2.png'))
        Boss_IMAGE2=pygame.transform.scale(Boss_IMAGE2,(900,Boss1_HEIGHT))
        Boss_IMAGE= pygame.image.load(os.path.join('Assets','Boss1.png'))
        Boss_IMAGE=pygame.transform.scale(Boss_IMAGE,(Boss1_WIDTH,Boss1_HEIGHT))
    elif Choice == 2:
        Boss_IMAGE2= pygame.image.load(os.path.join('Assets','Boss2_2.webp'))
        Boss_IMAGE2=pygame.transform.flip(pygame.transform.scale(Boss_IMAGE2,(400,400)),True,False)
        Boss_IMAGE= pygame.image.load(os.path.join('Assets','Boss2_1.webp'))
        Boss_IMAGE=pygame.transform.flip(pygame.transform.scale(Boss_IMAGE,(400,400)),True,False)
    elif Choice == 3:
        Boss_IMAGE2= pygame.image.load(os.path.join('Assets','Boss3_2.png'))
        Boss_IMAGE2=pygame.transform.scale(Boss_IMAGE2,(300,400))
        Boss_IMAGE= pygame.image.load(os.path.join('Assets','Boss3_1.webp'))
        Boss_IMAGE=pygame.transform.scale(Boss_IMAGE,(400,400))
    elif Choice == 4:
        Boss_IMAGE2= pygame.image.load(os.path.join('Assets','Boss4_2.png'))
        Boss_IMAGE2=pygame.transform.scale(Boss_IMAGE2,(300,400))
        Boss_IMAGE= pygame.image.load(os.path.join('Assets','Boss4_1.png'))
        Boss_IMAGE=pygame.transform.scale(Boss_IMAGE,(400,400))
    return Boss_IMAGE, Boss_IMAGE2
# Death animation insert and size 
Death= pygame.image.load(os.path.join('Assets','Death.png'))
Death=pygame.transform.scale(Death,(Boss1_WIDTH,Boss1_HEIGHT))
#hero states steady and attack
sama_width, sama_height=400,500
Hero_IMAGE= pygame.image.load(os.path.join('Assets','Sama.webp'))
Hero_IMAGE=pygame.transform.flip(pygame.transform.scale(Hero_IMAGE,(sama_width, sama_height)),True,False)
Hero_IMAGE2= pygame.image.load(os.path.join('Assets','P1 2.webp'))
Hero_IMAGE2=pygame.transform.flip(pygame.transform.scale(Hero_IMAGE2,(sama_width, sama_height)),True,False)
#button images insert and size
LIGHT_IMAGE= pygame.image.load(os.path.join('Assets','Light.png'))
LIGHT_IMAGE=pygame.transform.scale(LIGHT_IMAGE,(Button_W, Button_H))

HEAVY_IMAGE= pygame.image.load(os.path.join('Assets','Heavy.png'))
HEAVY_IMAGE=pygame.transform.scale(HEAVY_IMAGE,(Button_W, Button_H))

HEAL_IMAGE= pygame.image.load(os.path.join('Assets','Heal.png'))
HEAL_IMAGE=pygame.transform.scale(HEAL_IMAGE,(Button_W, Button_H))

RECH_IMAGE= pygame.image.load(os.path.join('Assets','Recharge.png'))
RECH_IMAGE=pygame.transform.scale(RECH_IMAGE,(Button_W, Button_H))
#inserting background music

# drawing initial window 
def draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2):
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Boss_IMAGE,(300,250))
    WIN.blit(Hero_IMAGE,(900,150))
    HHT = STATUS_FONT.render(
        "Health: " + str(hero_health), 1, WHITE)
    HST = STATUS_FONT.render(
        "Stamina: " + str(hero_stamina), 1, WHITE)
    HPo = STATUS_FONT.render(
        "Health Potions: " + str(health_potions), 1, WHITE)
    EHT = STATUS_FONT.render(
        "Health: " + str(enemy_health), 1, WHITE)
    WIN.blit(HHT, (WIDTH - HHT.get_width() - 20, 20))
    WIN.blit(HST, (WIDTH - HST.get_width() - 20, 70))
    WIN.blit(HPo, (WIDTH - HPo.get_width() - 20, 120))
    WIN.blit(EHT, (20, 20))
    pygame.display.update()#this is to ubdate the changes
#draiwng window with buttons
def redrawWindow(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2):
    LIGHT=Buttons.Button(50,800,LIGHT_IMAGE,1)
    HEAVY=Buttons.Button(500,800,HEAVY_IMAGE,1)
    HEAL=Buttons.Button(950,800,HEAL_IMAGE,1)
    RECH=Buttons.Button(1400,800,RECH_IMAGE,1)
    LIGHT.draw(B_IMAGE)
    HEAVY.draw(B_IMAGE)
    HEAL.draw(B_IMAGE)
    RECH.draw(B_IMAGE)
    HHT = STATUS_FONT.render(
        "Health: " + str(hero_health), 1, WHITE)
    HST = STATUS_FONT.render(
        "Stamina: " + str(hero_stamina), 1, WHITE)
    HPo = STATUS_FONT.render(
        "Health Potions: " + str(health_potions), 1, WHITE)
    EHT = STATUS_FONT.render(
        "Health: " + str(enemy_health), 1, WHITE)
    WIN.blit(HHT, (WIDTH - HHT.get_width() - 20, 20))
    WIN.blit(HST, (WIDTH - HST.get_width() - 20, 70))
    WIN.blit(HPo, (WIDTH - HPo.get_width() - 20, 120))
    WIN.blit(EHT, (20, 20))
    pygame.display.update()
#window with hero attacking enemy 
def heroAttackAnimation(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2):
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Boss_IMAGE,(300,250))
    WIN.blit(Hero_IMAGE2,(450,150))
    HHT = STATUS_FONT.render(
        "Health: " + str(hero_health), 1, WHITE)
    HST = STATUS_FONT.render(
        "Stamina: " + str(hero_stamina), 1, WHITE)
    HPo = STATUS_FONT.render(
        "Health Potions: " + str(health_potions), 1, WHITE)
    EHT = STATUS_FONT.render(
        "Health: " + str(enemy_health), 1, WHITE)
    WIN.blit(HHT, (WIDTH - HHT.get_width() - 20, 20))
    WIN.blit(HST, (WIDTH - HST.get_width() - 20, 70))
    WIN.blit(HPo, (WIDTH - HPo.get_width() - 20, 120))
    WIN.blit(EHT, (20, 20))
    pygame.display.update()
    Sound= mixer.Sound(os.path.join("Assets","Electricty.mp3"))
    Sound.play()
    sleep(1)
    draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
#window with hero's death
def heroDeath(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2):
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Boss_IMAGE,(300,250))
    WIN.blit(Death,(1000,300))
    Sound= mixer.Sound(os.path.join("Assets","Death.mp3"))
    Sound.play()
    HHT = STATUS_FONT.render(
        "Health: " + str(hero_health), 1, WHITE)
    HST = STATUS_FONT.render(
        "Stamina: " + str(hero_stamina), 1, WHITE)
    HPo = STATUS_FONT.render(
        "Health Potions: " + str(health_potions), 1, WHITE)
    EHT = STATUS_FONT.render(
        "Health: " + str(enemy_health), 1, WHITE)
    WIN.blit(HHT, (WIDTH - HHT.get_width() - 20, 20))
    WIN.blit(HST, (WIDTH - HST.get_width() - 20, 70))
    WIN.blit(HPo, (WIDTH - HPo.get_width() - 20, 120))
    WIN.blit(EHT, (20, 20)) 
    pygame.display.update()
    sleep(1)
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Boss_IMAGE,(300,250)) 
    pygame.display.update()
#window with enemy's death
def enemyDeath(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2):
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Hero_IMAGE,(900,150))
    WIN.blit(Death,(300,250))
    Sound= mixer.Sound(os.path.join("Assets","Death.mp3"))
    Sound.play()
    HHT = STATUS_FONT.render(
        "Health: " + str(hero_health), 1, WHITE)
    HST = STATUS_FONT.render(
        "Stamina: " + str(hero_stamina), 1, WHITE)
    HPo = STATUS_FONT.render(
        "Health Potions: " + str(health_potions), 1, WHITE)
    EHT = STATUS_FONT.render(
        "Health: " + str(enemy_health), 1, WHITE)
    WIN.blit(HHT, (WIDTH - HHT.get_width() - 20, 20))
    WIN.blit(HST, (WIDTH - HST.get_width() - 20, 70))
    WIN.blit(HPo, (WIDTH - HPo.get_width() - 20, 120))
    WIN.blit(EHT, (20, 20))
    pygame.display.update()
    sleep(1)
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Hero_IMAGE,(900,150))
    pygame.display.update()
#enemy's attack information
def enemyAttackAnimation(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2):
    WIN.fill(WHITE)# this fill the screnn with color the color is in rgb (red,green,blue)
    WIN.blit(B_IMAGE,(0,0))#(300,100) is the location of the image on the screen#this draw the a surface on a screen, an image or atext is a surface and needs blit
    WIN.blit(Boss_IMAGE2,(300,250))
    WIN.blit(Hero_IMAGE,(900,150))
    HHT = STATUS_FONT.render(
        "Health: " + str(hero_health), 1, WHITE)
    HST = STATUS_FONT.render(
        "Stamina: " + str(hero_stamina), 1, WHITE)
    HPo = STATUS_FONT.render(
        "Health Potions: " + str(health_potions), 1, WHITE)
    EHT = STATUS_FONT.render(
        "Health: " + str(enemy_health), 1, WHITE)
    WIN.blit(HHT, (WIDTH - HHT.get_width() - 20, 20))
    WIN.blit(HST, (WIDTH - HST.get_width() - 20, 70))
    WIN.blit(HPo, (WIDTH - HPo.get_width() - 20, 120))
    WIN.blit(EHT, (20, 20))
    Sound= mixer.Sound(os.path.join("Assets","Punch.mp3"))
    Sound.play()
    pygame.display.update()
    sleep(1)
    draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
# main game starts here
def main(enemy_name , enemy_health , Multi_damage, MaxHp , MaxSp, Attack, Boss_IMAGE, Boss_IMAGE2 ):
    clock = pygame.time.Clock()
    hero_health = MaxHp
    hero_stamina = MaxSp
    health_potions = 5
    Multi_damage_hero = Attack
    damage_taken = 0
    count = 0
    draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
    redrawWindow(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
    LIGHT=Buttons.Button(50,800,LIGHT_IMAGE,1)
    HEAVY=Buttons.Button(500,800,HEAVY_IMAGE,1)
    HEAL=Buttons.Button(950,800,HEAL_IMAGE,1)
    RECH=Buttons.Button(1400,800,RECH_IMAGE,1)
    run=True
    t1 = 0
    t2 = 0 
    print(f'Hp: {hero_health}/ Sp: {hero_stamina}/ potions: {health_potions}' )
    print(f' Enemy Hp: {enemy_health}')
    while run:
        clock.tick(FPS) #this will control the speed of this while loop 60 times per second/ this clock.tick is to insure that there is you donot go over the sherhold  
        draw_window(MaxHp,MaxSp,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
        #redrawWindow()
        while hero_health > 0 and enemy_health > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # this is to quit the window without having to force quit 
                    run=False
                    draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)    
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if LIGHT.draw(WIN):
                            if hero_stamina < 30:
                                print("Not enough stamina")
                                Stamina_Low = STATUS_FONT.render("Not enough stamina", 1, BLUE)
                                WIN.blit(Stamina_Low, (600, 150))
                                pygame.display.update()
                                sleep(2)
                                draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                            else:
                                enemy_health -= random.randint(15,25)*Attack
                                hero_stamina -= 30
                                t1 += 1
                                heroAttackAnimation(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                        elif HEAVY.draw(WIN):
                            if hero_stamina < 50:
                                    print("Not enough stamina")
                                    Stamina_Low = STATUS_FONT.render("Not enough stamina", 1, BLUE)
                                    WIN.blit(Stamina_Low, (600, 150))
                                    pygame.display.update()
                                    sleep(2)
                                    draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                            else:
                                enemy_health -= random.randint(45,70)*Attack
                                hero_stamina -= 50
                                t1 += 1
                                heroAttackAnimation(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                        elif HEAL.draw(WIN):
                            if health_potions > 0:
                                    hero_health += 30
                                    health_potions -= 1
                                    t1 += 1
                                    if hero_health > MaxHp:
                                        hero_health = MaxHp
                            else:
                                print(" You ran out of potions")
                                Potions_Low = STATUS_FONT.render("You ran out of potions", 1,RED)
                                WIN.blit(Potions_Low, (600, 150))
                                pygame.display.update()
                                sleep(2)
                                draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                        elif RECH.draw(WIN):
                            hero_stamina += 50
                            t1 += 1
                            if hero_stamina >= MaxSp:
                                hero_stamina = MaxSp                                
                        if enemy_health <= 0:
                            enemy_health = 0
                        if hero_health <= 0:
                            hero_health = 0
                        if t1 > t2 and enemy_health > 0:
                            sleep(0.1)
                            print(f'Hp: {hero_health}/ Sp: {hero_stamina}/ potions: {health_potions}' )
                            print(f' Enemy Hp : {enemy_health}')
                            damage_taken = random.randint(15,35)*Multi_damage
                            hero_health -= damage_taken
                            enemyAttackAnimation(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                            t2 += 1
                            
                        if hero_health < 25 and hero_health > 0:
                            digital_write(4, True)
                            BLEED1 = STATUS_FONT.render("Warning!!! health is low, hurry and patch your injury", 1, RED)
                            BLEED2 = STATUS_FONT.render("(Press Button till red alaram closes)", 1, RED)
                            WIN.blit(BLEED1, (430, 150))
                            WIN.blit(BLEED2,(530,200))
                            pygame.display.update()
                            sleep(2)
                            draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                            print("Warning!!! health is low, hurry and patch your injury (Press Button till red alaram closes)")
                            print("3..")
                            sleep(1)
                            print("2..")
                            sleep(1)
                            print("1..")
                            sleep(1)
                            
                            if digital_read(6):
                                digital_write(4, False)
                                print("Get back to the battle")
                                BLEED1 = STATUS_FONT.render("Get back to the battle", 1, GREEN)
                                WIN.blit(BLEED1, (700, 150))
                                pygame.display.update()
                                sleep(1)
                            elif digital_read(6) == False:
                                hero_health -= 5
                                print("You are bleeding")
                                BLEED1 = STATUS_FONT.render("You are bleeding", 1, RED)
                                WIN.blit(BLEED1, (700, 150))
                                pygame.display.update()
                                sleep(1)
                            draw_window(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                        #set hero or enemy health to zero if it becomes less than zero
                        if enemy_health <= 0:
                            enemy_health = 0

                        if hero_health <= 0:
                            hero_health = 0

                            print(f'Hp: {hero_health}/ Sp: {hero_stamina}/ potions: {health_potions}' )
                            print(f' Enemy Hp : {enemy_health}')

                #if statment to decide whether to congrat the player or inform them of lose depending on the levels result
                if enemy_health <= 0:
                    enemyDeath(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                    Victory = Victory_FONT.render(f"Congrats hero, {enemy_name} was defeated", 1, GREEN)
                    WIN.blit(Victory, (300, 150))
                    pygame.display.update()
                    print(f"Congrats hero, {enemy_name} was defeated")
                    sleep(1)
                    return (MaxHp , MaxSp, Attack, True)
                    #quit()
                    
                elif hero_health <= 0:
                    heroDeath(hero_health,hero_stamina,health_potions,enemy_health,B_IMAGE,Boss_IMAGE,Hero_IMAGE,LIGHT_IMAGE,HEAVY_IMAGE,HEAL_IMAGE,RECH_IMAGE,Hero_IMAGE2,Death,Boss_IMAGE2)
                    Lose = lose_FONT.render("Game Over", 1, RED)
                    WIN.blit(Lose, (570, 150))
                    Lose1 = lose_FONT.render("Try Again", 1, RED)
                    WIN.blit(Lose1, (650, 250))
                    pygame.display.update()
                    print("Game Over")
                    sleep(1)
                    return (MaxHp , MaxSp, Attack,False)
                    #quit()
                
    
    return (MaxHp , MaxSp, Attack)
    
    
    
'''if __name__=="__main__":
    Boss_IMAGE, Boss_IMAGE2 = chooseboss(2)
    main('Amoged' , 100 , 1, 100 , 100, 1, Boss_IMAGE, Boss_IMAGE2)'''