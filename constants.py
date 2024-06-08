AVAILABLE_TICKETS = 8
BREAKFAST = ['pasta']
AVAILABLE_RECIPES = BREAKFAST
UPGRADE_DISH = True
UPGRADE_TRASH = True



# bbox = (left_x, top_y, right_x, bot_y)
WINDOW_BOX = bbox = (0, 0, 1920, 1040)
ORDER_BOX = bbox= (0, 60, 420, 860)
TICKET_TITLE_BOX = bbox= (445, 813, 1515, 873)
TICKET_TEXT_BOX = bbox= (445, 875, 1515, 990)
FOOD_BOX = bbox = (400, 200, 1210, 800)
BUTTON_BOX = bbox = (1300, 155, 1850, 500)
TICKET_NUM_1 = bbox = (60, 130, 410, 210)
TICKET_NUM_2 = bbox = (60, 210, 410, 290)
TICKET_NUM_3 = bbox = (60, 290, 410, 370)
TICKETS_ORDER_BOX = (
    [(60, 130 + i * 85, 410, 210 + i*85) for i in range(AVAILABLE_TICKETS)])
TICKETS_NUM_BOX = (
    [(60, 130 + i * 85, 125, 210 + i*85) for i in range(AVAILABLE_TICKETS)])
COOK_NUM_BOX = (
    [(340, 130 + i * 85, 410, 210 + i*85) for i in range(AVAILABLE_TICKETS)])
OUTLINE_BOX = [(407, 130 + i * 85, 408, 150 + i*85) for i in range(AVAILABLE_TICKETS)]

AVAIALABLE_ORDER_RGB = (255, 255, 255)
ORDER_COOKED_RGB = [(255, 255, 64), (169, 102, 64), (216, 200, 57), (242, 242, 61), (237, 237, 63), 
                    (234, 233, 65), (248, 247, 67), (246, 245, 68), (246, 246, 68),
                    (124, 122, 35), (125, 123, 35), (125, 124, 35), (126, 125, 36), (126, 126, 37)]
ORDER_PHASE2_RGB = [(95, 229, 229), (96, 224, 225), (96, 221, 221), (97, 220, 221), (60, 135, 136),
                    (106, 255, 255), (106, 252, 252), (107, 246, 247), (107, 245, 245)]

# All recipes
#Single phase
SOPAPILLAS = 'sopapillas'
CORNDOG = 'corndog'
PRETZEL = 'pretzel'
BEER = 'beer'
FRIED_CHICKEN = 'friedChicken'
SODA = 'soda'
FRIES = 'fries'
SALAD = 'salad'
ICE_CREAM = 'iceCream'
LASAGNA = 'lasagna'
FISH = 'fish'
CHICKEN = 'chicken'
WINE = 'wine'
PIZZA = 'pizza'
STEAK = 'steak'
SOUP = 'soup'
COFFEE = 'coffee'
HASHBROWN = 'hashBrown'
BREAKWICH = 'breakwich'
SUSHI = 'sushi'
FRIED_RICE = 'friedRice'
BANANAS = 'bananas'
KABOB = 'kabob'
ENCHILADA = 'enchilada'
# Multi phase
POTATO = 'potato'
NACHOS = 'nachos'
PASTA = 'pasta'
BURGER = 'burger'
PANCAKE ='pancake'
LOBSTER = 'lobster'