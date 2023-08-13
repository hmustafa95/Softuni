tunnel_location = {'T': []}
N = 1
for x in range(2):
    tunnel_location['T'].append([N, 1])
    N += 1
number = [1, 1]
tunnel_location['T'].remove(number)
player_location = tunnel_location['T'][0][0]
print(tunnel_location)
print(player_location)