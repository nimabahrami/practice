import copy

house = [
    {'gym': True,
     'supermarket': False,
     'school': False,
     'office': True},

    {'gym': True,
     'supermarket': True,
     'school': False,
     'office': False},

    {'gym': False,
     'supermarket': False,
     'school': False,
     'office': True},

    {'gym': False,
     'supermarket': False,
     'school': False,
     'office': True},

    {'gym': False,
     'supermarket': False,
     'school': True,
     'office': False},

]

desired = ['gym', 'school', 'office', 'supermarket']


def to_point(item):
    points = []
    for keys in item.keys():
        points.append(0) if item.get(keys) == True else points.append(1)

    return points


total_points = [to_point(items) for items in house]

for index, items in enumerate(total_points):
    for inner_index, point in enumerate(items):
        if point == 1:
            _cursor = copy.deepcopy(index)
            left = _cursor
            right = _cursor
            met_req_l = False
            met_req_r = False
            ldist = 0
            rdist = 0

            while met_req_l == False:
                if left > 0:

                    if total_points[left-1][inner_index] == 0:
                        ldist += 1
                        left -= 1
                        met_req_l = True
                        break
                    else:
                        ldist += 1
                        left -= 1
                if left == 0:
                    break

            while met_req_r == False:
                if right+1 == len(total_points):
                    break
                if right >= 0:

                    if total_points[right+1][inner_index] == 0:
                        rdist += 1
                        met_req_r = True
                    else:
                        rdist += 1
                        right += 1

                if right == len(total_points):
                    break
            if (index == 0 or met_req_l == False) and met_req_r == True:
                total_points[index][inner_index] = rdist
            elif (index == len(total_points)-1 or met_req_r == False) and met_req_l == True:
                total_points[index][inner_index] = ldist
            else:
                if met_req_l == True and met_req_l == True:
                    total_points[index][inner_index] = min(ldist, rdist)


def find_dist(arr):
    return sum([items**2 for items in arr])


def finalized_dist(arr):
    return [find_dist(item) for item in arr]


finalized_list = finalized_dist(total_points)
minimum = min(finalized_list)
index_of_house = finalized_list.index(minimum)+1

print(min(finalized_dist(total_points)), f"best house: {index_of_house}th")
