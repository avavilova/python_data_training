# Write a code, which will:
#
# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.
import random
import string


def create_list_of_random_dicts(x: int, y:int) -> list:
    n = random.randint(x, y+1)
    l = []
    for _ in range(n):
        z = random.randint(x, y + 1)
        l.append({random.choice(string.ascii_lowercase): random.randint(0, 101) for _ in range(z)})
    return l

def create_dict(l1: list) -> dict:
    result_dict = {}
    for i in range(len(l1)):
        for key in l1[i].keys():
            if key in result_dict:
                if l1[i][key] >= result_dict[key]:
                    result_dict.pop(key)
                    result_dict.update({f'{key}_{i}': l1[i][key]})
                else:
                    result_dict.update({key: l1[i][key]})
            else:
                result_dict.update({key: l1[i][key]})
    return result_dict




if __name__ == "__main__":
    list_rand_dict = create_list_of_random_dicts(2, 10)
    print(list_rand_dict)
    updated_dict = create_dict(list_rand_dict)
    print(updated_dict)