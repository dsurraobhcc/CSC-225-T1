# rules
single_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
double_vals = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

# "MCMXC" -> 1990 ("M" -> 1000 + "CM" -> 900 + "XC" -> 90)

def next_val(roman):  
    total = 0
    if roman[:2] in double_vals.keys():
        total = double_vals[roman[:2]] + next_val(roman[2:])
    elif len(roman) > 0:
        total = single_vals[roman[:1]] + next_val(roman[1:])
    return total

roman = ''
while True:
    roman = input('Enter a roman numeral: ')
    if roman == 'q':
        break
    print(next_val(roman))