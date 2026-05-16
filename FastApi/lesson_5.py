my_list = [1, 2, 3, 4, 5]

sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop += x
print(sum_of_for_loop)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in days:
    print(f"Happy {x}!")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
