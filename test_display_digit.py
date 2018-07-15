# -*- coding: utf-8 -*-
from model.numbers import NumberInt
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_display_digit(app):
    app.load_home_page()
    app.add_one_digit(NumberInt())
    app.reset_calc_data()

