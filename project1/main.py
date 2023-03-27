#imports
import time
import pygame as p
import engine
import os

#constants
WIDTH = 512
HEIGHT = 512
ADD_BOX = 150
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
FPS = 30
IMAGES = {}


#image loading
def loadImages():
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wP", "bP", "bR", "bN", "bB", "bQ", "bK", "wC", "wS", "bC", "bS"]
    for piece in pieces:
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, 'images')
        IMAGES[piece] = p.transform.scale(p.image.load(os.path.join(image_path, piece+".png")), (SQ_SIZE, SQ_SIZE))
#the main window
def main():
#window name and icon
    p.init()
    p.display.set_caption("Shogi-Chess")
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'images' )
    programIcon = p.image.load(os.path.join(image_path, "icon.png"))
    p.display.set_icon(programIcon)
#screen height and width (white)
    screen = p.display.set_mode((WIDTH+ADD_BOX, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = engine.stategame()
    ValidMoves = gs.GetValidMove()
    moveMade = False #variable for when move is made else program slow
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
#variables for pieces
    buttonclick = False
    bishopclick = False
    rookclick = False
    queenclick = False
    knightclick = False
    pawnclick = False
#movelog
    movelog = []
#keeps window open
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
#undo move button press B
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove(move)
                    moveMade = True 


#click register for first click
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = [] 
#button at row 0 and col 7 bishop button
                    
                if row == 0 and col > 7:
                    if gs.whiteToMove == True:
                        if (gs.WBC-gs.Check_Board(gs.board)[6]) > 0:
                            bishopclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
                    else:
                        if (gs.BBC-gs.Check_Board(gs.board)[1]) > 0:
                            bishopclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
#button at row 1 and col 7 rook button
                elif row == 1 and col > 7:
                    if gs.whiteToMove == True:
                        if (gs.WRC-gs.Check_Board(gs.board)[5]) > 0:
                            rookclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
                    else:
                        if (gs.WRC-gs.Check_Board(gs.board)[0]) > 0:
                            rookclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
#button at row 2 and col 7 queen button
                elif row == 2 and col > 7:
                    if gs.whiteToMove == True:
                        if (gs.WQC-gs.Check_Board(gs.board)[8]) > 0:
                            queenclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
                    else:
                        if (gs.BQC-gs.Check_Board(gs.board)[3]) > 0:
                            queenclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
#knight button
                elif row == 3 and col > 7:
                    if gs.whiteToMove == True:
                        if (gs.WKC-gs.Check_Board(gs.board)[7]) > 0:
                            knightclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
                    else:
                        if (gs.BKC-gs.Check_Board(gs.board)[2]) > 0:
                            knightclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
#pawn button
                elif row == 4 and col > 7:
                    if gs.whiteToMove == True:
                        print(gs.WPC)
                        print(gs.Check_Board(gs.board)[9])
                        if (gs.WPC-gs.Check_Board(gs.board)[9]) > 0:
                            pawnclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
                    else:
                        if (gs.BPC-gs.Check_Board(gs.board)[4]) > 0:
                            pawnclick = True
                            buttonclick = True
                            playerClicks = []
                            sqSelected = ()
                        else:
                            pass
#button at row 4 and above the movelog save button
                elif row >= 5 and col > 7:
                    current_path = os.path.dirname(__file__)
                    path_G = os.path.join(current_path, 'game')
                    print(movelog)
                    f = open(path_G+"/Game.txt", "w")
                    for i in range(0, len(movelog)):
                        f.write(movelog[i]+"\n")
                    f.close()    
#detects the second click and saves as variable = sqSelected
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
#if bishop button pressed summon bishop as second click
                    if bishopclick == True and len(playerClicks) == 1:
                        gs.bishopSummon(row, col)
                        bishopclick = False
                        buttonclick = False
                        playerClicks = []
                        sqSelected = ()
                        ValidMoves = gs.GetValidMove()
#if rook button pressed summon bishop as second click
                    elif rookclick == True and len(playerClicks) == 1:
                        gs.rookSummon(row, col)
                        rookclick = False
                        buttonclick = False
                        playerClicks = []
                        sqSelected = ()
                        ValidMoves = gs.GetValidMove()
#if queen button pressed summon bishop as second click
                    elif queenclick == True and len(playerClicks) == 1:
                        gs.queenSummon(row, col)
                        queenclick = False
                        buttonclick = False
                        playerClicks = []
                        sqSelected = ()
                        ValidMoves = gs.GetValidMove()
                    elif knightclick == True and len(playerClicks) == 1:
                        gs.knightSummon(row, col)
                        knightclick = False
                        buttonclick = False
                        playerClicks = []
                        sqSelected = ()
                        ValidMoves = gs.GetValidMove()
                    elif pawnclick == True and len(playerClicks) == 1:
                        gs.pawnSummon(row, col)
                        pawnclick = False
                        buttonclick = False
                        playerClicks = []
                        sqSelected = ()
                        ValidMoves = gs.GetValidMove()
                    elif len(playerClicks) == 2: #click register for second click
                        move = engine.Move(playerClicks[0], playerClicks[1], gs.board)

                        print(move.getChessNotation())
                        movelog.append(move.getChessNotation())
                        for i in range(len(ValidMoves)):
                            if move == ValidMoves[i]: #checks move is valid

                                ranksToRows = {7:"1", 6:"2", 5:"3", 4:"4",3: "5", 2:"6", 1:"7", 0:"8"}
                                rowsToRanks = {v: k for k, v in ranksToRows.items()}
                                filesToCols = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h"} 
                                ColsToFiles = {v: k for k, v in filesToCols.items()}

#split list in half
                                def split(s):
                                    half, rem = divmod(len(s), 2)
                                    return s[:half + rem], s[half + rem:]
                                #get second move 
                                frontA, backA = split(move.getChessNotation())
                                #seperate second move into its row and column components.
                                F, B = split(backA)
                                r = rowsToRanks[B]#row
                                c = ColsToFiles[F]#col

                                if gs.whiteToMove == True:
                                    if gs.board[r][c] == "bP":
                                        gs.BPC -=1
                                        gs.WPC +=1
                                    elif gs.board[r][c] == "bB":
                                        gs.BBC -=1
                                        gs.WBC += 1
                                    elif gs.board[r][c] == "BQ":
                                        gs.BQC -=1
                                        gs.WQC += 1
                                    elif gs.board[r][c] == "bR":
                                        gs.BRC -=1
                                        gs.WRC += 1
                                    elif gs.board[r][c] == "bN":
                                        gs.BKC -=1
                                        gs.WKC += 1
                                else:
                                    if gs.board[r][c] == "wP":
                                        gs.WPC -=1
                                        gs.BPC +=1
                                    elif gs.board[r][c] == "wB":
                                        gs.WBC -=1
                                        gs.BBC += 1
                                    elif gs.board[r][c] == "wQ":
                                        gs.WQC -=1
                                        gs.BQC += 1
                                    elif gs.board[r][c] == "wR":
                                        gs.WRC -=1
                                        gs.BRC += 1
                                    elif gs.board[r][c] == "wN":
                                        gs.WKC -=1
                                        gs.BKC += 1
                                        
                                gs.makeMove(ValidMoves[i])
                                moveMade = True
                                
#resets clicks 
                            sqSelected = ()
                            playerClicks = []
                    else:
                        pass
                    
            if moveMade:#if move made update move from back end
                ValidMoves = gs.GetValidMove()
                moveMade = False
            drawGameState(screen, gs, ValidMoves, sqSelected, buttonclick)
                
            if gs.Checkmate:
                gameOver = True
                if gs.whiteToMove:
                    drawText(screen, "Back wins by Checkmate", "black")
                else:
                    drawText(screen, "White wins by Checkmate", "black")
            elif gs.Stalemate:
                gameOver = True
                drawText(screen, "stalemate", "black")

        
            clock.tick(FPS)
            p.display.flip()#change to other colour




#drawing board and pieces
def drawGameState(screen, gs, ValidMoves, sqSelected, buttonclick):
    drawBoard(screen,8)#displays board
    MoveHighlights(screen, gs, ValidMoves, sqSelected, buttonclick)#adds highlights
    drawPieces(screen, gs.board)#draws pieces on board
#draw board function
def piece_imagewords(screen):
#images for buttons added
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'images')
    IMAGESQ = p.image.load(os.path.join(image_path, "wQ.png"))
    IMAGESR = p.image.load(os.path.join(image_path, "wR.png"))
    IMAGESB = p.image.load(os.path.join(image_path, "wB.png"))
    IMAGESP = p.image.load(os.path.join(image_path, "wP.png"))
    IMAGESK = p.image.load(os.path.join(image_path, "wN.png"))
    
    BLACK = p.Color("#000000")
    font = p.font.SysFont(None, 24)
    font2 = p.font.SysFont(None, 40)
    bishop = font.render('Bishop', True, BLACK)
    pawn = font.render('pawn', True, BLACK)
    Rook = font.render('Rook', True, BLACK) 
    Queen = font.render('Queen', True, BLACK) 
    knight = font.render('Knight', True, BLACK)
    save = font2.render('Save', True, BLACK)

    screen.blit(bishop, (540, 20)) #bishop word
    screen.blit(IMAGESB, (595, 0)) #bishop image load
    screen.blit(Rook, (540, 84)) #rook word
    screen.blit(IMAGESR, (595, 64)) #rook image load
    screen.blit(Queen, (540, 148)) #queen word
    screen.blit(IMAGESQ, (595, 128)) # queen image load
    screen.blit(knight, (540, 220))#knight word
    screen.blit(IMAGESK, (595, 190))#knight image load
    screen.blit(pawn, (540, 280))#pawn word
    screen.blit(IMAGESP, (595, 255))#pawn image load
    screen.blit(save, (560, 350))#save word
def drawBoard(screen, DIMENSION):
    colors = [p.Color("white"), p.Color("#add8e6")]
    but1color = p.Color("#89cff0")
    but2color = p.Color("#00008b")
    but3color = p.Color("#8b0000")
    but4color = p.Color("#800080")
    but5color = p.Color("#40e0d0")
    SColor = p.Color("#2CAEBE")
    color_light = p.Color("#F1F1F1")
    #board colours and tiles
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

        p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
        p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
        p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
        p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
        p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
        p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
        piece_imagewords(screen)

        mouse = p.mouse.get_pos()  
        
        if 512 <= mouse[0] <= 662 and 0 <= mouse[1] <= 63: #1
            p.draw.rect(screen, color_light, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
            piece_imagewords(screen)
        elif 512 <= mouse[0] <= 662 and 64 <= mouse[1] <= 127: #2
            p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, color_light, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
            piece_imagewords(screen)
        elif 512 <= mouse[0] <= 662 and 128 <= mouse[1] <= 191:#3
            p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, color_light, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
            piece_imagewords(screen)
        elif 512 <= mouse[0] <= 662 and 192 <= mouse[1] <= 255:#4
            p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, color_light, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
            piece_imagewords(screen)
        elif 512 <= mouse[0] <= 662 and 256 <= mouse[1] <= 320:#5
            p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, color_light, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
            piece_imagewords(screen)
        elif 512 <= mouse[0] <= 662 and 320 <= mouse[1] <= 512:#5
            p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, color_light, p.Rect(512, 320, 150, 200))
            piece_imagewords(screen)
        else:  
            p.draw.rect(screen, but1color, p.Rect(512, 0, 150, SQ_SIZE))
            p.draw.rect(screen, but2color, p.Rect(512, 64, 150, SQ_SIZE))
            p.draw.rect(screen, but3color, p.Rect(512, 128, 150, SQ_SIZE))
            p.draw.rect(screen, but4color, p.Rect(512, 192, 150, SQ_SIZE))
            p.draw.rect(screen, but5color, p.Rect(512, 256, 150, SQ_SIZE))
            p.draw.rect(screen, SColor, p.Rect(512, 320, 150, 200))
        

        
        piece_imagewords(screen) 


def MoveHighlights(screen, gs, ValidMoves, sqSelected, buttonclick):
    if sqSelected != () and buttonclick == False:
        r, c = sqSelected
        if gs.board[r][c][0] == ("w" if gs.whiteToMove else "b"): #square selected is piece that can be moved
            #highlight square for piece
            surface = p.Surface((SQ_SIZE, SQ_SIZE))
            surface.set_alpha(100) # transparent value
            surface.fill(p.Color("#00003f"))#dark blue color
            screen.blit(surface,(c*SQ_SIZE, r*SQ_SIZE))
            #highlighted moves
            surface.fill(p.Color("#0C800C")) #dark green
            for move in ValidMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(surface, (SQ_SIZE*move.endCol, SQ_SIZE*move.endRow))
                    #shows moves that are possible with particular piece


#draw piece function            
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "-":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE) )
    
