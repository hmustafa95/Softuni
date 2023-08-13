length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
volume = length * width * height
volume_liters = volume / 1000
print(volume_liters * (1 - percent))
