class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Check for base case
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        f_map = {}
        f_map[s[0]] = 1

        left = 0
        right = 1

        cur_freq, max_freq = 1, 1

        while (right < len(s)):

            if s[right] not in f_map:
                cur_freq += 1
                if cur_freq > max_freq:
                    max_freq = cur_freq
                f_map[s[right]] = 1
                right += 1
            
            else:
                f_map[s[right]] += 1
                cur_freq += 1
                while (f_map[s[right]] > 1):
                    f_map[s[left]] -= 1
                    cur_freq -= 1
                    left += 1
                if cur_freq > max_freq:
                    max_freq = cur_freq
                right += 1


        return max_freq
         






















        # # Set the max_freq value
        # max_freq = 1

        # # Initialize a frequency map
        # f_map = {}
        # f_map[s[0]] = 1

        # # Set the pointers
        # left = 0
        # right = 1

        # # Initialize the current frequency value
        # cur_freq = 1

        # # Iterate over the window
        # length = len(s)

        # while (right < length):

        #     if s[right] not in f_map:
        #         f_map[s[right]] = 1
        #         cur_freq += 1
        #         if cur_freq > max_freq:
        #             max_freq = cur_freq
        #     else:
        #         f_map[s[right]] += 1
        #         # Keep removing s[left] until f_map[s[right]] == 1
        #         while (f_map[s[right]] != 1):
        #             left += 1
        #             if cur_freq > 1:
        #                 cur_freq -= 1
        #             f_map[s[left]] -= 1
        #     # print("Substring: ", s[left:right+1])
        #     # print("Current freq: ", cur_freq)
        #     right += 1
        
        # return max_freq

        # # while (right < length):
        # #     print("Looking at: ", s[left:right+1])
        # #     if s[right] not in f_map or f_map[s[right]] == 0:
        # #         print("Entered if")
        # #         cur_freq += 1
        # #         if cur_freq > max_freq:
        # #             max_freq += 1
        # #         right += 1
            
        # #     else:
        # #         print("Entered else")
        # #         print("s[left]: ", s[left])
        # #         print("s[right]: ", s[right])
        # #         while (right < length and f_map[s[right]] > 0):
        # #             print("Entered while!")
        # #             f_map[s[left]] -= 1
        # #             left += 1
        # #             if left == right:
        # #                 right += 1
        # #                 if s[right] not f_map:
        # #                     f_map[s[right]] = 1
        # #             cur_freq -= 1
        # #             print("New substring: ", s[left:right+1])
        # #         if right < length:
        # #             f_map[s[right]] = 1
        # #             right += 1
        # #     print("max_freq: ", max_freq)
        # #     print("------")
        
        # return max_freq