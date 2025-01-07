import random, time
from sys import exit

import pygame.time

from Fish import *
from pygame import mixer
pygame.init()
mixer.init()


# Title text
title_font = pygame.font.Font("Retro Gaming.ttf", 75)
title_surface = title_font.render('FISHING FRENZY', False, 'peachpuff4')
title_rect = title_surface.get_rect(midtop=(400, 60))

enter_font = pygame.font.Font("Retro Gaming.ttf", 50)
enter_surface = enter_font.render('Press [Enter] to Begin', False, 'grey29')
enter_rect = enter_surface.get_rect(midbottom=(400, 350))


# Various variables
enter_key = 0
title_variable = True
fishing = False


# Backgrounds/other images
ocean_background = pygame.image.load("Images\\Miscellaneous\\Ocean-Background.png")
boat_graphic = pygame.image.load("Images\\Miscellaneous\\Boat.png")
bottom_bar = pygame.image.load("Images\\Miscellaneous\\Bottom-Bar.png")


def background_display():
    screen.blit(ocean_background, (0, 0))
    screen.blit(boat_graphic, (0, 0))
    screen.blit(bottom_bar, (0, 0))
    screen.blit(bar_surface, bar_rect)


# Fishing animation
fishing_rod_1 = pygame.image.load("Images\\Miscellaneous\\Fishing_Rod_1.png")
fishing_rod_2 = pygame.image.load("Images\\Miscellaneous\\Fishing_Rod_2.png")
fishing_rod_3 = pygame.image.load("Images\\Miscellaneous\\Fishing_Rod_3.png")
fishing_animation = [fishing_rod_1, fishing_rod_2, fishing_rod_3]


# Fish list
fish = ["Bass", "Yellowfin Tuna", "Red Drum", "Dolphinfish", "Sunfish", "Rainbow Trout", "Pike", "Shark", "Octopus", "Trash"]
fish_weighting = [10, 6, 8, 5, 8, 7, 10, 2, 1, 9]


# Functions
def go_fish():
    chosen_fish = random.choices(fish, weights=fish_weighting, k=1)
    return chosen_fish

fishing_timer_start = 2
fishing_timer_stop = 9
    
# Caught fish text
fish_text_font = pygame.font.Font("Retro Gaming.ttf", 20)


# Bar display
bar_font = pygame.font.Font("Retro Gaming.ttf", 25)
bar_surface = bar_font.render('[SPACE] to fish | [I] for inventory | [T] for store', False, 'lightsalmon4')
bar_rect = bar_surface.get_rect(midbottom=(400, 490))


# Inventory variables
player_inventory = {
    "bass amount":           0,
    "yellowfin tuna amount": 0,
    "red drum amount":       0,
    "dolphinfish amount":    0,
    "sunfish amount":        0,
    "rainbow trout amount":  0,
    "pike amount":           0,
    "shark amount":          0,
    "octopus amount":        0,
    "trash amount":          0
}

player_inventory_two = ["bass amount", "yellowfin tuna amount", "red drum amount", "dolphinfish amount", "sunfish amount", "rainbow trout amount", "pike amount", "shark amount", "octopus amount", "trash amount"]


# Selling
fish_price = {
    "bass price":            9,
    "yellowfin tuna price":  55,
    "red drum price":        24,
    "dolphinfish price":     68,
    "sunfish price":         41,
    "rainbow trout price":   36,
    "pike price":            11,
    "shark price":           86,
    "octopus price":         100,
    "trash price":           5
}

store_inventory = ["trash be-gone", "shark bait", "octopi bait", "faster fishing", "profit increaser", "multi-fish net"]
store_prices = {
    "trash be-gone":    85,
    "shark bait":       100,
    "octopi bait":      150,
    "faster fishing":   300,
    "profit increaser": 500,
    "multi-fish net":   1000
}

money = 0
fish_costs = ["bass price", "yellowfin tuna price", "red drum price", "dolphinfish price", "sunfish price", "rainbow trout price", "pike price", "shark price", "octopus price", "trash price"]

inventory_title_font = pygame.font.Font("Retro Gaming.ttf", 30)
inventory_title_surface = inventory_title_font.render('INVENTORY', False, 'chocolate4')
inventory_title_rect = inventory_title_surface.get_rect(midtop=(400, 30))

