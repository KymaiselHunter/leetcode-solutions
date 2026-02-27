class Solution:
    def numSteps(self, s: str) -> int:
        output = 0 

        while s != '1':
            # print(s)
            output += 1 
            if s[-1] == '0':
                s = s[0:-1]
                continue
            
            new = "0"
            add = True

            for index in range(len(s)-2,-1,-1):
                bit = s[index]
                if not add:
                    new = bit + new
                    continue
                
                if bit == '0':
                    new = '1' + new
                    add = False
                    continue
                
                new = '0' + new

            if add:
                new = '1' + new
            
            s = new

        return output