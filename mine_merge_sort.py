import datetime


def merge_sort(p1s, p2s, b1, b2, meeting_time):

    p1s_flat, p2s_flat = [], []
    p1s = [time_interval_creator(items) for items in p1s]
    b1 = time_interval_creator(b1)
    for items in p1s:
            p1s_flat+=items

    p2s = [time_interval_creator(items) for items in p2s]
    b2 = time_interval_creator(b2)
    for items in p2s:
            p2s_flat+=items
    p1s = p1s_flat
    p2s = p2s_flat
    result = []
    p1index = p2index = 0

    while len(result) < len(p1s)+len(p2s):
        if p1s[p1index] < p2s[p2index]:
            result.append(p1s[p1index])
            p1index += 1
        else:
            result.append(p2s[p2index])
            p2index += 1

        if p1index == len(p1s):
            result += p2s[p2index:]

        if p2index == len(p2s):
            result += p1s[p1index:]

    total_interval = total_time_bounded(b1, b2)
    available_minutes = [_min for _min in total_interval if _min not in result]
    available_interval, cursor = [], []
    for _min in available_minutes:
        if _min+1 in available_minutes:
            cursor.append(_min)
        else:
            available_interval.append(cursor)
            cursor = []

    final_res_in_time_string = [to_time_string(
        items) for items in available_interval if len(items) >= meeting_time-1]

    return final_res_in_time_string


def total_time_bounded(b1, b2):
    return[item for item in b1 if item in b2]


def time_interval_creator(time_int):
    time1h, time1m = map(int, time_int[0].split(':'))
    time2h, time2m = map(int, time_int[1].split(':'))
    return(range(time1h*60+time1m, time2h*60+time2m, 1))


def to_time_string(t):
    t[-1] = t[-1]+2
    t_start_hour = t[0]//60
    t_start_min = t[0] % 60
    t_end_hour = t[-1]//60
    t_end_min = t[-1] % 60
    return [f'{t_start_hour}:{t_start_min}' if t_start_min != 0 else f'{t_start_hour}:00',
            f'{t_end_hour}:{t_end_min}' if t_end_min != 0 else f'{t_end_hour}:00']


start_fun = datetime.datetime.now()
print(merge_sort([['9:00', '9:20'], ['12:00', '13:00'], ['16:00', '18:20']],
                 [['10:00', '11:30'], ['12:30', '14:30'], [
                     '14:30', '15:00'], ['16:00', '17:00']],
                 ['9:00', '20:00'],
                 ['9:00', '18:30'],
                 30))
end_fun = datetime.datetime.now() - start_fun

print(end_fun)
