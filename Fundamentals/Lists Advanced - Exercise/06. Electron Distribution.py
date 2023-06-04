electrons = int(input())
layers = []
left_electrons = electrons
counter = 1

if electrons > 2:
    while True:
        append_electrons = 2 * (counter ** 2)
        counter += 1
        if left_electrons >= append_electrons:
            layers.append(append_electrons)
            left_electrons -= append_electrons
        else:
            if left_electrons > 0:
                layers.append(left_electrons)
                break
            else:
                break
else:
    layers.append(electrons)

print(layers)
