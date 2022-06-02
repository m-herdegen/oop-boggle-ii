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
                  # self.board_list.append(new_letter)
                  if new_letter == 'Q':
                        self.board += new_letter + 'u '
                        self.board_list.append(new_letter + 'u')
                  else:
                        self.board += new_letter + '  '
                        self.board_list.append(new_letter)
            self.board += '\n'

            print('{:}'.format(self.board))
            #print(self.board_list)

            return self.board_list

      def include_word(self, word):
            temp = []
            temp2 = []
            horizontal_list = []
            vertical_list = []
            diagonal_list = []
            master_list = []
            
            for value in self.board_list:

                  temp.append(value)
                  if len(temp) == 4:
                        horizontal_list.append(temp)
                        master_list.append(temp)
                        master_list.append(temp[::-1])
                        temp = []

            for i in range(4):
                  for value in horizontal_list:
                        temp.append(value[i])
                  vertical_list.append(temp)
                  master_list.append(temp)
                  master_list.append(temp[::-1])
                  temp = []

            for j,value in enumerate(horizontal_list):
                  for i, val in enumerate(value):
                        if j == i:
                              temp.append(val)
                        elif i + j == 3:
                              temp2.append(val)

            diagonal_list.append(temp)
            master_list.append(temp)
            master_list.append(temp[::-1])
            diagonal_list.append(temp2)
            master_list.append(temp2)
            master_list.append(temp2[::-1])


            # print(*master_list)

            if list(word.upper()) in master_list:
                  return True 
            return False




board_new = BoggleBoard()
board_new.shake()
print(board_new.include_word('U')) # => True or False