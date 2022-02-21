from Functiontest.lib import try_me

def test_func():
    name = 'Alex'
    assert try_me(name) == 'Welcome Home, Alex'
