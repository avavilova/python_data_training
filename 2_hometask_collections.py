import random
import string


def create_list_of_random_dicts(x: int, y: int) -> list:
    """To create a list of random number of dicts (from x to y)"""
    n = random.randint(x, y+1)
    random_list = []
    for _ in range(n):
        z = random.randint(x, y + 1)
        random_list.append({random.choice(string.ascii_lowercase): random.randint(0, 101) for _ in range(z)})
    return random_list


def create_dict(initial_list: list) -> dict:
    """To get previously generated list of dicts and create one common dict:
        if dicts have same key, we will take max value, and rename key with dict number with max value
        # if key is only in one dict - take it as is"""
    result_dict = {}
    max_values_dict = {}
    for i in range(len(initial_list)):
        for key, value in initial_list[i].items():
            if key not in max_values_dict:
                max_values_dict[key] = (i, value)
            elif value > max_values_dict[key][1]:
                max_values_dict[key] = (i, value)

    for k, (ind, v) in max_values_dict.items():
        count = sum(1 for d in initial_list if k in d)
        if count > 1:
            final_key = f"{k}_{ind}"
        else:
            final_key = k
        result_dict[final_key] = v
    return result_dict


if __name__ == "__main__":
    list_rand_dict = create_list_of_random_dicts(2, 10)
    print(list_rand_dict)
    updated_dict = create_dict(list_rand_dict)
    print(updated_dict)
