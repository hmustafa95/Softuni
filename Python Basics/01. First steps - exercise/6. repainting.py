nylon = (int(input()) + 2) * 1.50
paint = (int(input()) * 1.10) * 14.50
diluent = int(input()) * 5
bags = 0.40
hours = int(input())
workhand = (nylon + paint + diluent + bags) * 0.3 * hours
print(workhand + nylon + paint + diluent + bags)
