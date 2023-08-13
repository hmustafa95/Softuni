pens = 5.80
markers = 7.20
cleaning = 1.20
pack_pens = int(input()) * pens
pack_markers = int(input()) * markers
pack_cleaning = int(input()) * cleaning
discount = int(input()) / 100
print((pack_pens + pack_markers + pack_cleaning) - (pack_pens + pack_markers + pack_cleaning) * discount)
