elements = input().split()

number_of_moves = 0
while True:
    sequences = input().split()
    if "end" in sequences:
        break
    number_of_moves += 1

    first_index = int(sequences[0])
    second_index = int(sequences[1])
    if first_index == second_index or 0 > first_index or first_index >= len(elements) or 0 > second_index or \
            second_index >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        middle = len(elements) // 2
        elements.insert(middle, f"-{number_of_moves}a")
        elements.insert(middle, f"-{number_of_moves}a")
    else:
        if elements[first_index] == elements[second_index]:
            removed_one = elements[first_index]
            elements.remove(removed_one)
            elements.remove(removed_one)
            print(f"Congrats! You have found matching elements - {removed_one}!")
        else:
            print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break

if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements))
