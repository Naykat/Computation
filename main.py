def is_prime(number: int, cycle_origin: int = 2) -> bool:
    dividers = 0
    for divider in range(cycle_origin,int(number**0.5)+1):
        if number%divider==0:
            dividers+=1
        if dividers>0:
            return False
    return True

def get_prime_numbers(limit: int) -> list:
    numbers = []
    result = []
    for position in range(limit+1):
        numbers.append(1)
    numbers[0] = 0
    numbers[1] = 0
    for position in range(2,limit+1):
        if numbers[position] == 1:
            result.append(position)
            for removing_position in range(position**2, limit+1,position):
                numbers[removing_position] = 0
    return result

def get_dividers(number: int) -> list:
    dividers = []
    for divider in range(1,int(number**0.5)+1):
        if number%divider==0:
            dividers.append(divider)
            dividers.append(number//divider)
    return sorted(dividers)

def get_prime_dividers(number: int) -> list:
    result = [2]
    divider = 1
    while number > 1:
        divider+=1
        if number%divider == 0 and is_prime(divider, max(result)):
            result.append(divider)
            while number%divider==0:
                number= number//divider
    if number%2!=0:
        result.remove(2)
    return result

def radical(number: int or float, degree: int) -> float:
    return number**(1/degree)
