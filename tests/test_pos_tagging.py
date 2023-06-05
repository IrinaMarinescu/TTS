from unittest import TestCase

from app.pos_tagging import pos_tagging


class Test(TestCase):
    def test_pos_tagging_normal(self):
        tokens = "I am a surgeon"
        result = pos_tagging(tokens)
        self.assertEqual(result, [('I', 'PRON'), ('am', 'VERB'), ('a', 'DET'), ('surgeon', 'NOUN')])

    def test_pos_tagging_empty(self):
        tokens = ""
        result = pos_tagging(tokens)
        self.assertEqual(result, [])

