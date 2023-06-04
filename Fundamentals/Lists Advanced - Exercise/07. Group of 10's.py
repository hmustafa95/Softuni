received_list = input().split(", ")
numbers = [int(x) for x in received_list]
copy_list = numbers.copy()
groups = 10

while len(numbers) > 0:
    tens = []
    for num in numbers:
        if num <= groups:
            tens.append(num)
    print(f"Group of {groups}'s: {tens}")
    for copy_num in tens:
        if copy_num in numbers:
            numbers.remove(copy_num)
    groups += 10
