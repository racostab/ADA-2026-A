def odd_digits(x):
    digits = list(str(x))
    digits_int = list(map(int,digits))
    for digit in digits_int:
        if digit%2 == 0:
            return False

    return True

rev_num_counter = 0
i=11

while i < 10**8:
    if len(str(i))%4 == 1:
        i_str = "1" + "0"*(len(str(i)))
        i = int(i_str)
        
    if i%10 == 0:
        i+=1
        continue

    rev_i = int(str(i)[::-1])
    rev_num = i + rev_i
    i+=1   

    if odd_digits(rev_num):
        rev_num_counter +=1

print(rev_num_counter)
