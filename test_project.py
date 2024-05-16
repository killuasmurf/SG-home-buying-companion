from project import check_file, see_neighbourhoods, ending
import pytest

def test_check_file():
  with pytest.raises(SystemExit):
      check_file()

def test_see_neighbourhoods():
    assert see_neighbourhoods("mock.csv") == None

def test_ending():
    assert ending() == "\nThanks for using, bye!"

