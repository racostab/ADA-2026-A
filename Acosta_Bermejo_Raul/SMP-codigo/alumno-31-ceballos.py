
user_input = input()
user_input_values = user_input.split(' ')

N = int(user_input_values[0])
matching_type = user_input_values[1]
men_pref = {}
women_pref = {}

for i in range(N):
    user_input = input()
    user_input_values = user_input.split(' ')
    men_pref[user_input_values[0]] = user_input_values[1:]

for i in range(N):
    user_input = input()
    user_input_values = user_input.split(' ')
    women_pref[user_input_values[0]] = user_input_values[1:]

S = {}
M = list(men_pref.keys())
W = list(women_pref.keys())


if matching_type == 'm':
    while M:
        current_M = M.pop(0)
        M_pref = men_pref[current_M]
        current_W = M_pref.pop(0)
        W_pref = women_pref[current_W]
        
        if current_W in S.keys():
            W_pair = S[current_W]
            if W_pref.index(W_pair) > W_pref.index(current_M):
                S[current_W] = current_M
                M.append(W_pair)
            else:
                men_pref[current_M] = M_pref
                M.append(current_M)
                
        else:
            S[current_W] = current_M
    
    S_inv = dict(map(reversed, S.items()))

    for p in list(men_pref.keys()):
        print(f"{p} {S_inv[p]}")

else:
    while W:
        current_W = W.pop(0)
        W_pref = women_pref[current_W]
        current_M = W_pref.pop(0)
        M_pref = men_pref[current_M]

        if current_M in S.keys():
            M_pair = S[current_M]
            if M_pref.index(M_pair) > M_pref.index(current_W):
                S[current_M] = current_W
                W.append(M_pair)
            else:
                women_pref[current_M] = W_pref
                W.append(current_W)
            
        else:
            S[current_M] = current_W
        
    S_inv = dict(map(reversed, S.items()))

    for p in list(women_pref.keys()):
        print(f"{p} {S_inv[p]}")


