# Leetcode 14. Longest Common Prefix 
# Given: Array of strings -> return longest common prefix amongst all or "" if no common prefix.

# ex1: strs = ["flower", "flow", "flight"] -> "fl" is the answer

def longesCommonPrefix(strs: list[str]) -> str:
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res

print(longesCommonPrefix(["flower","flow","flight"]))