dndbeyond_websearch
===================

Install
-------

`pip install dndbeyond-websearch`

Example
-------

```python
>>> from dndbeyond_websearch import Searcher
>>> Searcher().search('Otyugh')[0]
SearchResult(title=u'Otyugh', breadcrumbs=u'Compendium - Compendium->Rules->Monster Manual', snippets=[u'Otyugh\notyugh\nOtyugh\r\nLarge aberration, neutral\r\nArmor Class 14 (natural armor)\r\nHit Points 114 (12d10 + 48)\r\nSpeed 30 ft.\r\n\r\n\r\nSTR\r\n16(+3)\r\n\r\n\r\nDEX\r\n11(+0)\r\n\r\n\r\nCON\r\n19(+4)\r\n\r\n\r\nINT\r\n6(\u22122', u')\r\n\r\n\r\nWIS\r\n13(+1)\r\n\r\n\r\nCHA\r\n6(\u22122)\r\n\r\n\r\nSaving Throws Con +7\r\nSenses darkvision 120 ft., passive Perception 11\r\nLanguages Otyugh\r\nChallenge 5 (1,800 XP)\r\nLimited Telepathy. The otyugh can'])
```
