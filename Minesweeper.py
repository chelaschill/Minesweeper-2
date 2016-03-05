import pygame
import random
import time
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
YELLOW   = ( 255, 255,   0)
CYAN     = (   0, 255, 255)
GREEN    = (   0, 255,   0)
LGREEN   = ( 112, 255, 112)
RED      = ( 255,   0,   0)
GRAY1    = ( 150, 150, 150)
GRAY2    = ( 128, 128, 128)

# Initialize pygame
pygame.init()
size = [505, 505]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
width  = 20
height = 20
margin = 5
done6 = False
done = False
    #--------------------------------------------TITLE SCREEN--------------------------------------------------#
while done6 == False:
    difficultyLoop = False
    rect_x = 200
    rect_change_x = 2
    difficulty = 1
    while difficultyLoop == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                difficultyLoop = True
                done6 = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] > 106 and position[0] < 188 and position[1] > 324 and position[1] < 406:
                    difficultyLoop = True
                    done = False
                    difficulty = 8
                if position[0] > 212 and position[0] < 294 and position[1] > 324 and position[1] < 406:
                    difficultyLoop = True
                    done = False
                    difficulty = 6
                if position[0] > 316 and position[0] < 398 and position[1] > 324 and position[1] < 406:
                    difficultyLoop = True
                    done = False
                    difficulty = 5
        screen.fill(BLACK)
        font = pygame.font.Font(None, 18)
        text = font.render("Made by: Austin Ayers", True, BLACK)
        pygame.draw.ellipse(screen, GRAY1, [rect_x, 40, 100, 100])
        screen.blit(text, [195, 85])
        text = font.render("MINESWEEPER", True, BLACK)
        screen.blit(text, [217, 70])
        rect_x += rect_change_x
        if rect_x > 318 or rect_x < 105:
            rect_change_x = rect_change_x * -1
        font = pygame.font.Font(None, 45)
        pygame.draw.rect(screen, WHITE, [55, 140, 400, 50])
        text = font.render("Please select a difficulty:", True, BLACK)
        screen.blit(text, [65, 150])
        pygame.draw.rect(screen, GREEN, [107, 325, 80, 80])
        pygame.draw.rect(screen, YELLOW, [213, 325, 80, 80])
        pygame.draw.rect(screen, RED, [317, 325, 80, 80])
        text = font.render("Easy", True, BLACK)
        screen.blit(text, [111, 350])
        font = pygame.font.Font(None, 30)
        text = font.render("Medium", True, BLACK)
        screen.blit(text, [216, 356])
        font = pygame.font.Font(None, 45)
        text = font.render("Hard", True, BLACK)
        screen.blit(text, [320, 350])
        clock.tick(60)
        pygame.display.flip()
    #--------------------------------------------TITLE SCREEN END--------------------------------------------------#
        
    # Initial data
    font = pygame.font.Font(None, 25)
    grid = []
    mineGrid = []
    numberGrid = []
    blankSpaceChecker = []
    possibleBlanks = []
    squaresRevealed = []
    resultRevealed = []
    number_counting = 0
    mineCount = 0
    rect_x = 400
    rect_y = 250
    rect_change_x = 2
    rect_change_y = 3
    done2 = False
    done3 = False
    done4 = False
    done5 = False
    win   = False
    lose  = False
    blankLoop = False

    # Empty grid filled with 0s
    for row in range(20):
        grid.append([])
        for column in range(20):
            grid[row].append(0)
    # Empty mineGrid filled with 0s
    for row in range(20):
        mineGrid.append([])
        for column in range(20):
            mineGrid[row].append(0)
    # Fill mine grid randomly
    for elem in range(20):
        for elem2 in range(20):
            rand = random.randint(0, difficulty)
            if (rand == 1):
                mineGrid[elem][elem2] = 1
    # Empty numberGrid filled with 0s
    for row in range(20):
        numberGrid.append([])
        for column in range(20):
            numberGrid[row].append(0)
    # Fill numberGrid with correct numbers
    for elem3 in range(20):
        for elem4 in range(20):
            data1, data3, data4, data5, data6, data7, data8, data9 = 0, 0, 0, 0, 0, 0, 0, 0
            try:
                if (not elem4 - 1 < 0):
                    data1 = mineGrid[elem3][elem4-1]
            except IndexError:
                data1 = "null"
            try:
                data3 = mineGrid[elem3][elem4+1]
            except IndexError:
                data3 = "null"
            try:
                if (not elem3 - 1 < 0 and not elem4 - 1 < 0):
                    data4 = mineGrid[elem3-1][elem4-1]
            except IndexError:
                data4 = "null"
            try:
                if (not elem3 - 1 < 0):
                    data5 = mineGrid[elem3-1][elem4]
            except IndexError:
                data5 = "null"
            try:
                if (not elem3 - 1 < 0):
                    data6 = mineGrid[elem3-1][elem4+1]
            except IndexError:
                data6 = "null"
            try:
                if (not elem4 - 1 < 0):
                    data7 = mineGrid[elem3+1][elem4-1]
            except IndexError:
                data7 = "null"
            try:
                data8 = mineGrid[elem3+1][elem4]
            except IndexError:
                data8 = "null"
            try:
                data9 = mineGrid[elem3+1][elem4+1]
            except IndexError:
                data9 = "null"
            if (data1 == 1):
                number_counting += 1
            if (data3 == 1):
                number_counting += 1
            if (data4 == 1):
                number_counting += 1
            if (data5 == 1):
                number_counting += 1
            if (data6 == 1):
                number_counting += 1
            if (data7 == 1):
                number_counting += 1
            if (data8 == 1):
                number_counting += 1
            if (data9 == 1):
                number_counting += 1
            numberGrid[elem3][elem4] = number_counting
            number_counting = 0
    # Replaces all 0s in numberGrid with ""
    for k in range(20):
        for l in range(20):
            if numberGrid[k][l] == 0:
                numberGrid[k][l] = ""
    # Counts total number of mines
    for i in range(20):
        for j in range(20):
            if mineGrid[i][j] == 1:
                mineCount += 1

    # -------------------------------------Main Program Loop-----------------------------------------------------------------------------------#
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                done6 = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                column = position[0] // (width + margin)
                row = position[1] // (height + margin)
                if (column > 19):
                    column = 19
                if (row > 19):
                    row = 19
                if event.button == 1:
                    if (mineGrid[row][column] == 0 and not grid[row][column] == 3 and not grid[row][column] == 4):
                        blankLoop = False
                        if not numberGrid[row][column] == "":
                            grid[row][column] = 1
                        ###--------------------------------------Clearing algorithm-------------------------------###
                        if numberGrid[row][column] == "":
                            blankSpaceChecker.append((row, column))
                        while blankLoop == False:
                            for element in blankSpaceChecker:
                                topleft, top, topright, left, right, bottomleft, bottom, bottomright = 0,0,0,0,0,0,0,0
                                if (grid[element[0]][element[1]] == 0 and numberGrid[element[0]][element[1]] == ""):
                                    try:
                                        if (not element[1] - 1 < 0):
                                            left = (element[0],element[1]-1)
                                            if left not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                                possibleBlanks.append(left)
                                    except IndexError:
                                        left = "null"
                                    try:
                                        right = (element[0],element[1]+1)
                                        if right not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                            possibleBlanks.append(right)
                                    except IndexError:
                                        right = "null"
                                    try:
                                        if (not element[0] - 1 < 0 and not element[1] - 1 < 0):
                                            topleft = (element[0]-1,element[1]-1)
                                            if topleft not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                                possibleBlanks.append(topleft)
                                    except IndexError:
                                        topleft = "null"
                                    try:
                                        if (not element[0] - 1 < 0):
                                            top = (element[0]-1,element[1])
                                            if top not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                                possibleBlanks.append(top)
                                    except IndexError:
                                        top = "null"
                                    try:
                                        if (not element[0] - 1 < 0):
                                            topright = (element[0]-1,element[1]+1)
                                            if topright not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                                possibleBlanks.append(topright)
                                    except IndexError:
                                        topright = "null"
                                    try:
                                        if (not element[1] - 1 < 0):
                                            bottomleft = (element[0]+1,element[1]-1)
                                            if bottomleft not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                                possibleBlanks.append(bottomleft)
                                    except IndexError:
                                        bottomleft = "null"
                                    try:
                                        bottom = (element[0]+1,element[1])
                                        if bottom not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                            possibleBlanks.append(bottom)
                                    except IndexError:
                                        bottom = "null"
                                    try:
                                        bottomright = (element[0]+1,element[1]+1)
                                        if bottomright not in possibleBlanks and grid[element[0]][element[1]] == 0:
                                            possibleBlanks.append(bottomright)
                                    except IndexError:
                                        bottomright = "null"
                                grid[element[0]][element[1]] = 1
                            blankSpaceChecker = []
                            for elem in possibleBlanks:
                                try:
                                    if (numberGrid[elem[0]][elem[1]] == "" and grid[elem[0]][elem[1]] == 0):
                                        blankSpaceChecker.append((elem[0],elem[1]))
                                except IndexError:
                                    continue
                                try:
                                    if (not numberGrid[elem[0]][elem[1]] == "" and grid[elem[0]][elem[1]] == 0):
                                        grid[elem[0]][elem[1]] = 1
                                except IndexError:
                                    continue
                            possibleBlanks = []
                            if (len(blankSpaceChecker) == 0):
                                blankLoop = True
                       ###--------------------------------------Clearing algorithm end-------------------------------###

                    if (mineGrid[row][column] == 1 and not grid[row][column] == 3 and not grid[row][column] == 4):
                        grid[row][column] = 2
                if event.button == 3:
                    if grid[row][column] == 0:
                        grid[row][column] = 3
                        continue
                    if grid[row][column] == 3:
                        grid[row][column] = 4
                        continue
                    if grid[row][column] == 4:
                        grid[row][column] = 0
                        continue
        screen.fill(BLACK)
        for row in range(20):
            for column in range(20):
                if grid[row][column] == 0:
                    color = WHITE
                elif grid[row][column] == 1:
                    number_on_grid = str(numberGrid[row][column])
                    if (not numberGrid[row][column] == ""):
                        color = GRAY2
                    else:
                        color = GRAY1
                    text = font.render(number_on_grid, True, BLACK)
                elif grid[row][column] == 2:
                    color = RED
                    text = font.render("X", True, BLACK)
                elif grid[row][column] == 3:
                    color = LGREEN
                    text = font.render("X", True, BLACK)
                elif grid[row][column] == 4:
                    color = YELLOW
                    text = font.render("?", True, BLACK)
                pygame.draw.rect(screen,
                                 color,
                                 [(margin+width)*column+margin,
                                  (margin+height)*row+margin,
                                  width,
                                  height])
                if (not grid[row][column] == 0):
                    screen.blit(text, [(margin+width)*column+margin,(margin+height)*row+margin])
                if (color == RED):
                    done = True
                    lose = True
        gameEndCheck = 0
        totalXCheck = 0
        for row1 in range(20):
            for column1 in range(20):
                if (mineGrid[row1][column1] == 1 and grid[row1][column1] == 3):
                    gameEndCheck += 1
                if (grid[row1][column1] == 3):
                    totalXCheck += 1
        if (gameEndCheck == mineCount and totalXCheck == mineCount):
            done = True
            win = True
        clock.tick(60)
        pygame.display.flip()
    # -------------------------------------Main Program Loop end-----------------------------------------------------------------------------------#
        
    #-----------------------------------END GAME SEQUENCE-----------------------------------#
    if lose == True:
        time.sleep(1)
        while done2 == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done2 = True
                    done6 = True
            for row in range(20):
                for column in range(20):
                    if mineGrid[row][column] == 1:
                        pygame.draw.rect(screen,
                                         RED,
                                         [(margin+width)*column+margin,
                                          (margin+height)*row+margin,
                                          width,
                                          height])
                        text = font.render("X", True, BLACK)
                        screen.blit(text, [(margin+width)*column+margin,(margin+height)*row+margin])
            pygame.display.flip()
            time.sleep(1)
            for row in range(20):
                for column in range(20):
                    pygame.draw.rect(screen,
                                        RED,
                                        [(margin+width)*column+margin,
                                        (margin+height)*row+margin,
                                        width,
                                        height])
                    clock.tick(130)
                    pygame.display.flip()
            time.sleep(1)
            done2 = True
        while done3 == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done3 = True
                    done6 = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    done3 = True
            screen.fill(BLACK)
            for x_offset in range(137, 407, 30):
                pygame.draw.line(screen,WHITE,[x_offset,260],[x_offset-10,250],2)
                pygame.draw.line(screen,WHITE,[x_offset,250],[x_offset-10,260],2)
            pygame.draw.rect(screen, RED, [125, 125, 260, 80])
            pygame.draw.rect(screen, GRAY2, [rect_x, rect_y, 50, 50])
            rect_x += rect_change_x
            rect_y += rect_change_y
            if rect_y > 455 or rect_y < 0:
                rect_change_y = rect_change_y * -1
            if rect_x > 455 or rect_x < 0:
                rect_change_x = rect_change_x * -1
            font = pygame.font.Font(None, 50)
            text = font.render("GAME OVER", True, WHITE)
            screen.blit(text, [150, 150])
            text = font.render("Thanks for playing!", True, RED)
            screen.blit(text, [92, 300])
            text = font.render("Click to play again.", True, WHITE)
            screen.blit(text, [92, 390])
            clock.tick(60)
            pygame.display.flip()
            
    if win == True:
        while done4 == False:
            for row in range(20):
                for column in range(20):
                    pygame.draw.rect(screen,
                                        GREEN,
                                        [(margin+width)*column+margin,
                                        (margin+height)*row+margin,
                                        width,
                                        height])
                    clock.tick(130)
                    pygame.display.flip()
            time.sleep(1)
            done4 = True
        while done5 == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done5 = True
                    done6 = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    done5 = True
            screen.fill(BLACK)
            for x_offset in range(135, 405, 30):
                pygame.draw.line(screen,GREEN,[x_offset,260],[x_offset-10,250],2)
                pygame.draw.line(screen,GREEN,[x_offset,250],[x_offset-10,260],2)
            pygame.draw.rect(screen, GREEN, [125, 125, 255, 80])
            pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])
            rect_x += rect_change_x
            rect_y += rect_change_y
            if rect_y > 455 or rect_y < 0:
                rect_change_y = rect_change_y * -1
            if rect_x > 455 or rect_x < 0:
                rect_change_x = rect_change_x * -1
            font = pygame.font.Font(None, 50)
            text = font.render("YOU WIN!", True, WHITE)
            screen.blit(text, [168, 150])
            text = font.render("Thanks for playing!", True, GREEN)
            screen.blit(text, [92, 300])
            text = font.render("Click to play again.", True, WHITE)
            screen.blit(text, [92, 390])
            clock.tick(60)
            pygame.display.flip()

pygame.quit()
