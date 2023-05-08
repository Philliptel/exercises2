def count_a_number(numbers, number):
    count = 0
    for element in numbers:
        if element == number:
            count += 1
    return count


print(count_a_number(list((1, 2, 3, 1, 2, 3, 1, 1, 5)), 1))


def play_with_lists(numbers, number):

    numbers2 = numbers.copy()
    numbers2.reverse()
    print(numbers2)
    numbers2.reverse()

    numbers2.remove(number)
    numbers2.insert(6,1)
    print(numbers2)

    numbers_sorted = numbers.copy()
    numbers_sorted.sort()
#"""Ich habe .sort() verwendet weil sorted(list) nicht funktioniert hat.. """
    numbers_sorted.reverse()
    print(numbers_sorted)


play_with_lists([1,2,3,4,5,5,6,7,333,2,99], 6)


def compare_lists(list1, list2):
    compared_list = []
    for x in list1:
        if x in list2:
            compared_list.append(x)
    print(compared_list)
compare_lists([1,2,3,"apple","banana","orange"],[4,5,6,"apple","cherry","orange"])


def remove_duplicates(items):
    items2 = []
    for thing in items:
        if thing not in items2:
            items2.append(thing)
    items2.sort()
    return items2

print(remove_duplicates(["Ball", "Pencil", "Cup", "Ball", "Book", "Phone", "Ball", "Cup", "Charger"]))


def remove_duplicates_my_way(items):
    for thing in items:
        while items.count(thing) > 1:
              items.remove(thing)
    items.sort()
    return items

print(remove_duplicates_my_way(["Ball", "Pencil", "Cup", "Ball", "Book", "Phone", "Ball", "Cup", "Charger"]))


def describe_computer(computer):
    type2 = computer.get("Type", "unknown type")
    brand2 = computer.get("Brand", "unknown brand")
    price2 = computer.get("Price", "unknown price")
    print(f"You have a {type2} from {brand2} that costs {price2}€.")
    computer["OS"] = "Linux"
    print(computer)
describe_computer({"Type":"Notebook", "Price": 1500})