from enum import IntEnum
from collections import deque


def build_data_test():
    """
    params = ['5', 'm']  #FWho propose M -> Men  W -> Women
    universe = [
        ['Victor', 'Bertha', 'Amy', 'Diane', 'Erika', 'Clare'],
        ['Wyatt', 'Diane', 'Bertha', 'Amy', 'Clare', 'Erika'],
        ['Xavier', 'Bertha', 'Erika', 'Clare', 'Diane', 'Amy'],
        ['Yancey', 'Amy', 'Diane', 'Clare', 'Bertha', 'Erika'],
        ['Zeus', 'Bertha', 'Diane', 'Amy', 'Erika', 'Clare'],
        ['Amy', 'Zeus', 'Victor', 'Wyatt', 'Yancey', 'Xavier'],
        ['Bertha', 'Xavier', 'Wyatt', 'Yancey', 'Victor', 'Zeus'],
        ['Clare', 'Wyatt', 'Xavier', 'Yancey', 'Zeus', 'Victor'],
        ['Diane', 'Victor', 'Zeus', 'Yancey', 'Xavier', 'Wyatt'],
        ['Erika', 'Yancey', 'Wyatt', 'Zeus', 'Xavier', 'Victor']
    ]
    """
    """
    params = ['10', 'm']  #FWho propose M -> Men  W -> Women
    universe = [
        ['abe', 'abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
        ['bob','cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
        ['col', 'hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
        ['dan', 'ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
        ['ed','jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
        ['fred', 'bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
        ['gav', 'gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
        ['hal', 'abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
        ['ian', 'hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
        ['jon', 'abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope'],
        ['abi','bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
        ['bea','bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
        ['cath','fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
        ['dee','fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
        ['eve','jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
        ['fay','bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
        ['gay','jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
        ['hope','gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
        ['ivy','ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
        ['jan','ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']
    ]
    """
    """
    params = ['5', 'w']  #F Who propose M -> Men  W -> Women
    universe = [
        ['Adam', 'Beth', 'Amy', 'Diane', 'Ellen', 'Cara'],
        ['Bill','Diane', 'Beth', 'Amy', 'Cara', 'Ellen'],
        ['Carl','Beth', 'Ellen', 'Cara', 'Diane', 'Amy'],
        ['Dan','Amy', 'Diane', 'Cara', 'Beth', 'Ellen'],
        ['Eric','Beth', 'Diane', 'Amy', 'Ellen', 'Cara'],
        ['Amy','Eric', 'Adam', 'Bill', 'Dan', 'Carl'],
        ['Beth','Carl', 'Bill', 'Dan', 'Adam', 'Eric'],
        ['Cara','Bill', 'Carl', 'Dan', 'Eric', 'Adam'],
        ['Diane','Adam', 'Eric', 'Dan', 'Carl', 'Bill'],
        ['Ellen','Dan', 'Bill', 'Eric', 'Carl', 'Adam'],
    ]
    """
    
    """
    params = ['2', 'm']  #FWho propose M -> Men  W -> Women    
    universe = [
    ['A', 'X', 'Y'],
    ['B', 'X', 'Y'],
    ['X', 'B', 'A'],
    ['Y', 'A', 'B']
    ]
    """
    """
    params = ['3', 'm']  #FWho propose M -> Men  W -> Women    
    universe = [
    ['A', 'X', 'Y', 'Z'],
    ['B', 'Y', 'Z', 'X'],
    ['C', 'Z', 'X', 'Y'],
    ['X', 'B', 'C', 'A'],
    ['Y', 'C', 'A', 'B'],
    ['Z', 'A', 'B', 'C'],
    ]
    """
    """
    params = ['3', 'm']  # 3 parejas, los hombres (m) proponen
    universe = [
        ['A', 'X', 'Y', 'Z'],  # Preferencias de A
        ['B', 'X', 'Z', 'Y'],  # Preferencias de B
        ['C', 'X', 'Y', 'Z'],  # Preferencias de C
        ['X', 'C', 'B', 'A'],  # Preferencias de X (Prefiere a C sobre todos)
        ['Y', 'A', 'B', 'C'],  # Preferencias de Y
        ['Z', 'A', 'B', 'C']   # Preferencias de Z
    ]
    """
    """
    params = ['3', 'w']  # Ahora las mujeres (w) proponen
    universe = [
        ['A', 'X', 'Y', 'Z'],
        ['B', 'X', 'Z', 'Y'],
        ['C', 'X', 'Y', 'Z'],
        ['X', 'C', 'B', 'A'],
        ['Y', 'A', 'B', 'C'],
        ['Z', 'A', 'B', 'C']
    ]
    """
    """
    params = ['3', 'w']  #FWho propose M -> Men  W -> Women
    universe = [
        ['Xavier', 'Amy', 'Bertha', 'Clare'],
        ['Yancey', 'Bertha', 'Amy', 'Clare'],
        ['Zeus', 'Amy', 'Bertha', 'Clare'],
        ['Amy', 'Yancey', 'Xavier', 'Zeus'],
        ['Bertha', 'Xavier', 'Yancey', 'Zeus'],
        ['Clare', 'Xavier', 'Yancey', 'Zeus']
    ]
    """
    #"""
    params = ['5', 'M']  #F Who propose M -> Men  W -> Women
    universe = [
        ['Adam', 'Beth', 'Amy', 'Diane', 'Ellen', 'Cara'],
        ['Bill','Diane', 'Beth', 'Amy', 'Cara', 'Ellen'],
        ['Carl','Beth', 'Ellen', 'Cara', 'Diane', 'Amy'],
        ['Dan','Amy', 'Diane', 'Cara', 'Beth', 'Ellen'],
        ['Eric','Beth', 'Diane', 'Amy', 'Ellen', 'Cara'],
        ['Amy','Eric', 'Adam', 'Bill', 'Dan', 'Carl'],
        ['Beth','Carl', 'Bill', 'Dan', 'Adam', 'Eric'],
        ['Cara','Bill', 'Carl', 'Dan', 'Eric', 'Adam'],
        ['Diane','Adam', 'Eric', 'Dan', 'Carl', 'Bill'],
        ['Ellen','Dan', 'Bill', 'Eric', 'Carl', 'Adam'],
    ]
    #"""
    """
    params = ['2', 'W']  #FWho propose M -> Men  W -> Women
    universe = [   
        ['lalo', 'alma', 'erika'], 
        ['mario', 'alma', 'erika'], 
        ['alma', 'lalo', 'mario'], 
        ['erika', 'mario', 'lalo']
    ]
    """

    return params, universe