store_title_font = pygame.font.Font("Retro Gaming.ttf", 30)
store_title_surface = store_title_font.render('STORE', False, 'chocolate4')
store_title_rect = store_title_surface.get_rect(midtop=(400, 30))

money_font = pygame.font.Font("Retro Gaming.ttf", 20)


# Selection box in inventory variables
c = 51
d = 109

inventory_background = pygame.image.load("Images\\Miscellaneous\\Inventory-Background.png")
inventory_box = pygame.image.load("Images\\Miscellaneous\\Rectangle.png")
inventory_rectangle = inventory_box.get_rect(center=(c, d))

store_x_r = False
store_x_l = False
store_y_d = False
store_y_u = False

e = -223
f = -72


store_background = pygame.image.load("Images\\Miscellaneous\\Store-Background.png")
store_box = pygame.image.load("Images\\Miscellaneous\\Store-Rectangle.png")
store_rectangle = store_box.get_rect(center=(e, f))

inventory_x_r = False
inventory_x_l = False
inventory_y_d = False
inventory_y_u = False

# Other Various inventory stuff
inventory_text_font = pygame.font.Font("Retro Gaming.ttf", 17)

store_font = pygame.font.Font("Retro Gaming.ttf", 25)
store_surface = store_font.render('Press [S] to sell', False, 'chocolate4')
store_rect = store_surface.get_rect(midtop=(400, 65))

inventory_font = pygame.font.Font("Retro Gaming.ttf", 25)
inventory_surface = inventory_font.render('Press [S] to buy', False, 'chocolate4')
inventory_rect = inventory_surface.get_rect(midtop=(400, 65))

added_fish_amount = 1

selling = False
buying = False
just_sold = False
just_bought = False
fish_num = 0
store_num = 0
timer = 0
lost_money_surface = ""
lost_money_rect = ""
gained_money_surface = ""
gained_money_rect = ""
not_applicable = False
current_price = 0
current_selling = 0
selling_money = 0




# Music
mixer.music.load("Ocean Audio.mp3")
pygame.mixer.music.play(-1)


# Set the screen dimensions
screen = pygame.display.set_mode((800, 500))

# Window caption and icon
pygame.display.set_caption("Fishing Frenzy")

window_icon = pygame.image.load("Images\\Fish\\Bass.png")
pygame.display.set_icon(window_icon)

# Maximum frame rate
clock = pygame.time.Clock()

# Inventory toggle
inventory_open = False
store_open = False

# Achievements

class Achievement:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.background = pygame.image.load("Images\\Miscellaneous\\Achievement_Background.png")
        self.titleFont = pygame.font.Font("Retro Gaming.ttf", 17)
        self.descriptionFont = pygame.font.Font("Retro Gaming.ttf", 14)
        # self.achievementUnlockedFont = pygame.font.Font("Retro Gaming.ttf", 15)
        self.status = False

    def displayAchievement(self, display):
        achievement_title_surface = self.titleFont.render(self.name, False, "chocolate4")
        achievement_title_rect = achievement_title_surface.get_rect(topleft=(520, 408))
        achievement_description_surface = self.descriptionFont.render(self.description, False, "darkgreen")
        achievement_description_rect = achievement_description_surface.get_rect(topleft=(522, 428))
        achievement_unlocked_surface = self.titleFont.render("Achievement Unlocked!", False, "tomato4")
        achievement_unlocked_rect = achievement_unlocked_surface.get_rect(topleft=(520, 388))

        display.blit(self.background, (0, 0))
        display.blit(achievement_title_surface, achievement_title_rect)
        display.blit(achievement_description_surface, achievement_description_rect)
        screen.blit(achievement_unlocked_surface, achievement_unlocked_rect)


eliteUpgrader = Achievement("Elite Upgrader", "Buy every upgrade")
thousandaire = Achievement("Thousand-aire", "Earn $1000")
luxuryEquipment = Achievement("Luxury Equipment", "Buy the best equipment")
seasonedPro = Achievement("Seasoned Pro", "Spend 10+ minutes in-game")
masterFisher = Achievement("Master Fisher", "Catch all types of fish")

master_fisher_list = []
upgrader_counter = 0
display_timer_check = False
display_timer = 0



# Run the program in a continuous loop
run = True

