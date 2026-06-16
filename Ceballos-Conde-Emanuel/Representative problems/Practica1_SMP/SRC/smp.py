
def smp(men_pref,women_pref):
  S = {}
  M = list(men_pref.keys())
  W = list(women_pref.keys())

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

  return S