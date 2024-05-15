# CodeWars_Medium_2 => DONE BY Azizbek;

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(ls_1 : list, ls_2 : list) -> list:
    natija = []

    for i in ls_1:
        if i not in ls_2:
            natija.append(i)

    return natija
