user_input = input()
numero_tcs = int(user_input)

test_cases = []
for _ in range(numero_tcs):
    user_input = input()
    tc = user_input.split()
    test_cases.append(tc)


def karatsuba(bin_A, bin_B):
    size_A = len(bin_A)
    size_B = len(bin_B)

    if size_A == 1 or size_B == 1:
        decimal_A = int(bin_A, 2)
        decimal_B = int(bin_B, 2)
        return bin(decimal_A * decimal_B)[2:]

    max_size = max(size_A, size_B)
    if max_size % 2 != 0:
        max_size += 1

    bin_A = bin_A.zfill(max_size)
    bin_B = bin_B.zfill(max_size)

    mitad = max_size // 2

    hi_A = bin_A[:mitad]
    lo_A = bin_A[mitad:]
    hi_B = bin_B[:mitad]
    lo_B = bin_B[mitad:]

    z2_bin = karatsuba(hi_A, hi_B)
    z0_bin = karatsuba(lo_A, lo_B)

    dec_sum_A = int(hi_A, 2) + int(lo_A, 2)
    dec_sum_B = int(hi_B, 2) + int(lo_B, 2)
    
    bin_sum_A = bin(dec_sum_A)[2:]
    bin_sum_B = bin(dec_sum_B)[2:]

    z1_combinado_bin = karatsuba(bin_sum_A, bin_sum_B)

    dec_z2 = int(z2_bin, 2)
    dec_z0 = int(z0_bin, 2)
    dec_z1_comb = int(z1_combinado_bin, 2)
    
    dec_z1 = dec_z1_comb - dec_z2 - dec_z0

    resultado_decimal = (dec_z2 << (2 * (max_size - mitad))) + (dec_z1 << (max_size - mitad)) + dec_z0
    return bin(resultado_decimal)[2:]


for tc in test_cases:
    string_A = tc[0]
    string_B = tc[1]
    
    resultado_binario = karatsuba(string_A, string_B)
    print(resultado_binario)