
AVAILABLE_TICKETS = 8

# bbox = (left_x, bot_y, right_x, top_y)
WINDOW_BOX = bbox = (0, 0, 1920, 1040)
ORDER_BOX = bbox= (0, 60, 420, 860)
TICKET_TITLE_BOX = bbox= (430, 810, 1520, 870)
TICKET_TEXT_BOX = bbox= (440, 875, 1515, 995)
FOOD_BOX = bbox = (400, 200, 1210, 800)
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
ORDER_COOKED_RGB = [(255, 255, 64), (169, 102, 64)]
# [169 102  57]
# 255, 255, 64
# 197 369 453 536 789
