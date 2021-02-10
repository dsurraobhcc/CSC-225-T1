make_word = ''
found_block_index = []

def can_make_word(word):
   blocks = [('B', 'O'), ('X', 'K'), ('D', 'Q'), ('C', 'P'), ('N', 'A'), ('G', 'T'), ('R', 'E'), ('T', 'G'), ('Q', 'D'), ('F', 'S'), ('J', 'W'), ('H', 'U'), ('V', 'I'), ('A', 'N'), ('O', 'B'), ('E', 'R'), ('F', 'S'), ('L', 'Y'), ('P', 'C'), ('Z', 'M')]

   for letter in word:
      for i in range(len(blocks)):
         if i in found_block_index:
            continue
         else:
            if letter in blocks[i]:  
               # track index of found block
               found_block_index.append(i)
               #build word:
               global make_word
               make_word += letter
               not_found = False
               break
            else:
               not_found = True

      if not_found: 
         print('cannot make a word')
         break

print(can_make_word("BARK"))