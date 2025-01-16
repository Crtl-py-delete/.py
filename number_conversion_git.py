# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:05:33 2024

@author: mvdhe
Vives (Belgium)
"""

def float_to_sci_str(number: float, decimal_places: int, unit:str) -> str:
    """convert a number to (P, T, M, G, k | m, µ, n, p, f) notation.
    
    usage: float_to_sci_str(your_number, decimal places, "SI Unit"))"""
    if number < 0:
        sign = "-"
        number = abs(number)
    else: sign = ""
    sci_str_number = ""
    
    unit_sizes = {10**15: "P",
                  10**12: "T",
                  10**9: "M",
                  10**6: "G",
                  10**3: "k",
                  10**0: "",
                  10**-3: "m",
                  10**-6: "µ",
                  10**-9: "n",
                  10**-12: "p",
                  10**-15: "f"}
    
    if number < 1000 and number >= 1 or unit == "%": #no prefix
        sci_str_number = sign + str(round(number,decimal_places)) + unit
        return sci_str_number
    
    elif number >= 1000: #prexix that makes your number larger
        for key in unit_sizes:
            if number >= key:
                sci_str_number = str(round(number/key, decimal_places)) + unit_sizes[key] + unit
                break
        return sci_str_number
    
    elif number == 0: #zero
        return "0" + unit
    
    elif number < 1: #prexix that makes your number smaller
        for key in unit_sizes:
            if number <= key*1000:                  
                sci_str_number = sign + str(round(number/key, decimal_places)) + unit_sizes[key] + unit
            else: break
            
        return sci_str_number
    
if __name__ == "__main__": # test the program here:
    #usage: float_to_sci_str(your_number, decimal places, "SI Unit"))
    test_number = 684*10**15
    for prefix in range(0,34,2):
        
        print(float_to_sci_str(test_number*10**-prefix,3, "F"))
