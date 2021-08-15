#Check if the Sentence Is Pangram
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for num in range(26):
            if chr(num+97) not in sentence:
                return False
        return True

n = input("Enter the string :")
print(Solution().checkIfPangram(n))
