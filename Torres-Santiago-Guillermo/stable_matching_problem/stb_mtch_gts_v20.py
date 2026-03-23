def st_mch(pref_1,pref_2):
    per_lib=list(pref_1.keys())
    propuesta={p1:0 for p1 in pref_1}
    new_mtch={}
    p2_rank={}
    for p2,prefs in pref_2.items():
        p2_rank[p2]={p1:rank for rank,p1 in enumerate(prefs)}
    while per_lib:
        p1=per_lib[0]
        p2=pref_1[p1][propuesta[p1]]
        propuesta[p1]+=1
        if p2 not in new_mtch:        
            new_mtch[p2]=p1
            per_lib.pop(0)
        else: 
            pareja_actual=new_mtch[p2]  
            if p2_rank[p2][p1]<p2_rank[p2][pareja_actual]:
                new_mtch[p2]=p1
                per_lib.pop(0)
                per_lib.append(pareja_actual)
    matches={p1:p2 for p2,p1 in new_mtch.items()}
    return matches
def list_pers(parejas):
    pref_list={}
    for jk in range(parejas):
        persona=input()
        nombre_pref=persona.split()
        nombre=nombre_pref[0]
        preferencias=nombre_pref[1:]
        pref_list.update({nombre:preferencias})
    return pref_list
pref_hombres={}
pref_mujeres={}
parejas={}
cadena1=input()
cadena2=cadena1.split()
np=int(cadena2[0])
proponer=cadena2[1].upper()
pref_hombres=list_pers(np)
pref_mujeres=list_pers(np)
if proponer=="M":
    parejas=st_mch(pref_hombres,pref_mujeres)
    for h in pref_hombres:print(f"{h} {parejas[h]}")
else:
    parejas=st_mch(pref_mujeres,pref_hombres)
    for m in pref_mujeres:print(f"{m} {parejas[m]}")