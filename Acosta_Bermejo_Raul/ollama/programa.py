from typing import List, Dict

def stable_matching(num_students: int, num_houses: int, preferences: Dict[int, List[int]]) -> List[int]:
    matching: List[int] = [0] * num_students
    free_students: List[int] = list(range(num_students))
    free_houses: List[int] = list(range(num_houses))

    while free_students and free_houses:
        student = free_students.pop(0)
        house = None

        for pref in preferences[student]:
            if pref in free_houses:
                house = pref
                break

        if house:
            free_houses.remove(house)
            matching[student] = house
            for pref in preferences[student]:
                if pref == house:
                    continue
                free_students.append(pref)
        else:
            free_students.append(student)

    return matching