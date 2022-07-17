import pytest


@pytest.fixture(scope='module')
def call_me_once_use_when_needed():
    print('\ncall me once use when needed')


@pytest.fixture()
def call_me_every_time():
    print('call me every time')


@pytest.fixture(autouse=True)
def call_me_everywhere():
    print('You\'ll call me even if you don\'t wanna to')


def test_one(call_me_once_use_when_needed, call_me_every_time):
    print('test one')
    print('after chenge by Students6')


def test_two(call_me_once_use_when_needed, call_me_every_time):
    print('test two')
    print('after chenge by Students6')

def test_three_by_student6(call_me_once_use_when_needed, call_me_every_time):
    print('test three by Student6')
