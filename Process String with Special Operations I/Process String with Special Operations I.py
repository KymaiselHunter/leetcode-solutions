class Solution:
    def processStr(self, s: str) -> str:
        st = list()

        for c in s:
            if c.isalpha():
                st.append(c)
                continue

            if c == '#':
                st += st
                continue

            if c == '%':
                st = st[::-1]
                continue

            if st:#c == '*':
                st.pop()

        return "".join(st)