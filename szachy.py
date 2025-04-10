def Game():
    chessboard = [["R", "Kn", "B", "Q", "K", "B", "Kn", "R"],
                  ["P", "P", "P", "P", "P", "P", "P", "P"],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  ["P", "P", "P", "P", "P", "P", "P", "P"],
                  ["R", "Kn", "B", "Q", "K", "B", "Kn", "R"]]
    

    def printBoard(board):
        print("  a  b  c  d  e  f  g  h")
        for i in range(8):
            print(8 - i, end=" ")
            for j in range(8):
                print(f"[{board[i][j]:2}]", end="")
            print()

    printBoard(chessboard)

    gameOver = False
    while not gameOver:
        printBoard(chessboard)
        whichFigure = input("Wpisz figurę (R, Kn, B, Q, K, P): ")
        whichSquare = input("Wpisz pole figury (np. e2): ")
        whichCol = ZamianaZLiterek(whichSquare[0])
        whichRow = 8 - int(whichSquare[1])

        match whichFigure:
            case "R":
                Rook(whichCol, whichRow, chessboard)
            case "Kn":
                Knight(whichCol, whichRow, chessboard)
            case "B":
                Bishop(whichCol, whichRow, chessboard)
            case "Q":
                Queen(whichCol, whichRow, chessboard)
            case "K":
                King(whichCol, whichRow, chessboard)
            case "P":
                Pawn(whichCol, whichRow, chessboard)
            case _:
                print("Niepoprawna figura.")


    match whichFigure:
        case "R":
            Rook(whichCol, whichRow ,chessboard )
            for i in range(0,8):
                for j in range(0,8):
                    print(f"[{chessboard[i][j]}]", end="")
                    if j == 7:
                        print("\n")
        case "Kn":
            Knight(whichCol, whichRow ,chessboard)
            for i in range(0,8):
                for j in range(0,8):
                    print(f"[{chessboard[i][j]}]", end="")
                    if j == 7:
                        print("\n")
        case "B":
            Bishop(whichCol, whichRow ,chessboard )
            for i in range(0,8):
                for j in range(0,8):
                    print(f"[{chessboard[i][j]}]", end="")
                    if j == 7:
                        print("\n")
        case "Q":
            Queen(whichCol, whichRow ,chessboard)
            for i in range(0,8):
                for j in range(0,8):
                    print(f"[{chessboard[i][j]}]", end="")
                    if j == 7:
                        print("\n")
        case "K":
            King(whichCol, whichRow ,chessboard )
            for i in range(0,8):
                for j in range(0,8):
                    print(f"[{chessboard[i][j]}]", end="")
                    if j == 7:
                        print("\n")
        case "P":
            Pawn(whichCol, whichRow ,chessboard )
            for i in range(0,8):
                for j in range(0,8):
                    print(f"[{chessboard[i][j]}]", end="")
                    if j == 7:
                        print("\n")



def ZamianaZLiterek(lit):
    return ord(lit) - 1

def ZamianaNaPole(row, col):
    return f"{row}{chr(col + ord('a'))}"





def Pawn(whichCol, whichRow, chessboard):
    listOfLegalMoves = []
    rowIndex = 8 - int(whichRow)
    colIndex = ZamianaZLiterek(whichCol)

    if rowIndex + 1 <= 7 and chessboard[rowIndex + 1][colIndex] == " ":
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 1, colIndex))

    if rowIndex == 1 and chessboard[rowIndex + 2][colIndex] == " " and chessboard[rowIndex + 1][colIndex] == " ":
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 2, colIndex))

    print("Możliwe ruchy:", listOfLegalMoves)

    whereGo = input("Podaj pole docelowe (np. e4): ")
    whereGoCol = ZamianaZLiterek(whereGo[0])
    whereGoRow = 8 - int(whereGo[1])

    chessboard[rowIndex][colIndex] = " "
    chessboard[whereGoRow][whereGoCol] = "P"

    return chessboard

