'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len_of_substring = 0
        chars_in_substring = dict()
        substring_start_index = 0
        for index, char in enumerate(s):
            if char in chars_in_substring:
                print(char, substring_start_index, chars_in_substring[char])
                substring_start_index = max(chars_in_substring[char], substring_start_index)

            chars_in_substring[char] = index + 1
            max_len_of_substring = max(max_len_of_substring, index - substring_start_index + 1)

        return max_len_of_substring

if __name__ == "__main__":
    solution = Solution()
    s = "asdasd"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "abcabcbb"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "aaabccddbcad"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "abcad"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "bbtablud"
    print(s, solution.lengthOfLongestSubstring(s))

    s = "bbtatlud"
    print(s, solution.lengthOfLongestSubstring(s))

    s = ""
    print(s, solution.lengthOfLongestSubstring(s))