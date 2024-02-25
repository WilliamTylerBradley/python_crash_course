import pytest
from employee import Employee

@pytest.fixture
def new_employee():
    """Employee fixture"""
    new_employee = Employee('Test', 'Tester', 50000)
    return new_employee

def test_give_default_raise(new_employee):
    """test default raise"""
    new_employee.give_raise()
    assert new_employee.salary == 55000

def test_give_custom_raise(new_employee):
    """test custom raise"""
    new_employee.give_raise(2500)
    assert new_employee.salary == 52500