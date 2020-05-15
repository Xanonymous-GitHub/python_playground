# def binary_search(input_list, number, min=None, max=None):
#     if min == None:
#         return binary_search(input_list, number, 0, len(input_list) - 1)
#     if min > max:
#         return -1, 0
#     else:
#         time = 0
#         mid = (int)((min + max) / 2)
#         if input_list(mid) < number:
#             time += 1
#             return binary_search(input_list, number, mid + 1, max)
#         elif input_list(mid) > number:
#             time += 1
#             return binary_search(input_list, number, min, mid - 1)
#             return times += 1
#         else:
#             return mid, time
#
#
# def main():
#     input_list = input()
#     for ele in input_list:
#         list1 = []
#         list1.append(ele)
#     number = int(input())
#     print(' '.join(map(int, binary_search(list1, number, 0, len(list1) - 1)))
#     if __name__ == '__main__':
#         main()
