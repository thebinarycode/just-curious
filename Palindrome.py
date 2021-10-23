from collections import Counter

class Palindrome:
    """class would return 0 if given word is palindrome, -1 if word cannot be framed as a palindrome or numerical value
    indicating the minimum steps required to form palindrome by shuffling only adjacent letters"""

    def check_if_palindrome(self, inputword: str) -> tuple:
        """to check if provided word is already a palindrome or reordered word can be formed as palindrome"""

        print(f"given word: {inputword}")
        reversedword = "".join(reversed(inputword))

        if inputword == reversedword:
            return 0

        charcount = Counter(inputword)
        oddoccurance = [key for key, value in charcount.items() if value % 2]
        if len(oddoccurance) > 1: return -1
        else:
            return self.calculate_steps(list(inputword), charcount)

    def calculate_steps(self, inputword: list, charcount: dict) -> tuple:
        totalswaps = 0
        startindex, endindex = 0, len(inputword) - 1

        print(f"initial order: {inputword}")

        while startindex < endindex:
            if inputword[startindex] == inputword[endindex]:
                startindex += 1
                endindex -= 1
            else:
                tmpindex = endindex

                while tmpindex > startindex and inputword[startindex] != inputword[tmpindex]:
                    tmpindex -= 1

                if tmpindex == startindex:
                    inputword[swapindex], inputword[swapindex + 1] = inputword[swapindex + 1], inputword[swapindex]
                    totalswaps += 1
                    print(f"step {totalswaps} order: {inputword}")
                    continue

                for swapindex in range(tmpindex, endindex):
                    inputword[swapindex], inputword[swapindex + 1] = inputword[swapindex + 1], inputword[swapindex]
                    totalswaps += 1
                    print(f"step {totalswaps} order: {inputword}")

                startindex += 1
                endindex -= 1

        return totalswaps, "".join(inputword)


obj = Palindrome()
word = "aaaabbc"
print(f"total swaps for string: {word} is {obj.check_if_palindrome(word)[0]}, "
      f"swapped word: {obj.check_if_palindrome(word)[1]}")




