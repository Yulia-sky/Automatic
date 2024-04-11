import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('string, result', [('Юля', ' Ю л я'), (' ', ''), ('5', '-5')])
def test_capitalize_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.xfail
def test_capitilize_positive():
    string_utils = StringUtils()
    res = string_utils.capitilize('5')
    assert res == '5'

@pytest.mark.xfail
def test_capitilize_negative():
    string_utils = StringUtils()
    res = string_utils.capitilize('5')
    assert res == '5'

@pytest.mark.xfail
def test_capitilize_negative1():
    string_utils = StringUtils()
    res = string_utils.capitilize(None)
    assert res == None

@pytest.mark.xfail
def test_capitilize_negative1():
    string_utils = StringUtils()
    res = string_utils.capitilize('-5')
    assert res == '-5'      

@pytest.mark.parametrize('string, result', [('Юля', ' Ю л я'), (' ', ''), ('5', '-5')])
def test_trim_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result  

@pytest.mark.xfail
def test_trim_positive():
    string_utils = StringUtils()
    res = string_utils.trim('5')
    assert res == '5'

@pytest.mark.xfail
def test_trim_negative():
    string_utils = StringUtils()
    res = string_utils.trim('5')
    assert res == '5'

@pytest.mark.xfail
def test_trim_negative1():
    string_utils = StringUtils()
    res = string_utils.trim(None)
    assert res == None

@pytest.mark.xfail
def test_trim_negative1():
    string_utils = StringUtils()
    res = string_utils.trim('-5')
    assert res == '-5'

@pytest.mark.parametrize('string, result', [('Юля', ' Ю л я'), (' ', ''), ('5', '-5')])
def test_to_list_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string)
    assert res == result  

@pytest.mark.xfail
def test_to_list_positive():
    string_utils = StringUtils()
    res = string_utils.to_list('5')
    assert res == '5'

@pytest.mark.xfail
def test_to_list_negative():
    string_utils = StringUtils()
    res = string_utils.to_list('5')
    assert res == '5'

@pytest.mark.xfail
def test_to_list_negative1():
    string_utils = StringUtils()
    res = string_utils.to_list(None)
    assert res == None

@pytest.mark.xfail
def test_to_list_negative1():
    string_utils = StringUtils()
    res = string_utils.to_list('-5')
    assert res == '-5'

@pytest.mark.parametrize('string, result', [('Юля', ' Ю л я'), (' ', ''), ('5', '-5')])
def test_contains_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.contains(string)
    assert res == result  

@pytest.mark.xfail
def test_contains_positive():
    string_utils = StringUtils()
    res = string_utils.contains('5')
    assert res == '5'

@pytest.mark.xfail
def test_contains_negative():
    string_utils = StringUtils()
    res = string_utils.contains('5')
    assert res == '5'

@pytest.mark.xfail
def test_contains_negative1():
    string_utils = StringUtils()
    res = string_utils.contains(None)
    assert res == None

@pytest.mark.xfail
def test_contains_negative1():
    string_utils = StringUtils()
    res = string_utils.contains('-5')
    assert res == '-5'       