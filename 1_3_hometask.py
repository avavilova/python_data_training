import random


def create_random_numbers_list(n: int, x: int, y: int) -> list:
    """Function to create list of n random numbers from x to y"""
    return [random.randrange(x, y+1) for i in range(n)]


def sort_list(l1: list) -> list:
    """Function to sort list from min to max (without using sort())"""
    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] >= l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    return l1


def calculate_average(l2: list):
    """Function to calculate and print average for even and odd numbers"""
    even_numbers = []
    odd_numbers = []
    for i in l2:
        if i%2 == 0:
            odd_numbers.append(i)
        else:
            even_numbers.append(i)
    even_avg = sum(even_numbers)/len(even_numbers)
    odd_avg = sum(odd_numbers)/len(odd_numbers)
    print(f"The average of even numbers is {even_avg:.2f}, the average of odd numbers is {odd_avg:.2f}")


if __name__ == "__main__":
    random_numbers = create_random_numbers_list(100, 0, 1000)
    print(random_numbers)
    sorted_list = sort_list(random_numbers)
    print(sorted_list)
    calculate_average(sorted_list)


