#Keyboard Row

class Solution:
    def findWords(self, words):
        word_list=[]
        top_row=set('qwertyuiop')
        mid_row=set('asdfghjkl')
        bottom_row=set('zxcvbnm')
        for word in words:
            if set(word.lower()).issubset(top_row) or set(word.lower()).issubset(mid_row) or set(word.lower()).issubset(bottom_row):
                word_list.append(word)
        return word_list

n=int(input("Enter size : "))
c=[]
for i in range(n):
    s=input()
    c.append(s)

print(Solution().findWords(c))