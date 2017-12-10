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

Challenge where one is asked to develop a search algorithm to be used in a train ticket machine to help users entering the name of stations.

Implementation
==============

The search algorithm is implemented using a `Trie <https://en.wikipedia.org/wiki/Trie>`_ together with `BFS <https://en.wikipedia.org/wiki/Breadth-first_search>`_.

Normal API usage
================

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
