class Piece:
    def __init__(self, horizontal_pos, vertical_pos, player):
        self.horizontal_pos = horizontal_pos
        self.vertical_pos = vertical_pos
        self.player = player

    def move_to(self, new_horizontal_pos, new_vertical_pos):
        self.horizontal_pos = new_horizontal_pos
        self.vertical_pos = new_vertical_pos
        return

    def get_valid_positions(self):
        raise NotImplementedError("Method not implemented for subclass")


class Pawn(Piece):
    def __init__(self, horizontal_pos, vertical_pos, player):
        super().__init__(horizontal_pos, vertical_pos, player)


class Knight(Piece):
    def __init__(self, horizontal_pos, vertical_pos, player):
        super().__init__(horizontal_pos, vertical_pos, player)


class Bishop(Piece):
    def __init__(self, horizontal_pos, vertical_pos, player):
        super().__init__(horizontal_pos, vertical_pos, player)


class Tower(Piece):
    def __init__(self, horizontal_pos, vertical_pos, player):
        super().__init__(horizontal_pos, vertical_pos, player)


class Queen(Piece):
    def __init__(self, horizontal_pos, vertical_pos, player):
        super().__init__(horizontal_pos, vertical_pos, player)


class King(Piece):
    def __init__(self, horizontal_pos, vertical_pos, player):
        super().__init__(horizontal_pos, vertical_pos, player)
