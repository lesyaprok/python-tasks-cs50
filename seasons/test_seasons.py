from seasons import Seasons
import pytest

def test_number_to_words():
    seasons = Seasons("2021-07-07")
    assert seasons.number_to_words() == "Five hundred twenty-five thousand, six hundred minutes"
    seasons = Seasons("2020-07-07")
    assert seasons.number_to_words() == "One million, fifty-one thousand, two hundred minutes"

def test_seasons():
    with pytest.raises(SystemExit):
        seasons = Seasons("2020-15-99")
