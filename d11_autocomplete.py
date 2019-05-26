WORDS = ['foo', 'bar', 'dog', 'dogs', 'done']
# def autocomplete(s):
#     results = set()
#     for word in WORDS:
#         if word.startswith(s):
#             results.add(word)
#     return results

ENDS_HERE = '__ENDS_HERE'

class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            # print(c," ",v)
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

trie = Trie()
for word in WORDS:
    trie.insert(word)

def autocomplete(s):
    suffixes = trie.elements(s)
    return [s + w for w in suffixes]

print(autocomplete("do"))