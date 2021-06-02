# ["a", "bcd", "e"]

# str = " a bcd e "
# read how many times of this str

# #point: what's next?
# -a-bcd-e
#       v
#      v
#     v
# 1) case 1: reach "-", have_rd +=1
# 2) case 2: next_val is "-", have_rd +=2
# 3) case 3: back before - 
# |-----------|
# iterate num_row_time, 
# every time cur_idx += cols
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):

        rd = 0 
        s = " ".join(sentence)  + " "
        for _ in range(rows):
            rd = rd + cols -1
            if s[rd%len(s)] == " ":
                rd += 1
            elif s[(rd+1)%len(s)] == " ":
                rd += 2
            else:
                while s[ rd % len(s)]!= " ":
                    rd -= 1
                rd += 1
              
       
        return rd / len(s)ls