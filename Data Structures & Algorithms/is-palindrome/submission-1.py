class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Approach 2: Two pointers
        l, r = 0, len(s) - 1

        #loop over the strings from both sides and stop when l == r or l > r
        while l < r:
            #while left pointer is smaller than right pointer, but if it's not alnum, then skip that char, i.e, move the pointer to the right.
            while l < r and not self.isAlnum(s[l]):
                l += 1
            #while right pointer is larger than left pointer, but if it's not alnum, then skip that char, i.e, move the pointer to the left.
            while r > l and not self.isAlnum(s[r]):
                r -= 1
            #now, when both characters are Alnum, check whether are equivalent or not, if not equivalent, return False.
            if s[l].lower() != s[r].lower():
                return False
            # if the characters are equal, shift both pointers up
            l , r = l + 1, r - 1
        # if at the end of the loop, none of the above conditions have trigerred a False outcome, then the string must be a valid palindrome.
        return True

        #define a function to determine whether a character is alnum.
    def isAlnum(self, c: str) -> bool:
        if  (ord('A') <= ord (c) <= ord('Z')  or
            ord ('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')):
            return True
        else:
            return False