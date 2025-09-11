import pytest
from employee import Employee

@pytest.fixture
def sample_employee():
    """Fixture to provide a common Employee instance for tests."""
    return Employee("Steven", "Armenta", 60000)

def test_give_default_raise(sample_employee):
    """Test that the default raise adds 5000 to the salary."""
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 65000

def test_give_custom_raise(sample_employee):
    """Test that a custom raise adds the correct amount to the salary."""
    sample_employee.give_raise(10000)
    assert sample_employee.annual_salary == 70000
