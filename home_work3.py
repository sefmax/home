def common_elements():

    list1 = [i for i in range(101) if i % 3 == 0]
    list2 = [i for i in range(101) if i % 5 == 0]

    set1, set2 = set(list1), set(list2)

    common = set1.intersection(set2)

    print(common)
    return common


common_elements()