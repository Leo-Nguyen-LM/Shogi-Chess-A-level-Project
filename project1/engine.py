
class stategame():
    def __init__(self):
#board list within list 
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.movelog = []
        self.whiteKPos = (7, 4) #white king position
        self.blackKPos = (0, 4) #black king position
        self.Checkmate = False
        self.Stalemate = False
        #number of bishops captured
        self.WBC = 2
        self.BBC = 2
        #number of queens captured
        self.WQC = 1
        self.BQC = 1
        #number of rooks captured
        self.WRC = 2
        self.BRC = 2
        #number of knights captured
        self.WKC = 2
        self.BKC = 2
        #number of pawns captured
        self.WPC = 8
        self.BPC = 8
    def Check_Board(self, board):
        bR = 0
        bB = 0
        bN = 0
        bQ = 0
        bP = 0
        wR = 0
        wB = 0
        wN = 0
        wQ = 0
        wP = 0
        for i in range(0,8):
            for j in range(0,8,1):
                if self.board[i][j] == "bR":
                    bR += 1
                elif self.board[i][j] == "bB":
                    bB += 1
                elif self.board[i][j] == "bN":
                    bN += 1
                elif self.board[i][j] == "bQ":
                    bQ += 1
                elif self.board[i][j] == "bP":
                    bP += 1
                elif self.board[i][j] == "wR":
                    wR += 1
                elif self.board[i][j] == "wB":
                    wB += 1
                elif self.board[i][j] == "wN":
                    wN += 1
                elif self.board[i][j] == "wQ":
                    wQ += 1
                elif self.board[i][j] == "wP":
                    wP += 1
                else:
                    pass


        piecelist = [bR, bB, bN, bQ, bP, wR, wB, wN, wQ, wP]
        return piecelist

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "-"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movelog.append(move)
        self.whiteToMove = not self.whiteToMove

#if kings move change position of kings
        if self.board[move.endRow][move.endCol] == "wK":#white
            self.whiteKPos = (move.endRow, move.endCol)
        elif self.board[move.endRow][move.endCol] == "bK":#black
            self.blackKPos = (move.endRow, move.endCol)

#pawn promotion
        if move.IsPawnPromotion:
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + "Q"
#Rook promotion
        if move.IsRookPromotion:
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + "C"
#Bishop promotion
        if move.IsBishopPromotion:
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + "S"
#undoing moves
    def undoMove(self, move):
        if len(self.movelog) != 0:
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
#undo king move position
            if move.pieceMoved == "wK":
                self.whiteKPos = (move.startRow, move.startCol)
            elif move.pieceMoved == "bK":
                self.blackKPos = (move.startRow, move.startCol)
#summon bishop
    def bishopSummon(self, r, c):
        if self.whiteToMove == True:
            if self.board[r][c] == "-":
                self.board[r][c] = "wB"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
        else:
            if self.board[r][c] == "-":
                self.board[r][c] = "bB"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
#summon rook
    def rookSummon(self, r, c):
        if self.whiteToMove == True:
            if self.board[r][c] == "-":
                self.board[r][c] = "wR"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
        else:
            if self.board[r][c] == "-":
                self.board[r][c] = "bR"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
#summon queen
    def queenSummon(self, r, c):
        if self.whiteToMove == True:
            if self.board[r][c] == "-":
                self.board[r][c] = "wQ"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
        else:
            if self.board[r][c] == "-":
                self.board[r][c] = "bQ"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
#pawn summon
    def pawnSummon(self, r, c):
        if self.whiteToMove == True:
            if self.board[r][c] == "-":
                self.board[r][c] = "wP"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
        else:
            if self.board[r][c] == "-":
                self.board[r][c] = "bP"
                self.whiteToMove = not self.whiteToMove    
            else:
                pass
