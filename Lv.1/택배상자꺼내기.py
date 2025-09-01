def solution(n, w, num):
    box_pos = [0, 0, 0]
    box_set = []
    answer = 0
    for i in range(n):
        if i % w == 0:
            box_pos[0] += 1
            box_pos[1] += 1
            box_pos[2] = 0
            box_set.append(box_pos.copy())
        else:
            box_pos[1] += 1
            box_pos[2] += 1
            box_set.append(box_pos.copy())
    for box in box_set:
        if box[0] % 2 == 0:
            box[2] = abs(box[2] - w+1)
    for box in box_set:
        if box[1] == num:
            box_floor = box[0]
            out_box = box[2]
            break
    for box in box_set:
        # print(box)
        if box[2] == out_box and box[0] >= box_floor:
            answer += 1
    return answer