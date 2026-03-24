class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        out = ""

        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                break
            # check if divisor of 1
            check = str1
            checkValid = True

            while check:
                # print(check, str1[:i+1])
                if check[:i+1] != str1[:i+1]:
                    checkValid = False
                    break

                check = check[i+1::]

            if not checkValid:
                continue

            check = str1[:i+1]
            checkValid = True

            while check:
                if check[:i+1] != str1[:i+1]:
                    checkValid = False
                    break

                check = check[i+1::]

            if not checkValid:
                continue

            out = str1[:i+1]

        return out