#knight
    def knightSummon(self, r, c):
        if self.whiteToMove == True:
            if self.board[r][c] == "-":
                self.board[r][c] = "wN"
                self.whiteToMove = not self.whiteToMove
            else:
                pass
        else:
            if self.board[r][c] == "-":
                self.board[r][c] = "bN"
                self.whiteToMove = not self.whiteToMove     
            else:
                pass       
    def GetValidMove(self):
        Movement = self.GetAllPossibleMoves()
        for i in range((len(Movement)-1), -1 ,-1): #Goes backwards within the list
            CMove = Movement[i]
            self.makeMove(CMove)#makes move to check for checks
            self.whiteToMove = not self.whiteToMove
            if self.checks() == True:#if there are then remove the move from valid moves
                Movement.remove(CMove)

            self.whiteToMove = not self.whiteToMove
            self.undoMove(CMove) #undo the move

            if len(Movement) == 0:
                if self.checks() == True:
                    self.Checkmate = True #if no more moves in list then its checkmate
                else:
                    self.Stalemate = True #if no more moves and not check its stalemate
            else:
                self.Checkmate = False
                self.Stalemate = False
        return Movement

    def checks(self):
        if self.whiteToMove == True:
            return self.SquareUnderAttack(self.whiteKPos[0], self.whiteKPos[1])#uses white king to check if king is in check

        else:
            return self.SquareUnderAttack(self.blackKPos[0], self.blackKPos[1])#uses black king to check if king is in check
    def SquareUnderAttack(self, r, c):
        #switch to enemy move to get opponent moves
        self.whiteToMove = not self.whiteToMove
        Opponents_moves = self.GetAllPossibleMoves()#get enemy moves
        self.whiteToMove = not self.whiteToMove#switches back

        for move in Opponents_moves:
            if move.endRow == r and move.endCol == c:
                return True#if in check return true

        return False
    
    
    def GetAllPossibleMoves(self):
        moves = []
        for r in range(8):    #all the rows
            for d in range(8):  #all the columns in each row
                turn = self.board[r][d][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][d][1] 
                    if piece == "P":
                        self.getPawnMoves(r, d, moves)#gets pawn moves
                    elif piece == "R":
                        self.getRookMoves(r, d, moves)#gets rook moves
                    elif piece == "B":
                        self.getBishopMoves(r, d, moves)#gets bishop moves
                    elif piece == "K":
                        self.getKingMoves(r, d, moves)#gets king moves
                    elif piece == "Q":
                        self.getQueenMoves(r, d, moves)#gets queen moves
                    elif piece == "N":
                        self.getKnightMoves(r, d, moves)#gets knight moves
                    elif piece == "C":
                        self.getURookMoves(r, d, moves)#gets upgraded rook moves
                    elif piece == "S":
                        self.getUBishopMoves(r, d, moves)#gets upgraded bishop moves
        return moves
#This subroutine allows for extra pieces to be added in the future or be removed easily as 
#so long as there is a symbol for the new piece then it can be added however a new function and 
#way to add the piece must be added

