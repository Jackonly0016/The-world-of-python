import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summer', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summer': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected

@pytest.mark.run_these_please
def test_replace():
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brain', True, 10)
    t = Task('buy milk', 'brain')
    assert t_after == t_expected
