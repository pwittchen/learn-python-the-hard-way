from nose.tools import *
from exercise48.parser import *


def test_parse_sentence():
  sentence = parse_sentence([('verb', 'run'), ('direction', 'north')])
  assert_equal(sentence.subject, 'player')
  assert_equal(sentence.verb, 'run')
  assert_equal(sentence.object, 'north')
