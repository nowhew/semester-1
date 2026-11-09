# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(15) == "COLD"
    assert comfort_level(10) == "COLD"

def test_hot():
    assert comfort_level(26) == "HOT"
    assert comfort_level(30) == "HOT"
    
def test_ok():
    test_cold()
    test_hot()