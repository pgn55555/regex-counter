from regex_task import Regex

def test_1_sample_test():
    r = Regex('ab+c.aba.*.bac.+.+* a 2')
    assert r.is_include()

def test_2_sample_test():
    r = Regex('acb..bab.c.*.ab.ba.+.+*a. a 0')
    assert not r.is_include()


def test_1_regex_validation():
    try:
        Regex('ab+ a 0')
    except ValueError:
        assert False

def test_2_regex_validation():
    try:
        Regex('abb+ a 0')
    except ValueError:
        assert True

def test_3_regex_validation():
    try:
        Regex('ab. a 0')
    except ValueError:
        assert False

def test_4_regex_validation():
    try:
        Regex('a* a 0')
    except ValueError:
        assert False


def test_1_accept_check():
    r = Regex('ab+ a 1')
    assert r.is_include()

def test_2_accept_check():
    r = Regex('abaab.*.aab.*..+*. a 5')
    assert r.is_include()

def test_3_accept_check():
    r = Regex('ab.ba.+*1a+ba.+. a 5')
    assert r.is_include()

def test_4_accept_check():
    r = Regex('aa*.* a 200')
    assert r.is_include()


def test_1_reject_chech():
    r = Regex('a* b 1')
    assert not r.is_include()

def test_2_reject_chech():
    r = Regex('ab.ba.+*1a+ba.+. c 1')
    assert not r.is_include()

def test_3_reject_chech():
    r = Regex('ba*. b 2')
    assert not r.is_include()