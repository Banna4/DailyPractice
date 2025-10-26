# Day 1

# a = [1,2,3,4,5,6,7,8,9,10]
# def is_even(number):
#     even = []
#     for i in number:
#         if i % 2 == 0:
#             even.append(i)
      

#     return even

# print(is_even(a))


# marksheet = {"Aman": 49, "Jatin": 72, "Rohan": 88}
# def is_topper(mark):
#     Topper = max(mark, key=mark.get)
#     return Topper, mark[Topper]

# print(is_topper(marksheet))

# a = "Radisan"
# print(a[::-1])

def starpattern(rows):
    for i in range(1,rows + 1):
        for j in range(i):
            print('*',end=' ')
        print()
rows = 5
starpattern(rows)