def HowToPlay():
    p.init()  
    res = (662,512)  
    p.display.set_caption("Shogi-Chess")
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'images' )
    programIcon = p.image.load(os.path.join(image_path, "icon.png"))
    p.display.set_icon(programIcon)
    screen = p.display.set_mode(res)  
    color = (255,255,255)  #white
    color_light = (170,170,170)  # light shade of the button  
    color_dark = (100,100,100)  # dark shade of the button  
    gs = engine.stategame()
    loadImages()
    nextI = 0

    width = screen.get_width()  

    height = screen.get_height()   

    smallfont = p.font.SysFont('Corbel',35)  
    textB = smallfont.render('Back' , True , color)  
    textC = smallfont.render('>>>>' , True , color)
    textD = smallfont.render('<<<<' , True , color)
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'images' )
    cap1 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture1.PNG")), (400,400))
    cap2 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture2.PNG")), (400,400))
    cap3 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture3.PNG")), (400,400))
    cap4 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture4.PNG")), (400,400))
    cap5 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture5.PNG")), (400,400))
    cap6 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture6.PNG")), (400,400))
    cap7 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture7.PNG")), (400,400))
    cap8 = p.transform.scale(p.image.load(os.path.join(image_path, "Capture8.PNG")), (400,400))
    listcap = [cap1,cap2,cap3,cap4,cap5,cap6,cap7,cap8]
    while True:  
        for ev in p.event.get():   
            if ev.type == p.QUIT:  
                p.quit()  
            if ev.type == p.MOUSEBUTTONDOWN:  #checks if a mouse is clicked  
                if width-150 <= mouse[0] <= width and height-50 <= mouse[1] <= height:  
                    p.quit()
                    main_menu()
                elif width-150 <= mouse[0] <= width and height-100 <= mouse[1] <= height-50:
                    nextI +=1
                elif width-150 <= mouse[0] <= width and height-150 <= mouse[1] <= height-100:
                    nextI-=1


        screen.fill(p.Color("#d3d3d3"))  
        colors = [p.Color("white"), p.Color("#add8e6")]
        screen.blit(listcap[nextI], (SQ_SIZE, SQ_SIZE))
        #board colours and tiles

        mouse = p.mouse.get_pos()  

        if width-150 <= mouse[0] <= width and height-50 <= mouse[1] <= height:  
            p.draw.rect(screen,color_light,[width-150,height-50,140,40])  
            p.draw.rect(screen,color_dark,[width-150,height-100,140,40])  
            p.draw.rect(screen,color_dark,[width-150,height-150,140,40]) 
        elif width-150 <= mouse[0] <= width and height-100 <= mouse[1] <= height-50:
            p.draw.rect(screen,color_light,[width-150,height-100,140,40])
            p.draw.rect(screen,color_dark,[width-150,height-50,140,40])   
            p.draw.rect(screen,color_dark,[width-150,height-150,140,40]) 
        elif width-150 <= mouse[0] <= width and height-150 <= mouse[1] <= height-100:
            p.draw.rect(screen,color_dark,[width-150,height-50,140,40])  
            p.draw.rect(screen,color_dark,[width-150,height-100,140,40])  
            p.draw.rect(screen,color_light,[width-150,height-150,140,40]) 

        else:  
            p.draw.rect(screen,color_dark,[width-150,height-50,140,40])  
            p.draw.rect(screen,color_dark,[width-150,height-100,140,40])  
            p.draw.rect(screen,color_dark,[width-150,height-150,140,40]) 

        screen.blit(textB , (width-110,height-50))   
        screen.blit(textC, (width-110,height-100))
        screen.blit(textD, (width-110,height-150))
        if nextI >0 and nextI < 7:
            screen.blit(listcap[nextI], (SQ_SIZE, SQ_SIZE))
        p.display.update()  


