# Train ticket machine

Challenge where one is asked to develop a search algorithm to be used
in a train ticket machine to help users entering the name of stations.
For every character users type, the API computes the possible words
from the characters already typed and the next possible characters
the user can type.

## Implementation

The search algorithm is implemented using a [Trie](https://en.wikipedia.org/wiki/Trie)
together with [BFS](https://en.wikipedia.org/wiki/Breadth-first_search).

The autocomplete API is implemented using a [Trie](https://en.wikipedia.org/wiki/Trie>) as a data structure to save all the possible words. The Trie is computed from these words in the loading phase and this ony happens once.

During runtime, when users are typing and the API is outputting the possible words and the next available characters, the search in the Trie is done using the [BFS](https://en.wikipedia.org/wiki/Breadth-first_search>) algorithm.

## Usage

The API exposed methods to:
* Add a list of words to the trie
* Add a single word to the trie
* Checking the possible words given a prefix
* Check if a given word exists

### Normal usage

The normal usage of the API should be done from the UI/UX interface by calling the Trie.*from_prefix* method for every character chosen by the user. Nonetheless, here is an example of computing the Trie from a list of words and getting the possible words and next characters from prefixes:

```
>>> import trie
>>> words = ["Dartford", "Dartmouth", "Tower Hill",
...          "Derby", "Liverpool", "Liverpool Line Street",
...          "Paddington", "Euston", "London Bridge", "Victoria"]
>>> t = trie.Trie()
>>> t.add_words(words)
>>> t.from_prefix("dart")
{'matches': ['Dartford', 'Dartmouth'], 'next_chars': ['m', 'f']}
>>> t.from_prefix("liverpool")
{'matches': ['Liverpool', 'Liverpool Line Street'], 'next_chars': [' ']}
```

For a more detailed documentation of the API, please refer to the contents of the **doc** directory. There you will find an HTML page and a PDF generated using [Sphinx](http://www.sphinx-doc.org/en/stable/), the Python Documentation Generator.