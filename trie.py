"""
.. module:: Trie
   :synopsis: API implementing a Trie structured to be used for autocomplete use cases

.. moduleauthor:: Diogo Pires <diogo.fpmp.pires@gmail.com>

"""


class Node(object):
    """
    This class implements Nodes of a Trie.

    Normal usage of the class is

    >>> n = Node("d")
    >>> n.add_child("da")
    >>> n
    <data --> d (children=['da'])>
    >>> n["da"]
    <data --> da (children=[])>
    >>> n["daa"]
    Traceback (most recent call last):
    ...
    KeyError: 'daa'
    """

    CNT = -1 # Starts at -1 because the head node of a Trie has no data

    def __init__(self, data=None, label=None):
        """
        :param data: The identifier of the node in the Trie
        :type data: str
        :param label: A label of the node
        :type label: str
        :returns: None
        """
        self.data = data
        self.label = label
        self.children = {}
        self.is_key = False
        Node.CNT += 1

    def add_child(self, data):
        """
        Add child to node.

        :param data: The identifier of the node in the Trie
        :type data: str
        """
        self.children[data] = Node(data)

    def __getitem__(self, data):
        """
        Get node from children.

        :param data: The identifier of the node in the Trie
        :type data: str
        :raises: KeyError
        """
        try:
            return self.children[data]
        except KeyError:
            raise KeyError("The node ID requested does not exist in the children of " + \
                           "node with ID {} and label {}".format(self.data, self.label))

    def __repr__(self):
        return "<data --> {} (children={})>".format(self.data, list(self.children.keys()))


class Trie(object):
    """
    This class implements a Trie data structure using BFS as the search algorithm within the Trie

    Normal usage of the class should be done from the UI/UX interface
    by calling the Trie.from_prefix method for every character chosen by 
    the user.

    Nonetheless, an example is

    >>> t = Trie()
    >>> words = ["Dartford", "Dartmouth", "Tower Hill",
    ...          "Derby", "Liverpool", "Liverpool Line Street",
    ...          "Paddington", "Euston", "London Bridge", "Victoria"]
    >>> t.add_words(words)
    >>> t.from_prefix("Liverpool")
    {'matches': ['Liverpool', 'Liverpool Line Street'], 'next_chars': [' ']}
    >>> t.from_prefix("X")
    {'matches': [], 'next_chars': []}
    """

    def __init__(self):
        self.head = Node()

    def __repr__(self):
        return "<trie with {} nodes>".format(Node.CNT)

    def _add_word(self, word):
        """
        Add word to Trie. Used internally during load period before Trie is used.
    
        :param word: String to be inserted as a node in the Trie
        :type word: str
        :raises: TypeError
        """
        if not isinstance(word, str):
            raise TypeError("'word' needs to be a string")

        cur_node = self.head
        word_norm = word.encode("utf8").lower()
        finished = True

        for idx, value in enumerate(word_norm):
            if value in cur_node.children:
                cur_node = cur_node.children[value]
            else:
                finished = False
                break

        if not finished:
            while idx < len(word_norm):
                cur_node.add_child(word_norm[idx])
                cur_node = cur_node.children[word_norm[idx]]
                idx += 1
        cur_node.data = word_norm
        cur_node.label = word
        cur_node.is_key = True

    def add_words(self, words):
        """
        Add list of words to Trie. Should be used during load period before Trie is used.
    
        :param words: List of strings to be inserted as nodes in the Trie
        :type word: list
        :raises: TypeError
        """
        if not isinstance(words, list):
            raise TypeError("'words' needs to be a list")
        
        for entry in words:
            self._add_word(entry)

    def from_prefix(self, prefix):
        """
        Check what are the possible words given a prefix. Uses BFS search.
    
        :param prefix: String from which to check the possible words in the Trie
        :type prefix: str
        :returns: Dictionary with the possible words and the next available characters
        :raises: ValueError, TypeError
        """
        if prefix is None:
            raise ValueError("'prefix' cannot be null")
        if not isinstance(prefix, str):
            raise TypeError("'prefix' needs to be a string")

        result = set()
        prefix_norm = prefix.encode("utf8").lower()

        # Computing top node for BFS search
        top_node = self.head
        for letter in prefix_norm:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                result_out = {}
                result_out["matches"] = []
                result_out["next_chars"] = []
                return result_out

        # BFS search
        if top_node == self.head:
            frontier = [node for _, node in top_node.children.items()]
        else:
            frontier = [top_node]

        while frontier != []:
            cur_node = frontier.pop()
            frontier += [node for _, node in cur_node.children.items()]
            if list(cur_node.children.items()) == [] or cur_node.is_key:
                result.add(cur_node.label)

        # Ordering results by word length
        result = [(entry, len(entry)) for entry in result]
        result = sorted(result, key=lambda k: k[1])
        result = [entry[0] for entry in result]

        # Formatting output result and computing next possible characters
        result_out = self._output(result, prefix_norm.decode("utf8"))
        return result_out

    def word_exists(self, word, ignore_case=True):
        """
        Check if a given word exists in the Trie.
    
        :param word: String to check for correspondences in the Trie
        :type word: str
        :param ignore_case: Boolean to indicate if case should be taken into consideration
        :type ignore_case: bool
        :returns: True, False
        :raises: ValueError, TypeError
        """
        if word is None:
            raise ValueError("'word' cannot be null")
        if not isinstance(word, str):
            raise TypeError("'word' needs to be a string")

        word_norm = word.encode("utf8").lower()

        cur_node = self.head
        for letter in word_norm:
            if letter in cur_node.children:
                cur_node = cur_node.children[letter]
                if cur_node.label == word:
                    return True
                elif ignore_case and cur_node.data == word_norm:
                    return True
            else:
                return False
        return False

    @staticmethod
    def _output(result, prefix):
        """
        Given a list of words and the used prefix, outputs the words
        alphabetically ordered and the next possible characters.
    
        :param result: List of words
        :type word: list
        :param prefix: Prefix used in search
        :type prefix: str
        :returns: Dictionary with the possible words and the next available characters
        """
        result_out = {}
        result_out["matches"] = result
        result_out["next_chars"] = set()

        for entry in result:
            aux = entry.lower().split(prefix)[-1]
            try:
                result_out["next_chars"].add(aux[0])
            except IndexError:
                pass
        result_out["next_chars"] = list(result_out["next_chars"])
        return result_out


if __name__ == "__main__":
    import doctest
    doctest.testmod()
