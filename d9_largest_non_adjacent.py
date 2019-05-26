# def largest_non_adjacent(arr):
#     if not arr:
#         return 0

#     return max(
#             largest_non_adjacent(arr[1:]),
#             arr[0] + largest_non_adjacent(arr[2:]))

# def largest_non_adjacent(arr):
#     if len(arr) <= 2:
#         return max(0, max(arr))

#     cache = [0 for i in arr]
#     cache[0] = max(0, arr[0])
#     cache[1] = max(cache[0], arr[1])

#     for i in range(2, len(arr)):
#         num = arr[i]
#         cache[i] = max(num + cache[i - 2], cache[i - 1])
#     return cache[-1]

def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last= max(0, arr[0])
    # max_excluding_last= arr[0]
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)

print(largest_non_adjacent([5,1,1,5]))
print(largest_non_adjacent([-5,-1,-1,-5]))