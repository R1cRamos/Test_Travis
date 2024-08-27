def add(a, b): # Defines a function to add two numbers
    return a + b

def test_add(): # Defines a function to test the 'add' function
    assert add(2, 3) == 5 # Checks if 2 + 3 equals 5
    assert add(-1, 1) == 0 # Checks if -1 + 1 equals 0

if __name__ == "__main__": # Runs the test function if the script is executed directly
    test_add()
    print("All tests passed!")
