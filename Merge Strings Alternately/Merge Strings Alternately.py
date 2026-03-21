class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer = 0
        newWord = list()

        while pointer < len(word1) or pointer < len(word2):
            if pointer >= len(word1):
                newWord += word2[pointer::]
                break
            if pointer >= len(word2):
                newWord += word1[pointer::]
                break

            newWord.append(word1[pointer])
            newWord.append(word2[pointer])

            pointer += 1

        return "".join(newWord)