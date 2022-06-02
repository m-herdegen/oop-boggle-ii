# You should re-use and modify your old BoggleBoard class to support the new requirements
import random 

class BoggleBoard:

      dice_list = []

      for i in range(16):
            die = []
            for x in range(6):
                  die.append((chr(random.randint(ord('A'), ord('Z')))))
            dice_list.append(die)
            random.shuffle(dice_list)

      def __init__(self):
            self.board = ''
            for x in range(16):
                  if x % 4 == 0:
                        self.board += '\n'
                  self.board += '_'
            self.board += '\n'
            print(*self.board)

      def shake(self):
            self.board = ''
            new_letter = ''
            self.board_list = []
            for i, x in enumerate(BoggleBoard.dice_list):
                  if i % 4 == 0:
                        self.board += '\n'
                  new_letter = x[random.randint(0, 5)]
                  self.board_list.append(new_letter)
                  if new_letter == 'Q':
                        self.board += new_letter + 'u '
                  else:
                        self.board += new_letter + '  '
            self.board += '\n'

            print('{:}'.format(self.board))
            #print(self.board_list)

            return self.board_list

      def include_word(self):
            temp = []
            horizontal_list = []
            vertical_list = []
            diagonal_list = []

            for value in self.board_list:

                  temp.append(value)
                  if len(temp) == 4:
                        horizontal_list.append(temp)
                        temp = []

            for i in range(4):
                  for value in horizontal_list:
                        temp.append(value[i])
                  vertical_list.append(temp)
                  temp = []
                        
            print(*vertical_list)
                  

            print(*horizontal_list)




board_new = BoggleBoard()
board_new.shake()
board_new.include_word() # => True or False