#returns all possible moves for all valid moves

    def getPawnMoves(self, r, d, moves):#moves for pawn
        if self.whiteToMove == True:#white move pawn
            if self.board[r-1][d] == "-": # one move for pawn
                moves.append(Move((r,d), (r-1, d), self.board))
                if r == 6 and self.board[r-2][d] == "-": # two square move for pawn
                    moves.append(Move((r ,d), (r-2, d), self.board))
            if d-1 >= 0: #captures to the left
                if self.board[r-1][d-1][0] == "b":
                    moves.append(Move((r,d), (r-1, d-1), self.board))
            if d+1 <=7:#captures to the right
                if self.board[r-1][d+1][0] == "b":
                    moves.append(Move((r,d), (r-1, d+1), self.board))


        else: # blacks pawn moves
            if self.board[r+1][d] == "-":
                moves.append(Move((r,d), (r+1, d), self.board))
                if r == 1 and self.board[r+2][d] == "-": # two square move for pawn
                    moves.append(Move((r, d), (r+2, d), self.board))
            if d-1 >= 0:#captures to the left
                if self.board[r+1][d-1][0] == "w":
                    moves.append(Move((r,d), (r+1, d-1), self.board))
            if d+1 <= 7:#captures to the right
                if self.board[r+1][d+1][0] == "w":
                    moves.append(Move((r,d), (r+1, d+1), self.board))
                    

    def getKingMoves(self, r, d, moves):
        UMoves = ((-1, -1), (-1, 0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))#all king moves possible
        if self.whiteToMove == True:
            SameColor = "w"
        else:
            SameColor = "b"
        for i in range(8):
            endRow = r + UMoves[i][0]
            endCol = d + UMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != SameColor:
                    moves.append(Move((r, d), (endRow, endCol), self.board))


    def getRookMoves(self, r, d, moves):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) # UP, DOWN, LEFT, RIGHT (order of directions)
        if self.whiteToMove == True:
            ColorEnemy = "b"
        else:
            ColorEnemy = "w"
        for g in directions:
            for i in range(1,8):
                endRow = r + g[0] * i
                endCol = d + g[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "-":
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                    elif endPiece[0] == ColorEnemy:
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break

                
    def getBishopMoves(self, r, d, moves):
        directions = ((-1, -1), (1,-1), (-1,1), (1,1)) #DOWN LEFT, UP LEFT, DOWN RIGHT, UP RIGHT
        if self.whiteToMove == True:
            ColorEnemy = "b"
        else:
            ColorEnemy = "w"
        for g in directions:
            for i in range(1,8):
                endRow = r + g[0] * i
                endCol = d + g[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "-":
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                    elif endPiece[0] == ColorEnemy:
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break
    def getKnightMoves(self, r, d, moves):
        KMoves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (2, 1), (1, -2), (2, -1)) #all knight moves
        if self.whiteToMove == True:#gets knight colour as knight cant capture same pieces
            SameColor = "w"
        else:
            SameColor = "b"
        for m in KMoves:
            endRow = r + m[0]
            endCol = d + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != SameColor:
                    moves.append(Move((r, d), (endRow, endCol), self.board))


    def getQueenMoves(self, r, d, moves):
        directions = ((-1, -1), (1,-1), (-1,1), (1,1), (-1, 0), (1, 0), (0, -1), (0, 1)) #DOWN LEFT, UP LEFT, DOWN RIGHT, UP RIGHT, UP, DOWN, LEFT, RIGHT
        if self.whiteToMove == True:
            ColorEnemy = "b"
        else:
            ColorEnemy = "w"
        for g in directions:
            for i in range(1,8):
                endRow = r + g[0] * i
                endCol = d + g[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "-":
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                    elif endPiece[0] == ColorEnemy:
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break
    def getURookMoves(self, r, d, moves):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) # UP, DOWN, LEFT, RIGHT (order of directions)
        UMoves = ((-1, -1), (1,-1), (-1,1), (1,1))
        if self.whiteToMove == True:
            ColorEnemy = "b"
        else:
            ColorEnemy = "w"
        for i in range(4):
            endRow = r + UMoves[i][0]
            endCol = d + UMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] == ColorEnemy or endPiece[0] == "-":
                    moves.append(Move((r, d), (endRow, endCol), self.board))
        for g in directions:
            for i in range(1,8):
                endRow = r + g[0] * i
                endCol = d + g[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "-":
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                    elif endPiece[0] == ColorEnemy:
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break
    def getUBishopMoves(self, r, d, moves):
        directions = ((-1, -1), (1,-1), (-1,1), (1,1))
        UMoves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        if self.whiteToMove == True:
            ColorEnemy = "b"
        else:
            ColorEnemy = "w"
        for i in range(4):
            endRow = r + UMoves[i][0]
            endCol = d + UMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] == ColorEnemy or endPiece[0] == "-":
                    moves.append(Move((r, d), (endRow, endCol), self.board))
        for g in directions:
            for i in range(1,8):
                endRow = r + g[0] * i
                endCol = d + g[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "-":
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                    elif endPiece[0] == ColorEnemy:
                        moves.append(Move((r, d), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break
""" upgraded rook and upgraded bishop both have a mixture between their own piece movement
and the kings movement i could have used kings function for the piece movement however they
may have been duplicates which should have been removed and could use more of the computers
resources"""
class Move():
#selecting ranks and rows clicks
    ranksToRows = {"1":7, "2":6, "3":5, "4":4,"5": 3, "6":2, "7":1, "8":0} #key for moves of rows for chess notation
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7} #key for moves of columns for chess notation
    ColsToFiles = {v: k for k, v in filesToCols.items()}

#start and end squares for clicks
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = (self.startRow * 1000) + (self.startCol * 100) + (self.endRow * 10) + (self.endCol)
        self.IsPawnPromotion = False # pawn promotion
        self.IsRookPromotion = False # rook promotion
        self.IsBishopPromotion = False # bishop promotion
#if these pieces more to end of their ranks
        if self.pieceMoved == "wP" and self.endRow == 0: #white pawn
            self.IsPawnPromotion = True
        elif self.pieceMoved == "bP" and self.endRow == 7:#black pawn
            self.IsPawnPromotion = True
        elif self.pieceMoved == "wR" and self.endRow == 0:#white rook
            self.IsRookPromotion = True
        elif self.pieceMoved == "bR" and self.endRow == 7:#black rook
            self.IsRookPromotion = True
        elif self.pieceMoved == "wB" and self.endRow == 0:#white bishop
            self.IsBishopPromotion = True
        elif self.pieceMoved == "bB" and self.endRow == 7:#black bishop
            self.IsBishopPromotion = True
        else:
            pass

#overriding equals
        

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        else:
            return False
#get positions from moves for engine
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
#get file rank   
    def getRankFile(self, r, c):
        return self.ColsToFiles[c] + self.rowsToRanks[r]