import pytest
from data_read.metro_overview_data_reader import read_data


def test_read_data():

    testing = read_data()
    print(testing)
    assert (type(testing),dict)