
import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Chess")
icon = pygame.image.load('./Assets/chesscom_pawn.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

#constants
frameRate = 60
boardTopLeftX = 280
fillWhite = (235, 236, 208)
fillGreen = (115, 149, 82)
turnStep = 0
selection = 100

whitePieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', ]

blackLocations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

blackPieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', ]

whiteLocations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

board = [['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black',],
         ['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white'],
         ['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black',],
         ['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white'],
         ['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black',],
         ['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white'],
         ['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black',],
         ['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white']]


#assets
bq = pygame.image.load('Assets/bq.png')
bq = pygame.transform.scale(bq, (90, 90))
bk = pygame.image.load('Assets/bk.png')
bk = pygame.transform.scale(bk, (90, 90))
br = pygame.image.load('Assets/br.png')
br = pygame.transform.scale(br, (90, 90))
bn = pygame.image.load('Assets/bn.png')
bn = pygame.transform.scale(bn, (90, 90))
bb = pygame.image.load('Assets/bb.png')
bb = pygame.transform.scale(bb, (90, 90))
bp = pygame.image.load('Assets/bp.png')
bp = pygame.transform.scale(bp, (90, 90))
wq = pygame.image.load('Assets/wq.png')
wq = pygame.transform.scale(wq, (90, 90))
wk = pygame.image.load('Assets/wk.png')
wk = pygame.transform.scale(wk, (90, 90))
wr = pygame.image.load('Assets/wr.png')
wr = pygame.transform.scale(wr, (90, 90))
wn = pygame.image.load('Assets/wn.png')
wn = pygame.transform.scale(wn, (90, 90))
wb = pygame.image.load('Assets/wb.png')
wb = pygame.transform.scale(wb, (90, 90))
wp = pygame.image.load('Assets/wp.png')
wp = pygame.transform.scale(wp, (90, 90))
whiteImages = [wp, wn, wb, wr, wk, wq]
blackImages = [bp, bn, bb, br, bk, bq]
pieceList = ['pawn', 'knight', 'bishop', 'rook', 'king', 'queen']
capturedWhite = []
capturedBlack = []


#functions
def draw_board():
    for i in range(0, 8, 2):
        for m in range(0, 8, 2):
            pygame.draw.rect(screen, fillWhite, [boardTopLeftX + (m * 90)      , i * 90      , 90, 90])
            pygame.draw.rect(screen, fillGreen, [boardTopLeftX + ((m + 1) * 90), i * 90      , 90, 90])
            pygame.draw.rect(screen, fillGreen, [boardTopLeftX + (m * 90)      , (i + 1) * 90, 90, 90])
            pygame.draw.rect(screen, fillWhite, [boardTopLeftX + ((m + 1) * 90), (i + 1) * 90, 90, 90])

def draw_pieces():
    for i in range(len(whitePieces)):
        if turnStep < 2 and selection == i:
                pygame.draw.rect(screen, (245, 245, 141), [280 + whiteLocations[i][0] * 90, whiteLocations[i][1] * 90, 90, 90])

        index = pieceList.index(whitePieces[i])
        screen.blit(whiteImages[index], ( 279 + whiteLocations[i][0] * 90, whiteLocations[i][1] * 90))
                
    for i in range(len(blackPieces)):
        if turnStep >= 2 and selection == i:
            pygame.draw.rect(screen, (245, 245, 141), [280 + blackLocations[i][0] * 90, blackLocations[i][1] * 90, 90, 90])
        index = pieceList.index(blackPieces[i])
        screen.blit(blackImages[index], ( 279 + blackLocations[i][0] * 90, blackLocations[i][1] * 90))
        
def checkPawn(location, type):
    movesList = []
    if type == 'white':
        if (location[0], location[1] - 1) not in whiteLocations and \
           (location[0], location[1] - 1) not in blackLocations and \
            location[1] >= 0:
            movesList.append((location[0], location[1] - 1))
        if (location[0], location[1] - 2) not in whiteLocations and \
           (location[0], location[1] - 2) not in blackLocations and \
            location[1] == 6:
            movesList.append((location[0], location[1] - 2))
        if (location[0] + 1, location[1] - 1) in blackLocations:
            movesList.append((location[0] + 1, location[1] - 1, True))
        if (location[0] - 1, location[1] - 1) in blackLocations:
            movesList.append((location[0] - 1, location[1] - 1, True))

    else:
        if (location[0], location[1] + 1) not in whiteLocations and \
           (location[0], location[1] + 1) not in blackLocations and \
            location[1] <= 7:
            movesList.append((location[0], location[1] + 1))

        if (location[0], location[1] + 2) not in whiteLocations and \
           (location[0], location[1] + 2) not in blackLocations and \
            location[1] == 1:
            movesList.append((location[0], location[1] + 2))

        if (location[0] + 1, location[1] + 1) in whiteLocations:
            movesList.append((location[0] + 1, location[1] + 1, True))

        if (location[0] - 1, location[1] + 1) in whiteLocations:
            movesList.append((location[0] - 1, location[1] + 1, True))
    return movesList

def checkRook(location, type):
    movesList = []
    if type == 'white':
        friendsList = whiteLocations
        enemiesList = blackLocations
    else:
        friendsList = blackLocations
        enemiesList = whiteLocations

    for i in range(4):
        path = True
        dist = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while path:
            x = location[0] + (dist * directions[i][0])
            y = location[1] + (dist * directions[i][1])
            if (x, y) not in friendsList\
               and 0 <= x <= 7\
               and 0 <= y <= 7:
                if (x, y) in enemiesList:
                    movesList.append((x, y, True))
                else:
                    movesList.append((x, y))
                if (x, y) in enemiesList:
                    path = False
                dist += 1
            else:
                path = False

    return movesList

def checkKnight(location, type):
    movesList = []
    if type == 'white':
        friendsList = whiteLocations
        enemiesList = blackLocations
    else:
        friendsList = blackLocations
        enemiesList = whiteLocations

    targets = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    for i in range(8):
        x = location[0] + targets[i][0]
        y = location[1] + targets[i][1]
        if 0 <= x <= 7 and\
           0 <= y <= 7 and\
           (x, y) not in friendsList:
           
            if (x, y) in enemiesList:
                movesList.append((x, y, True))
            else:
                movesList.append((x, y))


    return movesList

def checkBishop(location, type):
    movesList = []
    if type == 'white':
        friendsList = whiteLocations
        enemiesList = blackLocations
    else:
        friendsList = blackLocations
        enemiesList = whiteLocations

    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(len(directions)):  # Loop through all directions
        dx = directions[i][0]
        dy = directions[i][1]
        dist = 1

        while True:
            x = location[0] + (dist * dx)
            y = location[1] + (dist * dy)

            if (x, y) not in friendsList and 0 <= x <= 7 and 0 <= y <= 7:
                movesList.append((x, y))
                if (x, y) in enemiesList:
                    movesList[-1] = (x, y, True)  # Update last move with capture
                    break  # Stop at first enemy
            else:
                break

            dist += 1

    return movesList

def checkKing(location, type):
    movesList = []

    if type == 'white':
        friendsList = whiteLocations
        enemiesList = blackLocations
    else:
        friendsList = blackLocations
        enemiesList = whiteLocations

    targets = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(8):
        x = location[0] + targets[i][0]
        y = location[1] + targets[i][1]

        if (x, y) not in friendsList and 0 <= x <= 7 and 0 <= y <= 7:
            if (x, y) in enemiesList:
                movesList.append((x, y, True))
                
            else:
                movesList.append((x, y))

    index = whitePieces.index('king')
    location = whiteLocations[index]
    """if (location[0] + 1) not in whiteLocations and \
       (location[0] + 2) not in whiteLocations and \
       (location[0] + 1) not in blackLocations and \
       (location[0] + 2) not in blackLocations and \
       """

    return movesList

def checkQueen(location, type):
    return checkBishop(location, type) + checkRook(location, type)

def findCheck():
    check = False

    if turnStep < 2:
        kingIndex = whitePieces.index('king')
        kingLocation = whiteLocations[kingIndex]
        if kingLocation in blackOptions:
            check = 'white'

    else:
        kingIndex = blackPieces.index('king')
        kingLocation = blackLocations[kingIndex]
        if kingLocation in whiteOptions:
            check = 'black'

    return check

def checkOptions(pieces, locations, type):
    movesList = []
    allMovesList = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            movesList = checkPawn(location, type)
        if piece == 'rook': 
            movesList = checkRook(location, type)
        if piece == 'knight':
            movesList = checkKnight(location, type)
        if piece == 'bishop':
            movesList = checkBishop(location, type)
        if piece == 'king':
            movesList = checkKing(location, type)
        if piece == 'queen':
            movesList = checkQueen(location, type)
        
        

        allMovesList.append(movesList)
    return allMovesList

def drawValid(moves):
    if turnStep < 2:
        color = 'red'
    else: 
        color = 'blue'
    if moves == None:
        return
    for i in range(len(moves)):
        y = moves[i][1]
        x = moves[i][0]
        
        movesLength = len(moves[i])

        if movesLength == 3 and (board[y][x]) != 'white':
            pygame.draw.circle(screen, pygame.Color(99, 128, 70, 0), (moves[i][0] * 90 + 280 + 45, moves[i][1] * 90 + 45), 45, 8)
        elif movesLength == 3 and (board[y][x]) == 'white':
            pygame.draw.circle(screen, pygame.Color(202, 203, 179, 0), (moves[i][0] * 90 + 280 + 45, moves[i][1] * 90 + 45), 45, 8)
        elif (board[y][x]) != 'white':
            pygame.draw.circle(screen, (99, 128, 70), (moves[i][0] * 90 + 280 + 45, moves[i][1] * 90 + 45), 14)
        else:
            pygame.draw.circle(screen, (202, 203, 179), (moves[i][0] * 90 + 280 + 45, moves[i][1] * 90 + 45), 14)

def checkValidMoves():
    if turnStep < 2:
        optionsList = whiteOptions
    else:
        optionsList = blackOptions
    validOptions = optionsList[selection]
    return validOptions

blackOptions = checkOptions(blackPieces, blackLocations, 'black')
whiteOptions = checkOptions(whitePieces, whiteLocations, 'white')

running = True
while running:
    clock.tick(frameRate)
    draw_board()
    draw_pieces()
    validMoves = []
    if selection != 100:
        validMoves = checkValidMoves()
        drawValid(validMoves)
    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x = (event.pos[0] - 279) // 90
            y = (event.pos[1]) // 90
            if x < 0 or x > 7:
                continue
            clickCoords = (x, y)
            if turnStep <= 1:
                if clickCoords in whiteLocations:
                    selection = whiteLocations.index(clickCoords)
                    if turnStep == 0:
                        turnStep = 1
                print(validMoves)
                if (clickCoords in validMoves or (clickCoords + (True,)) in validMoves) and selection != 100:
                    whiteLocations[selection] = clickCoords
                    if clickCoords in blackLocations:
                        blackPiece = blackLocations.index(clickCoords)
                        capturedWhite.append(blackPieces[blackPiece])
                        blackPieces.pop(blackPiece)
                        blackLocations.pop(blackPiece)
                    turnStep = 2
                    selection = 100

                    blackOptions = checkOptions(blackPieces, blackLocations, 'black')
                    whiteOptions = checkOptions(whitePieces, whiteLocations, 'white')
                    validMoves = []

            if turnStep > 1:
                if clickCoords in blackLocations:
                    selection = blackLocations.index(clickCoords)
                    if turnStep == 2:
                        turnStep = 3
                if (clickCoords in validMoves or (clickCoords + (True,)) in validMoves) and selection != 100:
                    blackLocations[selection] = clickCoords
                    if clickCoords in whiteLocations:
                        whitePiece = whiteLocations.index(clickCoords)
                        capturedBlack.append(whitePieces[whitePiece])
                        whitePieces.pop(whitePiece)
                        whiteLocations.pop(whitePiece)
                    turnStep = 0
                    selection = 100
                    blackOptions = checkOptions(blackPieces, blackLocations, 'black')
                    whiteOptions = checkOptions(whitePieces, whiteLocations, 'white')
                    validMoves = []
    
    #update display
    pygame.display.flip()
    
pygame.quit()