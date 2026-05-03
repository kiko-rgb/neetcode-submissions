class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - ord('a')] += 1
            # print(char_count)
            # print(tuple(char_count))
            sorted_words[tuple(char_count)].append(word)
            
            # print(sorted_words)


        return list(sorted_words.values())
                

        