class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = list()

        for t in tokens:
            if t.isnumeric() or len(t)>2:
                if not t.isnumeric():
                    st.append(int(t[1::])*-1)
                    continue
                    
                st.append(int(t))
                continue
            right = st.pop()
            left = st.pop()

            curr = int()

            if t == '+':
                curr = left + right
            elif t == '-':
                curr = left - right
            elif t == '*':
                curr = left * right
            else:
                curr = int(left / right)
            st.append(curr)
        return st.pop()
            