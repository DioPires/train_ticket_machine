.. Train Ticket Machine documentation master file, created by
   sphinx-quickstart on Sun Dec 10 01:50:57 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Train Ticket Machine's documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
============

Challenge where one is asked to develop a search algorithm to be used in a train ticket machine to help users entering the name of stations. For every character users type, the API computes the possible words from the characters already typed and the next possible characters the user can type.

Implementation
==============

The autocomplete API is implemented using a `Trie <https://en.wikipedia.org/wiki/Trie>`_ as a data structure to save all the possible words. The Trie is computed from these words in the loading phase and this ony happens once.

During runtime, when users are typing and the API is outputting the possible words and the next available characters, the search in the Trie is done using the `BFS <https://en.wikipedia.org/wiki/Breadth-first_search>`_ algorithm.

Normal API usage
================

The normal usage of the API should be done from the UI/UX interface by calling the Trie.\ *from_prefix* method for every character chosen by the user. Nonetheless, here is an example of computing the Trie from a list of words and getting the possible words and next characters from prefixes:

::
   
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

API documentation
=================


.. automodule:: trie
	:members:
