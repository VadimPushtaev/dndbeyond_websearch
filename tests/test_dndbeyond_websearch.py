from collections import namedtuple
from unittest import TestCase

import os
from unittest.mock import patch

from dndbeyond_websearch import Searcher


class SearcherTestCase(TestCase):
    def setUp(self):
        with open(os.path.dirname(__file__) + '/cast_a_spell.html', 'r') as f:
            self._html = f.read()

        self._searcher = Searcher()

    @patch('dndbeyond_websearch.requests')
    def test_extract_result(self, mocked_requests):
        mocked_requests.get.return_value = namedtuple('Result', 'content')(content=self._html)
        results = self._searcher.search('cast a spell')
        mocked_requests.get.assert_called_with('https://www.dndbeyond.com/search', params=dict(q='cast a spell'))

        self.assertEqual(len(results), 35)

        first = results[0]
        self.assertEqual(first.title, 'Cast a Spell')
        self.assertEqual(first.url, 'https://www.dndbeyond.com/compendium/rules/phb/combat#CastaSpell')
        self.assertEqual(first.breadcrumbs.upper(), "COMPENDIUM - COMPENDIUM->RULES->PLAYER'S HANDBOOK")
        self.assertEqual(len([s for s in first.snippets if s is not None]), 2)

        forum = results[28]
        self.assertEqual(forum.title, 'Creating a spell')
        self.assertEqual(forum.breadcrumbs.upper(), 'FORUMS - RE: CREATING A SPELL')
        self.assertEqual(forum.snippets, ['Tweak as you like, I was just messin around'])