ENABLE_OUTPUT = False
_DB_SUITORS=[]
_DB_PROSPECTS=[]

_ID = "id"
_NAME="name"
_PROSPECTS = "prospects"
_ESTATUS = "estatus"
_MATCHED_ID = "matched_id"
_MATCHED_NAME = "matched_name"

class Estatus(IntEnum):
    UNMATCHED = 1
    MATCHED = 2
    REJECT = 3

def print_message(message, show=None):
    global ENABLE_OUTPUT
    output_enabled = show if show is not None else ENABLE_OUTPUT
    if output_enabled:
        print(message)
"""
Example of params:    
    data = [
            ['alma', 'lalo', 'mario'], 
            ['erika', 'mario', 'lalo']
    ] 
    preferences_keys = ['lalo', 'mario']
"""
def transform_data(data, preferences_keys):
    data_base = []
    #First element of every list, because I have a list of lists (data)
    keys = [list[0] for list in data if list]
    i = 1
    for key in keys:
        id = i
        name = key
        matching_preferences = data[i-1][1:]
        prospects = {}
        for j in range(len(matching_preferences)):
            pid = preferences_keys.index(matching_preferences[j]) + 1
            prospects[pid] = (Estatus.UNMATCHED, j)#estatus and order
        data_base.append({
                            _ID: id,
                            _NAME: name, 
                            _PROSPECTS: prospects,
                            _ESTATUS: Estatus.UNMATCHED,
                            _MATCHED_ID: None,
                            _MATCHED_NAME: None
                        })
        i=i+1
    return data_base

