# function
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    iteration = 0

    while low <= high:
        mid = int(round((low + high) / 2, 0))
        guess = list[mid]
        iteration += 1

        if guess == item:
            return "Iteration: ", iteration, "My number: ", list[mid]
            # return  mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# array
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("You can select your target in this array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]: ")
target = int(input())

# Please write to me the best option for finding a number from an array
print(binary_search(array, target))

# Result: The iteration will be change O (log n)

# I choose third_freelancer he did give me better than another freelancer.