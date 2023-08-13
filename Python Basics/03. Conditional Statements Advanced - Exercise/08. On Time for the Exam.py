hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

if hour_exam == 0:
    hour_exam = 24
if hour_arrival == 0:
    hour_arrival = 0

exam_time = hour_exam * 60 + minute_exam
coming_time = hour_arrival * 60 + minute_arrival
message = ""
diff_time = abs(exam_time - coming_time)

if exam_time >= coming_time:
    if diff_time <= 30:
        message = "On Time"
    else:
        message = "Early"
else:
    message = "Late"
diff_hours = diff_time // 60
diff_minutes = diff_time % 60
if exam_time == coming_time:
    print(message)
elif exam_time > coming_time:
    print(message)
    if diff_hours == 0:
        print(f'{diff_minutes} minutes before the start')
    else:
        if 0 <= diff_minutes <= 9:
            print(f'{diff_hours}:0{diff_minutes} hours before the start')
        else:
            print(f'{diff_hours}:{diff_minutes} hours before the start')
else:
    print(message)
    if diff_hours == 0:
        print(f'{diff_minutes} minutes after the start')
    else:
        if 0 <= diff_minutes <= 9:
            print(f'{diff_hours}:0{diff_minutes} hours after the start')
        else:
            print(f'{diff_hours}:{diff_minutes} hours after the start')

