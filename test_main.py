"""Tests for technical interview functions."""

from main import (
    make_uppercase,
    split_into_names,
    reformat_name,
    sort_names_alphabetically,
    join_elements_in_list
)


def test_make_uppercase_simple():

    assert make_uppercase('aaa') == 'AAA'


def test_make_uppercase_extended():

    assert make_uppercase(
        'Fred:Corwill;Wilfred:Corwill') == 'FRED:CORWILL;WILFRED:CORWILL'


def test_split_into_names():

    assert split_into_names('FRED:CORWILL;WILFRED:CORWILL') == [
        'FRED:CORWILL', 'WILFRED:CORWILL']


def test_reformat_name():

    assert reformat_name('FRED:CORWILL') == ('(CORWILL, FRED)')


def test_sort_names_alphabetically():

    test_input = ['(TORNBULL, BARNEY)', '(CORWILL, WILFRED)',
                  '(CORWILL, RAPHAEL)']

    assert sort_names_alphabetically(test_input) == [
        '(CORWILL, RAPHAEL)', '(CORWILL, WILFRED)', '(TORNBULL, BARNEY)']


def test_join_elements_in_list():

    test_input = ['(CORWILL, RAPHAEL)', '(CORWILL, WILFRED)',
                  '(TORNBULL, BARNEY)']

    assert join_elements_in_list(
        test_input) == '(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)'