def initialize_db(params, universe):
    size = int(params[0])
    whos_first = params[1].upper().strip()
    mid = (len(universe)) // 2
    suitors = prospects = []
    if whos_first == "M":
        suitors = universe[:mid] 
        prospects = universe[mid:]
    else: 
        suitors = universe[mid:] 
        prospects = universe[:mid]
    #First element of every list
    suitors_keys  = [list[0] for list in suitors if list]
    prospect_keys = [list[0] for list in prospects if list]
    print_message(f"============> Initializing DB <============") 
    print_message(f"============> (N) = {size}, Who's first=[{whos_first}]") 
    #print_message(f"Suitors ====> {suitors} keys => {suitors_keys}")
    #print_message(f"Prospects ==> {prospects} keys => {prospect_keys}")
    global _DB_SUITORS
    global _DB_PROSPECTS
    _DB_SUITORS = transform_data(suitors, prospect_keys)
    _DB_PROSPECTS = transform_data(prospects, suitors_keys)
    print_message(f"\nData Normalization result:")
    print_message(f"\n\tSuitors:")
    for item in _DB_SUITORS:
        print_message(f"\t\t==>{item}")
    print_message(f"\n\tProspects:")
    for item in _DB_PROSPECTS:
        print_message(f"\t\t==>{item}")

def get_suitors_queue():
    global _DB_SUITORS
    suitor_ids = deque(item[_ID] for item in _DB_SUITORS)
    return suitor_ids

def get_suitor_by_id(id):
    """
    suitor = None
    global _DB_SUITORS
    find = lambda lst, condition: next((e for e in lst if condition(e)), None)
    condition = lambda suitor: (suitor[_ID] == id)
    suitor = find(_DB_SUITORS, condition)
    Cambiamos de O(n) a O(1)
    """
    global _DB_SUITORS
    suitor = _DB_SUITORS[id - 1]
    return suitor

def get_prospect_by_id(id):
    """
    prospect = None
    global _DB_PROSPECTS
    find = lambda lst, condition: next((e for e in lst if condition(e)), None)
    condition = lambda prospect: (prospect[_ID] == id)
    prospect = find(_DB_PROSPECTS, condition)
    return prospect
    """
    global _DB_PROSPECTS
    prospect = _DB_PROSPECTS[id - 1]
    return prospect

def is_matched(suitor_data):
    status = suitor_data[_ESTATUS]
    if status == Estatus.UNMATCHED:
        return False
    else:
        return True

def is_new_suitor_better_than_current(prospect_preferences, new_suitor_id, current_suitor_id):
    new_one = prospect_preferences[new_suitor_id][1]
    current = prospect_preferences[current_suitor_id][1]
    if new_one < current:
        return True
    else:
        return False

def update_suitors(suitor, prospect, rejected_flag, prospect_data_in_suitor_prefs):
    """
    suitor      Comes directly from the DB
    prospect    Comes from suitor id's
    prospect_data Suitor preferences related
    """
    global _DB_SUITORS
    global _DB_PROSPECTS
    index = suitor[_ID] - 1
    
    if suitor and prospect and not rejected_flag:
        _DB_SUITORS[index][_ESTATUS] = Estatus.MATCHED
        #Update the suitor’s preferences list to reflect that the prospect accepted them.
        pivot_key=prospect[_ID]
        pivot_order=prospect_data_in_suitor_prefs[1]
        prospect_data_updated = (Estatus.MATCHED, pivot_order)
        _DB_SUITORS[index][_PROSPECTS][pivot_key] = prospect_data_updated
        _DB_SUITORS[index][_MATCHED_ID]= prospect[_ID]
        _DB_SUITORS[index][_MATCHED_NAME]= prospect[_NAME]
    else:
        _DB_SUITORS[index][_ESTATUS]= Estatus.UNMATCHED
        pivot_key=prospect[_ID]
        pivot_order=prospect_data_in_suitor_prefs[1]
        prospect_data_updated = (Estatus.REJECT, pivot_order)
        #update the suitor’s preference list to indicate that the prospect rejected them
        _DB_SUITORS[index][_PROSPECTS][pivot_key] = prospect_data_updated
        _DB_SUITORS[index][_MATCHED_ID] = None
        _DB_SUITORS[index][_MATCHED_NAME] = None
        
