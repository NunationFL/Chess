from logic.Piece import Bishop, King, Knight, Pawn, Queen, Tower


class Board:
    def __init__(self):
        self.board = []

        # Add black pieces
        aux = []
        aux.append(Tower(7,0,2))
        aux.append(Knight(7,1,2))
        aux.append(Bishop(7,2,2))
        aux.append(King(7,3,2))
        aux.append(Queen(7,4,2))
        aux.append(Bishop(7,5,2))
        aux.append(Knight(7,6,2))
        aux.append(Tower(7,7,2))
        self.board.append(aux)

        # Add black pawns
        aux = []
        for i in range(8):
            aux.append(Pawn(6,i,2))
        self.board.append(aux)

        
        for _ in range(4):
            aux = []
            for _ in range(8):
                aux.append(None)
            self.board.append(aux)

        # Add white pawns
        aux = []
        for i in range(8):
            aux.append(Pawn(1,i,1))
        self.board.append(aux)

        # Add white pieces
        aux=[]
        aux.append(Tower(0,0,1))
        aux.append(Knight(0,1,1))
        aux.append(Bishop(0,2,1))
        aux.append(Queen(0,3,1))
        aux.append(King(0,4,1))
        aux.append(Bishop(0,5,1))
        aux.append(Knight(0,6,1))
        aux.append(Tower(0,7,1))
        self.board.append(aux)

            
                
    
    def pos_is_occupied():

        return
    
    def pos_is_occupied_by_king():

        return
