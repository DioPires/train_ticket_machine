# Train ticket machine

Challenge where one is asked to develop a search algorithm to be used
in a train ticket machine to help users entering the name of stations.
For every character users type, the API computes the possible words
from the characters already typed and the next possible characters
the user can type.

## Implementation

The search algorithm is implemented using a [Trie](https://en.wikipedia.org/wiki/Trie)
together with [BFS](https://en.wikipedia.org/wiki/Breadth-first_search).

## Usage

The API exposed methods to:
* Add a list of words to the trie
* Add a single word to the trie
* Checking the possible words given a prefix
* Check if a given word exists

### Normal usage

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