while run:
    achievement_timer = pygame.time.get_ticks()

    screen.fill((133, 181, 237))
    screen.blit(ocean_background, (0, 0))

    # Get key inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                if title_variable:
                    enter_key = 1

            elif event.key == pygame.K_SPACE:
                if enter_key == 1 and inventory_open is False and store_open is False:
                    fishing = True

            elif event.key == pygame.K_i:
                if fishing is False and enter_key == 1 and store_open is False:
                    inventory_open = not inventory_open

            elif event.key == pygame.K_t:
                if fishing is False and enter_key == 1 and inventory_open is False:
                    store_open = not store_open

            elif event.key == pygame.K_RIGHT:
                if inventory_open:
                    store_x_r = True
                elif store_open:
                    inventory_x_r = True
            elif event.key == pygame.K_LEFT:
                if inventory_open:
                    store_x_l = True
                elif store_open:
                    inventory_x_l = True
            elif event.key == pygame.K_DOWN:
                if inventory_open:
                    store_y_d = True
                elif store_open:
                    inventory_y_d = True
            elif event.key == pygame.K_UP:
                if inventory_open:
                    store_y_u = True
                elif store_open:
                    inventory_y_u = True
            elif event.key == pygame.K_s:
                if inventory_open:
                    selling = True
                elif store_open:
                    buying = True

    # Title opening
    if title_variable is True and enter_key == 0:
        screen.blit(title_surface, title_rect)
        screen.blit(enter_surface, enter_rect)

    # Gets rid of opening title
    if enter_key == 1:
        background_display()

    # Fishing
    if fishing:

        # Fishing rod animation
        for frame in range(0, 3):
            background_display()
            screen.blit(fishing_animation[frame], (0, 0))
            pygame.display.update()

        # Random time
        fishing_timer = random.randrange(fishing_timer_start, fishing_timer_stop)
        time.sleep(fishing_timer)

        current_fish = go_fish()
        current_fish = str(current_fish).strip("[']")

        # for master fisher achievement
        if current_fish not in master_fisher_list:
            master_fisher_list.append(current_fish)

        if current_fish == "Bass":
            screen.blit(bass_fish, (300, 40))
            player_inventory["bass amount"] += added_fish_amount
        elif current_fish == "Yellowfin Tuna":
            screen.blit(yellowfintuna_fish, (300, 40))
            player_inventory["yellowfin tuna amount"] += added_fish_amount
        elif current_fish == "Red Drum":
            screen.blit(reddrum_fish, (300, 40))
            player_inventory["red drum amount"] += added_fish_amount
        elif current_fish == "Dolphinfish":
            screen.blit(dolphinfish_fish, (300, 40))
            player_inventory["dolphinfish amount"] += added_fish_amount
        elif current_fish == "Sunfish":
            screen.blit(sunfish_fish, (300, 40))
            player_inventory["sunfish amount"] += added_fish_amount
        elif current_fish == "Rainbow Trout":
            screen.blit(rainbowtrout_fish, (300, 40))
            player_inventory["rainbow trout amount"] += added_fish_amount
        elif current_fish == "Pike":
            screen.blit(pike_fish, (300, 40))
            player_inventory["pike amount"] += added_fish_amount
        elif current_fish == "Shark":
            screen.blit(shark_fish, (300, 30))
            player_inventory["shark amount"] += added_fish_amount
        elif current_fish == "Octopus":
            screen.blit(octopus_fish, (300, 30))
            player_inventory["octopus amount"] += added_fish_amount
        elif current_fish == "Trash":
            screen.blit(trash_fish, (300, 45))
            player_inventory["trash amount"] += added_fish_amount

        fish_text_surface = fish_text_font.render('You caught ' + current_fish + "!", False, 'lightsalmon4')
        fish_text_rect = fish_text_surface.get_rect(midtop=(400, 20))

        screen.blit(fish_text_surface, fish_text_rect)
        pygame.display.update()

        time.sleep(1.25)

        fishing = False

    # Inventory
    if inventory_open:
        fishing = False
        screen.blit(inventory_background, (0, 0))
        screen.blit(inventory_title_surface, inventory_title_rect)
        screen.blit(store_surface, store_rect)

        money_surface = money_font.render('$' + str(money), False, 'chocolate4')
        money_rect = money_surface.get_rect(topright=(735, 30))
        screen.blit(money_surface, money_rect)

        # Important variables
        i = 0
        a = 148
        b = 148

        # Fish amount numbers
        for x in player_inventory_two:
            i = i + 1
            if i <= 5:
                inventory_fish_surface = inventory_text_font.render(str(player_inventory[x]), False, 'lightsalmon4')
                inventory_fish_rect = inventory_fish_surface.get_rect(topright=(a, 198))
                screen.blit(inventory_fish_surface, inventory_fish_rect)
                a = a + 147

            elif i > 5:
                inventory_fish_surface = inventory_text_font.render(str(player_inventory[x]), False, 'lightsalmon4')
                inventory_fish_rect = inventory_fish_surface.get_rect(topright=(b, 338))
                screen.blit(inventory_fish_surface, inventory_fish_rect)
                b = b + 147

        # Moving Rectangle
        if store_x_l:
            c -= 147
            store_x_l = False
            fish_num -= 1

        elif store_x_r:
            c += 147
            store_x_r = False
            fish_num += 1

        elif store_y_d:
            d += 140
            store_y_d = False
            fish_num += 5

        elif store_y_u:
            d -= 140
            store_y_u = False
            fish_num -= 5

        if c < 51:
            c += 147
            fish_num += 1
        elif c > 750:
            c -= 147
            fish_num -= 1

        if d < 109:
            d += 140
            fish_num += 5
        elif d > 250:
            d -= 140
            fish_num -= 5

        inventory_rectangle.x = c
        inventory_rectangle.y = d
        screen.blit(inventory_box, inventory_rectangle)

        # Selling
        if selling:
            current_selling = player_inventory_two[fish_num]
            current_price = fish_costs[fish_num]
            added_money = player_inventory[current_selling] * fish_price[current_price]
            money = money + added_money
            selling_money = player_inventory[current_selling]


            gained_money_surface = money_font.render(f"+ ${added_money}", False, "chocolate4")
            gained_money_rect = gained_money_surface.get_rect(topright=(money_rect.left - 18, 30))

            just_sold = True
            timer = pygame.time.get_ticks()
            player_inventory[current_selling] = 0
            selling = False

        if selling_money != 0:
            if just_sold and pygame.time.get_ticks() - timer >= 2000:
                just_sold = False
            elif just_sold:
                screen.blit(gained_money_surface, gained_money_rect)

    # Store
    elif store_open:
        fishing = False
        screen.blit(store_background, (0, 0))
        screen.blit(store_title_surface, store_title_rect)
        screen.blit(inventory_surface, inventory_rect)

        money_surface = money_font.render('$' + str(money), False, 'chocolate4')
        money_rect = money_surface.get_rect(topright=(735, 30))
        screen.blit(money_surface, money_rect)

        g = 236
        h = 236
        j = 0

        # Displaying the item costs
        for x in store_inventory:
            j += 1
            if j <= 3:
                if store_prices[x] == "N/A":
                    store_price_surface = inventory_text_font.render(store_prices[x], False, 'lightsalmon4')
                else:
                    store_price_surface = inventory_text_font.render(f"${store_prices[x]}", False, 'lightsalmon4')
                store_price_rect = store_price_surface.get_rect(topright=(g, 220))
                screen.blit(store_price_surface, store_price_rect)
                g += 223
            elif j > 3:
                if store_prices[x] == "N/A":
                    store_price_surface = inventory_text_font.render(store_prices[x], False, 'lightsalmon4')
                else:
                    store_price_surface = inventory_text_font.render(f"${store_prices[x]}", False, 'lightsalmon4')
                store_price_rect = store_price_surface.get_rect(topright=(h, 386))
                screen.blit(store_price_surface, store_price_rect)
                h += 223

        if inventory_x_l:
            e -= 223
            store_num -= 1
            inventory_x_l = False

        elif inventory_x_r:
            e += 223
            store_num += 1
            inventory_x_r = False

        elif inventory_y_d:
            f += 165
            store_num += 3
            inventory_y_d = False

        elif inventory_y_u:
            f -= 165
            store_num -= 3
            inventory_y_u = False

        if e < -223:
            e += 223
            store_num += 1
        elif e > 400:
            e -= 223
            store_num -= 1

        if f < -72:
            f += 165
            store_num += 3
        elif f > 250:
            f -= 165
            store_num -= 3

        store_rectangle.x = e
        store_rectangle.y = f
        screen.blit(store_box, store_rectangle)


        if buying:
            current_buying = store_inventory[store_num]
            current_price = store_prices[current_buying]
            lost_money_surface = money_font.render(f"- ${current_price}", False, "chocolate4")

            if current_price == "N/A":
                not_applicable = True

            if store_num == 0 and current_price != "N/A" and money >= current_price:
                fish_weighting[9] = 1
                money -= current_price
                store_prices[current_buying] = "N/A"
                just_bought = True
            elif store_num == 1 and current_price != "N/A" and money >= current_price:
                fish_weighting[7] = 6
                money -= current_price
                store_prices[current_buying] = "N/A"
                just_bought = True
            elif store_num == 2 and current_price != "N/A" and money >= current_price:
                fish_weighting[8] = 5
                money -= current_price
                store_prices[current_buying] = "N/A"
                just_bought = True
            elif store_num == 3 and current_price != "N/A" and money >= current_price:
                fishing_timer_start = 1
                fishing_timer_stop = 4
                money -= current_price
                store_prices[current_buying] = "N/A"
                just_bought = True
            elif store_num == 4 and current_price != "N/A" and money >= current_price:
                for x in range(len(fish_costs)):
                    fish_price[fish_costs[x]] += 40
                money -= current_price
                store_prices[current_buying] = "N/A"
                just_bought = True
            elif store_num == 5 and current_price != "N/A" and money >= current_price:
                added_fish_amount += random.randint(1, 3)
                money -= current_price
                store_prices[current_buying] = "N/A"
                just_bought = True

            lost_money_rect = lost_money_surface.get_rect(topright=(money_rect.left - 18, 30))

            timer = pygame.time.get_ticks()

            buying = False

        if just_bought and pygame.time.get_ticks() - timer >= 1500 and not_applicable is False:
            just_bought = False
        elif just_bought and not_applicable is False:
            screen.blit(lost_money_surface, lost_money_rect)

        not_applicable = False

    # Achievements
    # elite upgrader:
    for x in range(6):
        store_item = store_inventory[x]
        if store_prices[store_item] == "N/A":
            upgrader_counter += 1

    if upgrader_counter >= 1 and display_timer_check is False and eliteUpgrader.status is False:
        display_timer = pygame.time.get_ticks()
        display_timer_check = True

    if upgrader_counter >= 1 and eliteUpgrader.status is False:
        if pygame.time.get_ticks() - display_timer >= 4000:
            display_timer_check = False
            eliteUpgrader.status = True
        else:
            eliteUpgrader.displayAchievement(screen)
    elif upgrader_counter > 1 and eliteUpgrader.status is False:
        upgrader_counter = 0

    # thousandaire:
    if money >= 1000 and display_timer_check is False and thousandaire.status is False:
        display_timer = pygame.time.get_ticks()
        display_timer_check = True
    if thousandaire.status is False and money >= 1000:
        if pygame.time.get_ticks() - display_timer >= 4000:
            display_timer_check = False
            thousandaire.status = True
        else:
            thousandaire.displayAchievement(screen)


    # luxury equipment:
    if store_prices["multi-fish net"] == "N/A" and display_timer_check is False and luxuryEquipment.status is False:
        display_timer = pygame.time.get_ticks()
        display_timer_check = True
    if luxuryEquipment.status is False and store_prices["multi-fish net"] == "N/A":
        if pygame.time.get_ticks() - display_timer >= 4000:
            display_timer_check = False
            luxuryEquipment.status = True
        else:
            luxuryEquipment.displayAchievement(screen)

    # seasoned pro:
    if achievement_timer >= 600000 and display_timer_check is False and seasonedPro.status is False:
        display_timer = pygame.time.get_ticks()
        display_timer_check = True
    if seasonedPro.status is False and achievement_timer >= 600000:
        if pygame.time.get_ticks() - display_timer >= 4000:
            display_timer_check = False
            seasonedPro.status = True
        else:
            seasonedPro.displayAchievement(screen)


    # master fisher:
    if len(master_fisher_list) == 10:
        masterFisher.displayAchievement(screen)
        master_fisher_list += 1


    # Maximum frame rate pt. 2
    clock.tick(60)

    # Refreshes the screen
    pygame.display.flip()


# Exits the game
pygame.quit()
exit()
