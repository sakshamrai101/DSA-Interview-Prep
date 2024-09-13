class Bishop:
     def move(self):
          print("Bishop moves diagonally")
     
class Knights:
     def move(self):
          print("Knights move two square vertically")


def move_test(chess_Piece):
     chess_Piece.move()


bishop = Bishop()
knight = Knights()

move_test(bishop)
move_test(knight)

