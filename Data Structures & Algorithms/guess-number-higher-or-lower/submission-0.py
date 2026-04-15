# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n - 1

        while True:
            curr_guess = (l + r) // 2
            guess_output = guess(curr_guess) 

            if guess_output == 0:
                return curr_guess 

            elif guess_output == -1:
                r = curr_guess - 1

            else:
                l = curr_guess + 2