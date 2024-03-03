def is_prime(num):
    if num <= 1 or (num % 2 == 0 and num!= 2) :
        return False
    for x in range(3,num,2) :
        if num % x == 0 :
            return False
    return True