class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def get_child(self, ch: str):
        return self.children.get(ch, None)

    def add_child(self, ch) -> bool:
        if self.get_child(ch) is not None:
            return False

        self.children[ch] = TrieNode()
        return True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, str_: str) -> bool:
        prev = self.root

        for idx in range(0, len(str_)):
            ch = str_[idx]
            curr = prev.get_child(ch)

            if curr is not None:
                prev = curr
                continue

            prev.add_child(ch)
            curr = prev.get_child(ch)
            prev = curr

        prev.is_end = True

        return True

    def contains(self, str_: str) -> list:
        indices = []
        prev = self.root

        for idx in range(0, len(str_)):
            ch = str_[idx]
            curr = prev.get_child(ch)

            if curr is None:
                break

            if curr.is_end:
                indices.append(idx)

            prev = curr

        return indices

    def __str__(self):
        return ""
