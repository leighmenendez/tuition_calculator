#test script for tuition calculator 

from tuition_calculator import calculate_tuition 

def test_tuition_calculator():
    assert calculate_tuition(credits = 0) == 0
    assert calculate_tuition(credits = 1, resident = True, dt = False) == 822
    assert calculate_tuition(credits = 1, resident = True, dt = True) == 940
    assert calculate_tuition(credits = 1, resident = False, dt = False) == 1911
    assert calculate_tuition(credits = 1, resident = False, dt = True) == 2029
    assert calculate_tuition(credits = 8, resident = True, dt = False) == 3391
    assert calculate_tuition(credits = 8, resident = True, dt = True) == 4335
    assert calculate_tuition(credits = 8, resident = False, dt = False) == 12103
    assert calculate_tuition(credits = 8, resident = False, dt = True) == 13047
    assert calculate_tuition(credits = 9, resident = True, dt = False) == 4280.5   
    assert calculate_tuition(credits = 9, resident = True, dt = True) == 5342.5
    assert calculate_tuition(credits = 9, resident = False, dt = False) == 14081.5
    assert calculate_tuition(credits = 9, resident = False, dt = True) == 15143.5
    assert calculate_tuition(credits = 11, resident = True, dt = False) == 5014.5
    assert calculate_tuition(credits = 11, resident = True, dt = True) == 6312.5
    assert calculate_tuition(credits = 11, resident = False, dt = False) == 16993.5
    assert calculate_tuition(credits = 11, resident = False, dt = True) == 18291.5
    assert calculate_tuition(credits = 12, resident = True, dt = False) == 5389.5
    assert calculate_tuition(credits = 12, resident = True, dt = True) == 6817.5
    assert calculate_tuition(credits = 12, resident = False, dt = False) == 18445.5
    assert calculate_tuition(credits = 12, resident = False, dt = True) == 19873.5
    assert calculate_tuition(credits = 15, resident = True, dt = False) == 5389.5
    assert calculate_tuition(credits = 15, resident = True, dt = True) == 6817.5
    assert calculate_tuition(credits = 15, resident = False, dt = False) == 18445.5
    assert calculate_tuition(credits = 15, resident = False, dt = True) == 19873.5
    
    
    
    
    
    
    