def update_prospects(suitor, prospect):
    global _DB_PROSPECTS
    if prospect:
        #index = _DB_PROSPECTS.index(matched_prospect)
        index = prospect[_ID]-1 #_DB_PROSPECTS.index(matched_prospect)
        _DB_PROSPECTS[index][_ESTATUS]= Estatus.MATCHED
        _DB_PROSPECTS[index][_MATCHED_ID]= suitor[_ID]
        _DB_PROSPECTS[index][_MATCHED_NAME]= suitor[_NAME]
        
""""
    suitor viene directo de la base
    prospect_id viene de los ids del suitor
    prospect_data es como vive en los preferences del suitor
"""                
def make_match(suitor, prospect_id, prospect_data_in_suitor_preferences):
    prospect = get_prospect_by_id(prospect_id)
    #print(f"make_match : Prospect = {prospect} - {prospect_id}")
    #Prospect is free? Accept the match
    rejected = None
    if prospect[_ESTATUS] == Estatus.UNMATCHED:
        rejected = False
        update_suitors(suitor, prospect, rejected, prospect_data_in_suitor_preferences)
        update_prospects(suitor, prospect)
        return 0
    else:
        #Prospect prefers the new suitor? Accept the match and reject the old one
        if is_new_suitor_better_than_current(prospect[_PROSPECTS], 
                                             suitor[_ID],
                                             prospect[_MATCHED_ID]):
            #Update old suitor status to UNMATCHED
            old_suitor = get_suitor_by_id(prospect[_MATCHED_ID])
            #global _DB_SUITORS
            old_suitor_index = old_suitor[_ID]-1#_DB_SUITORS.index(old_suitor)
            prospect_data_in_old_suitor_preferences = _DB_SUITORS[old_suitor_index][_PROSPECTS][prospect_id]
            rejected=True
            update_suitors(old_suitor, prospect, rejected, prospect_data_in_old_suitor_preferences)
            #Update new suitor and prospect status to MATCHED
            rejected=False
            update_suitors(suitor, prospect, rejected, prospect_data_in_suitor_preferences)
            update_prospects(suitor, prospect)
            return old_suitor[_ID]
        else:
            #Rejected
            rejected=True
            update_suitors(suitor, prospect, rejected, prospect_data_in_suitor_preferences)
            return -1