def Bishop(whichCol, whichRow, chessboard):
    listOfLegalMoves = []
    rowIndex = 8 - int(whichRow)
    colIndex = ZamianaZLiterek(whichCol)

    for i in range(1, 8):
        if 0 <= rowIndex + i <= 7 and 0 <= colIndex + i <= 7:
            if chessboard[rowIndex + i][colIndex + i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex + i))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex + i))
                break

    for i in range(1, 8):
        if 0 <= rowIndex - i <= 7 and 0 <= colIndex - i <= 7:
            if chessboard[rowIndex - i][colIndex - i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex - i))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex - i))
                break

    for i in range(1, 8):
        if 0 <= rowIndex + i <= 7 and 0 <= colIndex - i <= 7:
            if chessboard[rowIndex + i][colIndex - i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex - i))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex - i))
                break

    for i in range(1, 8):
        if 0 <= rowIndex - i <= 7 and 0 <= colIndex + i <= 7:
            if chessboard[rowIndex - i][colIndex + i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex + i))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex + i))
                break

    print("Możliwe ruchy:", listOfLegalMoves)

    whereGo = input("Podaj pole docelowe (np. e4): ")
    whereGoCol = ZamianaZLiterek(whereGo[0])
    whereGoRow = 8 - int(whereGo[1])

    chessboard[rowIndex][colIndex] = " "
    chessboard[whereGoRow][whereGoCol] = "B"

    return chessboard
    
def Rook(whichCol, whichRow, chessboard):
    listOfLegalMoves = []
    rowIndex = 8 - int(whichRow)
    colIndex = ZamianaZLiterek(whichCol)

    for i in range(1, 8):
        if rowIndex + i <= 7:
            if chessboard[rowIndex + i][colIndex] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex))
                break

    for i in range(1, 8):
        if rowIndex - i >= 0:
            if chessboard[rowIndex - i][colIndex] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex))
                break

    for i in range(1, 8):
        if colIndex - i >= 0:
            if chessboard[rowIndex][colIndex - i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex - i))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex - i))
                break

    for i in range(1, 8):
        if colIndex + i <= 7:
            if chessboard[rowIndex][colIndex + i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex + i))
            else:
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex + i))
                break

    print("Możliwe ruchy:", listOfLegalMoves)

    whereGo = input("Podaj pole docelowe (np. e4): ")
    whereGoCol = ZamianaZLiterek(whereGo[0])
    whereGoRow = 8 - int(whereGo[1])

    chessboard[rowIndex][colIndex] = " "
    chessboard[whereGoRow][whereGoCol] = "R"

    return chessboard

def Queen(whichCol, whichRow, chessboard):
    listOfLegalMoves = []

    colIndex = ord(whichCol) - ord('a')
    rowIndex = 8 - int(whichRow)  # Zamiana na indeksy

    # Kierunek +1 +1
    for i in range(1, 8):
        if 0 <= colIndex + i <= 7 and 0 <= rowIndex + i <= 7:
            if chessboard[rowIndex + i][colIndex + i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex + i))
            elif chessboard[rowIndex + i][colIndex + i] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex + i))
                break

    # Kierunek -1 -1
    for i in range(1, 8):
        if 0 <= colIndex - i <= 7 and 0 <= rowIndex - i <= 7:
            if chessboard[rowIndex - i][colIndex - i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex - i))
            elif chessboard[rowIndex - i][colIndex - i] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex - i))
                break

    # Kierunek -1 1
    for i in range(1, 8):
        if 0 <= colIndex - i <= 7 and 0 <= rowIndex + i <= 7:
            if chessboard[rowIndex + i][colIndex - i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex - i))
            elif chessboard[rowIndex + i][colIndex - i] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex - i))
                break

    # Kierunek 1 -1
    for i in range(1, 8):
        if 0 <= colIndex + i <= 7 and 0 <= rowIndex - i <= 7:
            if chessboard[rowIndex - i][colIndex + i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex + i))
            elif chessboard[rowIndex - i][colIndex + i] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex + i))
                break

    # Kierunek do góry
    for i in range(1, 8):
        if 0 <= rowIndex + i <= 7:
            if chessboard[rowIndex + i][colIndex] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex))
            elif chessboard[rowIndex + i][colIndex] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex + i, colIndex))
                break

    # Kierunek do dołu
    for i in range(1, 8):
        if 0 <= rowIndex - i <= 7:
            if chessboard[rowIndex - i][colIndex] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex))
            elif chessboard[rowIndex - i][colIndex] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex - i, colIndex))
                break

    # Kierunek lewo
    for i in range(1, 8):
        if 0 <= colIndex - i <= 7:
            if chessboard[rowIndex][colIndex - i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex - i))
            elif chessboard[rowIndex][colIndex - i] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex - i))
                break

    # Kierunek na prawo
    for i in range(1, 8):
        if 0 <= colIndex + i <= 7:
            if chessboard[rowIndex][colIndex + i] == " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex + i))
            elif chessboard[rowIndex][colIndex + i] != " ":
                listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex + i))
                break

    print("Możliwe ruchy:", listOfLegalMoves)

    whereGo = input("Podaj pole docelowe (np. e4): ")

    whereGoCol = ord(whereGo[0]) - ord('a')
    whereGoRow = 8 - int(whereGo[1])  # Zamiana na indeksy

    chessboard[rowIndex][colIndex] = " "
    chessboard[whereGoRow][whereGoCol] = "Q"

    return chessboard


