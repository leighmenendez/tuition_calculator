from argparse import ArgumentParser

import sys

def calculate_tuition(credits = 12, resident = True, dt = False):
    
    """Calculates tuition and mandatory fees for one semester at UMD.
    Takes into consideration the number of credits the student is taking, whether they are a resident of Maryland, 
    and whether they pay differential tuition.
    
    Args:
        credits (integer): the number of credits the student is taking (default: 12)
        resident(boolean): whether the student is consifered a Maryland state resident for tuition purposes (default: True).
        dt(boolean): whether or not the student pays differential tuition (default: False).
        
    Raises: 
        ValueError: credits must be non-negative.
    Returns:
        float: the student's combined tuition and mandatory fees
    """
    
    tuition = 0
    
    if credits >= 12 and resident == True and dt == False:
        tuition = 4412 + 977.50
    elif credits >= 12 and resident == True and dt == True:
        tuition = 4412 + 977.50 + 1428
    elif credits >= 12 and resident == False and dt == False:
        tuition = 17468 + 977.50 
    elif credits >= 12 and resident == False and dt == True:
        tuition = 17468 + 977.50 + 1428
    elif 12 > credits >= 9 and resident == True and dt == False:
        tuition = (credits * 367) + 977.50
    elif 12 > credits >= 9 and resident == True and dt == True: 
        tuition = (credits * 367) + (credits * 118) + 977.50 
    elif 12 > credits >= 9 and resident == False and dt == False:
        tuition = (credits * 1456) + 977.50
    elif 12 > credits >= 9 and resident == False and dt == True:
        tuition = (credits * 1456) + (credits * 118) + 977.50
    elif 8 >= credits >= 1 and resident == True and dt == False:
        tuition = (credits * 367) + 455
    elif 8 >= credits >= 1 and resident == True and dt == True:
        tuition = (credits * 367) + (credits * 118) + 455
    elif 8 >= credits >= 1 and resident == False and dt == False:
        tuition = (credits * 1456) + 455
    elif 8 >= credits >= 1 and resident == False and dt == True:
        tuition = (credits * 1456) + (credits * 118) + 455
    elif credits == 0:
        tuition = 0
        return tuition
    else:
        raise ValueError("credits must be non-negative")
    return tuition
      
    
def parse_args(arglist):
    
    """Parses command-line arguments.
    The following optional command-line arguments are defined:
     ​-c / --credits: the number of credits the student is taking
       ​(type: int, default: 12)
   ​-nr / --nonresident: indicates the student is not a Maryland
       ​resident (action: 'store_true')
   ​-dt / --differentialtuition: indicates the student pays differential
       ​tuition (action: 'store_true')

   ​Args:
       ​arglist (list of str): a list of command-line arguments.

   ​Returns:
       ​namespace: a namespace with variables credits, nonresident, and
       ​differentialtuition.
    """
    
    parser = ArgumentParser()
    
    parser.add_argument('-c', '--credits', type = int, default = 12)
    parser.add_argument('-nr', '--nonresident', action = 'store_false',
                        help = "use nonresident or resident(default = true)")
    parser.add_argument('-dt', '--differentialtuition', action = 'store_true',
                        help = "use differentialtuition or not(default = false)")
    return parser.parse_args(arglist)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:]) 
    tuition_price = calculate_tuition(args.credits, args.nonresident, args.differentialtuition)
    print(tuition_price)
    
    
        
        
