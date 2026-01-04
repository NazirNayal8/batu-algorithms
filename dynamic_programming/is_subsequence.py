
# two ways to iterate over a string
# Method 1: Using a for loop with index
# for i in range(len(s)):
# #     print(s[i])
# Method 2: Using a for loop directly over characters
# for char in s:
# #     print(char)

def is_subsequence(s, t):
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
        if i == len(s):
            return True
    return False


if __name__ == "__main__":
    s = "abcd"
    t = "ahbgdck"
    print(is_subsequence(s, t))