def King(whichCol, whichRow, chessboard):
    listOfLegalMoves = []

    colIndex = ord(whichCol) - ord('a')
    rowIndex = 8 - int(whichRow)  # Zamiana na indeksy

    # Prawo
    if 0 <= colIndex + 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex + 1))
    # Lewo
    if 0 <= colIndex - 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex, colIndex - 1))
    # Góra
    if 0 <= rowIndex + 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 1, colIndex))
    # Dół
    if 0 <= rowIndex - 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 1, colIndex))
    # Prawy górny
    if 0 <= colIndex + 1 <= 7 and 0 <= rowIndex + 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 1, colIndex + 1))
    # Prawy dolny
    if 0 <= colIndex + 1 <= 7 and 0 <= rowIndex - 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 1, colIndex + 1))
    # Lewy górny
    if 0 <= colIndex - 1 <= 7 and 0 <= rowIndex + 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 1, colIndex - 1))
    # Lewy dolny
    if 0 <= colIndex - 1 <= 7 and 0 <= rowIndex - 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 1, colIndex - 1))

    print("Możliwe ruchy:", listOfLegalMoves)

    whereGo = input("Podaj pole docelowe (np. e4): ")

    whereGoCol = ord(whereGo[0]) - ord('a')
    whereGoRow = 8 - int(whereGo[1])  

    chessboard[rowIndex][colIndex] = " "
    chessboard[whereGoRow][whereGoCol] = "K"

    return chessboard


def Knight(whichCol, whichRow, chessboard):
    listOfLegalMoves = []

    colIndex = ord(whichCol) - ord('a')
    rowIndex = 8 - int(whichRow) 

    # Do góry i na prawo
    if 0 <= colIndex + 1 <= 7 and 0 <= rowIndex + 2 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 2, colIndex + 1))
    # Do góry i na lewo
    if 0 <= colIndex - 1 <= 7 and 0 <= rowIndex + 2 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 2, colIndex - 1))
    # Do dołu i na prawo
    if 0 <= colIndex + 1 <= 7 and 0 <= rowIndex - 2 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 2, colIndex + 1))
    # Do dołu i na lewo
    if 0 <= colIndex - 1 <= 7 and 0 <= rowIndex - 2 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 2, colIndex - 1))
    # Na prawo i do góry
    if 0 <= colIndex + 2 <= 7 and 0 <= rowIndex + 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 1, colIndex + 2))
    # Na prawo i do dołu
    if 0 <= colIndex + 2 <= 7 and 0 <= rowIndex - 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 1, colIndex + 2))
    # Na lewo i do góry
    if 0 <= colIndex - 2 <= 7 and 0 <= rowIndex + 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex + 1, colIndex - 2))
    # Na lewo i do dołu
    if 0 <= colIndex - 2 <= 7 and 0 <= rowIndex - 1 <= 7:
        listOfLegalMoves.append(ZamianaNaPole(rowIndex - 1, colIndex - 2))

    print("Możliwe ruchy:", listOfLegalMoves)

    whereGo = input("Podaj pole docelowe (np. e4): ")

    whereGoCol = ord(whereGo[0]) - ord('a')
    whereGoRow = 8 - int(whereGo[1])  # Zamiana na indeksy

    chessboard[rowIndex][colIndex] = " "
    chessboard[whereGoRow][whereGoCol] = "Kn"

    return chessboard
   
Game()