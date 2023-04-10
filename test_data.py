import pytest
from main import get_price_change


@pytest.fixture
def data():
    return 'data_test.txt'


def test_get_data_changes(data):
    expected_results = 'Ціна товару Фотоапарат Nikon змінилась на 1000.0 за останній місяць'
    assert get_price_change('Фотоапарат Nikon', data) == expected_results


pytest.main(["-v", "--html=report.html"])
