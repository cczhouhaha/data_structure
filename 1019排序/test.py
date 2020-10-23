# c = "cd"
# # print(c[2:5])
# def hui(s):
#     for head in range(0, int(len(s) / 2)):
#         end = len(s) - 1
#         while head <= end:
#             if s[head] != s[end]:
#                 end -= 1
#                 print(s[head:end])
#             print(s[head:end])
# hui(c)

# def longestPalindrome( s) :
#     for head in range(len(s) - 1):
#         end = len(s) - 1
#         while head < end:
#             if s[head] != s[end]:
#                 end -= 1
#             if s[head] == s[end]:
#                 return s[head:end]
#

class Solution:
    def longestpalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        if length == 1 or s == s[::-1]:
            return s
        max_len, start = 1, 0
        for i in range(1, length):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]


if __name__ == '__main__':
    ss = Solution()
    str1 = "aesgfdfg"
    result = ss.longestpalindrome(str1)
    print(result)



