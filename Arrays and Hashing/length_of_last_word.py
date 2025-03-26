# Leetcode 58: Length of Last Word (Easy)
# Given: string s(words + spaces) -> return length of last word

def lengthOfLastWord(s: str) -> int:
        
    longest_word = []

    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            r = i
            while s[r] != " " and r >= 0:
                longest_word.append(s[r])
                r -= 1
        if len(longest_word) != 0:
            break

    return len(longest_word)

print(lengthOfLastWord("a "))