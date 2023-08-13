def flights(*args):
    dict_flights = {}
    for idx in range(0, len(args), 2):
        if args[idx] == 'Finish':
            break
        if args[idx] not in dict_flights:
            dict_flights[args[idx]] = 0
        dict_flights[args[idx]] += args[idx + 1]
    return dict_flights
