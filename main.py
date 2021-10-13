"""
K = set of keys (symbolic names)
A = set of positions (|A| = m; m –prime number)
h: K -> A
    h(k) = (val(k) mod m) + 1
"""

import sympy.ntheory as np


class SymbolTable:
    def __init__(self):
        self.__m = 11
        self.__st = [[] for _ in range(self.__m)]
        self.__occupancy = 0

    def hash(self, token):
        s = 0
        for character in token:
            s += ord(character)
        return s % self.__m

    def rehash(self):
        self.__m = np.nextprime(self.__m)  # get the next prime number
        st = [[] for _ in range(self.__m)]

        for ll in self.__st:
            for elem in ll:
                st[self.hash(elem)].append(elem)

        self.__st = st

    def add(self, token):
        key = self.hash(token)
        if token in self.__st[key]:
            return key, self.__st[key].index(token)
        self.__st[key].append(token)
        self.__occupancy += 1

        if self.__occupancy / self.__m > 0.8:
            self.rehash()
            key = self.hash(token)

        return key, self.__st[key].index(token)


if __name__ == '__main__':
    st = SymbolTable()

    # even if for my language I can't have aa2a or 2aaa
    # I used them for testing

    print(st.add("2aaaa"))
    print(st.add("a2aaa"))
    print(st.add("aa2aa"))
    print(st.add("aaa2a"))
    print(st.add("aaaa2"))
    print(st.add("2aaa"))
    print(st.add("a2aa"))
    print(st.add("aa2a"))
    print(st.add("aaa2"))
    print(st.add("2bbb"))
    print(st.add("b2bb"))
    print(st.add("bb2b"))
    print(st.add("bbb2"))
    print(st.add("aaa"))
    print(st.add("aaa"))
    print(st.add("aaa"))
