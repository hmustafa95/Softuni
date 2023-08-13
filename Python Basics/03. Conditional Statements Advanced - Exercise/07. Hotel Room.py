month = input()
nights = int(input())
price_studio = 0
price_ap = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_ap = 65
    if 13 >= nights > 7:
        price_studio = 50 * 0.95
    elif 14 < nights:
        price_studio = 50 * 0.70
        price_ap = 65 * 0.90
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_ap = 68.70
    if 14 < nights:
        price_studio = 75.20 * 0.80
        price_ap = 68.70 * 0.90
elif month == 'July' or month == 'August':
    price_studio = 76
    price_ap = 77
    if 14 < nights:
        price_ap = 77 * 0.90

ap_total = price_ap * nights
st_total = price_studio * nights

print(f'Apartment: {ap_total:.2f} lv.')
print(f'Studio: {st_total:.2f} lv.')