def stable_matching():
    print_message(f"\n============> Gale-Shapley Start <============")
    flag = True
    stable_matching=[]
    total_suitors = len(_DB_SUITORS)
    suitor_ids = get_suitors_queue()
    print_message(f"\n==> Suitors Queue Id's -> {suitor_ids}\n")
    while len(stable_matching) < total_suitors:
        #get the top suitor from the queue
        suitor_id = suitor_ids.popleft()
        suitor = get_suitor_by_id(suitor_id)
        #check if suitor is matched
        flag = is_matched(suitor)
        print_message(f"\t==> Suitor(id) -> [{suitor[_ID]}]"
                      f" Preferences -> {suitor[_PROSPECTS].keys()}"
                      f" match to -> [{suitor[_MATCHED_ID]}] status -> [{suitor[_ESTATUS]}]."
                      f" Has (he/she/it) been matched? -> [{flag}]"
                    )
        if not flag:
            filtered_prospects = dict(filter(lambda item:item[1][0] != Estatus.REJECT, suitor[_PROSPECTS].items()))
            for prospect_id, prospect in filtered_prospects.items():
                #print(f'prospect id {prospect_id} prospect {prospect}')
                res = make_match(suitor, prospect_id, prospect)
                if res == -1:
                    print_message(f'\t\t==> Prospect(id) -> [{prospect_id}] rejects suitor(id) -> [{suitor[_ID]}]')
                    continue
                else:
                    stable_matching.append((suitor[_ID], prospect_id))
                    if res == 0:
                        print_message(f"\t\t==> Prospect(id) -> [{prospect_id}] was free, so the match is accepted")
                    else:
                        print_message(f"\t\t==> Prospect(id) -> [{prospect_id}] prefers new suitor(id) -> [{suitor[_ID]}]"
                                      f" over current suitor(id) -> [{res}] so the match is accepted and the old suitor"
                                       f" (id)[{res}] is put back to the queue")
                        stable_matching.remove((res, prospect_id))
                        suitor_ids.append(res)
                    break    
    print_message(f"\n==> Gale-Shapley End")
    return stable_matching            

"""
Aux function to print only id and prospects from database in memory
"""
def print_db_sumary(description, db):
    keys_to_keep = [_ID, _NAME, _MATCHED_NAME, _MATCHED_ID,  _PROSPECTS, ]
    filtered_db = [{key: entry[key] for key in keys_to_keep} for entry in db]
    print_message(f"\n==> {description:<10s}:\n")
    for item in filtered_db:
        print_message(f"\t{item}\n")

def print_result(resultado_ids, params, universe):
    global _DB_SUITORS
    global _DB_PROSPECTS    
    #print(f"\n===> Todos : {resultado_ids }\n")
    suitors_key = params[1].upper().strip()
    if suitors_key=='W':
        #at index 0 I have the keys for women
        resultado_ids.sort(key=lambda x: x[0])        
    else:
        #at index 0 I have the keys for men
        resultado_ids.sort(key=lambda x: x[0])
    #print(f"Params = {params}")
    #print(f"R = {resultado_ids}")
    result_as_string = ""
    for couple in resultado_ids:
        suitor_id = couple[0]
        prospect_id = couple[1]
        #Have the same logic, but just in case somebody decides to change the order       
        if suitors_key=='M':
            #suitors are men
            print(f"{_DB_SUITORS[suitor_id-1][_NAME]} {_DB_PROSPECTS[prospect_id-1][_NAME]}".strip())
            result_as_string = result_as_string + f"{_DB_SUITORS[suitor_id-1][_NAME]} {_DB_PROSPECTS[prospect_id-1][_NAME]} "
        else:
            #suitors are women
            print(f"{_DB_SUITORS[suitor_id-1][_NAME]} {_DB_PROSPECTS[prospect_id-1][_NAME]}".strip())
            result_as_string = result_as_string + f"{_DB_SUITORS[suitor_id-1][_NAME]} {_DB_PROSPECTS[prospect_id-1][_NAME]} "
            
    result_as_string=result_as_string.strip()
        
def proceso(params=None, universe=None):
    if params==None and universe==None:
        params, universe = build_data_test()        
    initialize_db(params, universe)
    resultado = stable_matching()
    print_result(resultado, params, universe)

def main():
    """
    For COAH
    """
    #initial params
    init_params = input().split(" ")
    total_pairs = int(init_params[0])
    universe=[]
    #h m preferences
    for _ in range(total_pairs*2):
        _items = input().strip().split(" ")
        universe.append(_items)
    #print(f"Params ===> {init_params}")
    #print(f"Universe ===> \n{universe}")
    proceso(init_params, universe)

if __name__ == '__main__':
    #COAH
    main()
    #pruebas internas
    #proceso()