def main_menu():
    # initializing the constructor  
    p.init()  
    p.display.set_caption("Shogi-Chess")
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'images' )
    programIcon = p.image.load(os.path.join(image_path, "icon.png"))
    p.display.set_icon(programIcon)
    # opens up a window  
    res = (662, 512)
    screen = p.display.set_mode(res)  
    color = (255,255,255)  # white color  
    color_light = (170,170,170)  # light shade of the button  
    color_dark = (100,100,100)  # dark shade of the button 
    width = screen.get_width()  
    height = screen.get_height()  

    smallfont = p.font.SysFont('Corbel',30)  
    textQ = smallfont.render('quit' , True , color)  
    textH = smallfont.render('How to play' , True , color)  
    textP = smallfont.render('Play' , True , color)  
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'images')
    background_image = p.transform.scale(p.image.load(os.path.join(image_path, "Background_image.jpg")), (662,512))
    
    while True:  
        screen.blit(background_image, [0, 0])
        font = p.font.SysFont("Helvitca", 32, True, False)
        textObject = font.render("Shogi-Chess", 0, p.Color("white"))
        textlocation = p.Rect(0, 0, WIDTH, HEIGHT).move((WIDTH/2+ADD_BOX-50)- (textObject.get_width()/2), (HEIGHT/2-100)-textObject.get_height()/2)
        screen.blit(textObject,textlocation)
        for ev in p.event.get():  
            
            if ev.type == p.QUIT:  
                p.quit()  
                
            #checks if a mouse is clicked  
            if ev.type == p.MOUSEBUTTONDOWN:  
                
                #if the mouse is clicked on the  
                # button the game is terminated  
                if width/2-50 <= mouse[0] <= width/2+100 and height/2+50 <= mouse[1] <= height/2+90:#quit button
                    p.quit()  
                elif width/2-50 <= mouse[0] <= width/2+100 and height/2-50 <= mouse[1] <= height/2-10:#play button
                    p.quit()
                    main()
                elif width/2-50 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+40: #how to play
                    p.quit()
                    HowToPlay()
                else:
                    pass
                    
        mouse = p.mouse.get_pos()  
        
        if width/2-50 <= mouse[0] <= width/2+100 and height/2+50 <= mouse[1] <= height/2+90:  #quit
            p.draw.rect(screen,color_light,[width/2-50,height/2+50,140,40])  
            p.draw.rect(screen,color_dark,[width/2-50,height/2,140,40])
            p.draw.rect(screen,color_dark,[width/2-50,height/2-50,140,40])
        elif width/2-50 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+40: #how to play
            p.draw.rect(screen,color_light,[width/2-50,height/2,140,40])
            p.draw.rect(screen,color_dark,[width/2-50,height/2+50,140,40]) 
            p.draw.rect(screen,color_dark,[width/2-50,height/2-50,140,40])
        elif width/2-50 <= mouse[0] <= width/2+100 and height/2-50 <= mouse[1] <= height/2+40: #Play
            p.draw.rect(screen,color_dark,[width/2-50,height/2,140,40])
            p.draw.rect(screen,color_dark,[width/2-50,height/2+50,140,40])  
            p.draw.rect(screen,color_light,[width/2-50,height/2-50,140,40])
        
        else:  
            p.draw.rect(screen,color_dark,[width/2-50,height/2,140,40])
            p.draw.rect(screen,color_dark,[width/2-50,height/2+50,140,40])  
            p.draw.rect(screen,color_dark,[width/2-50,height/2-50,140,40])
        

        screen.blit(textQ , (width/2,height/2+50))  
        screen.blit(textH, (width/2-50,height/2))
        screen.blit(textP, (width/2,height/2-50))

        p.display.update()  

def drawText(screen, text, colorq):
    font = p.font.SysFont("Helvitca", 32, True, False)
    textObject = font.render(text, 0, p.Color(colorq))
    textlocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2- textObject.get_width()/2, HEIGHT/2-textObject.get_height()/2)
    screen.blit(textObject,textlocation)
main_menu()