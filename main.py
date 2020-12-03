import random
import time


def generate_numbers(set, n):
    for i in range(n):
        set.append(random.randint(-200, 200))
#
# def merge(set, i_p, i_s, i_k):
#     i_1 = i_p
#     i_2 = i_s
#     p = set
#     for i in range(i_p, i_k):
#         if i_1 == i_s or (i_2 <= i_k and set[i_1] > set[i_2]):
#             p[i] = set[i_2]
#             i_2 += 1
#         else:
#             p[i] = set[i_1]
#             i_1 += 1
#     for i in range(i_p, i_k):
#         set[i] = p[i]
#
    
def merge_sort(set, i_p, i_k):
    i_s = int((i_p + i_k + 1) / 2)
    if i_s - i_p > 1:
        merge_sort(set, i_p, i_s - 1)
    if i_k - i_s > 0:
        merge_sort(set, i_s, i_k)
    i_1 = i_p
    i_2 = i_s
    p = list(set)

    for i in range(i_p, i_k+1):
        if i_1 == i_s or (i_2 <= i_k and set[i_1] > set[i_2]):
            p[i] = set[i_2]
            i_2 += 1
        else:
            p[i] = set[i_1]
            i_1 += 1
    for i in range(i_p, i_k+1):
        set[i] = p[i]


small_set = []
big_set = []

start_time_small = time.perf_counter()

generate_numbers(small_set, 100)
print("Maly zbior liczb")
print("Przed sortowaniem: ")
print(small_set)
merge_sort(small_set, 0, len(small_set)-1)
print("Po sortowaniu: ")
print(small_set)

end_time_small = time.perf_counter()
print(f'Czas: {end_time_small - start_time_small} s')

print("-----------------------")

start_time_big = time.perf_counter()

generate_numbers(big_set, 100000)
print("Duzy zbior liczb")
print("Przed sortowaniem: ")
print(big_set)

print("Po sortowaniu: ")
print(big_set)

end_time_big = time.perf_counter()
print(f'Czas: {end_time_big - start_time_big} s')
