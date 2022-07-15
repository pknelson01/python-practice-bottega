def count_positives_sum_negatives(arr):
    x = []
    y = 0
    z = []
    
    if arr == []:
        return x
    else:
        for num in arr:
            if num > 0:
                x.append(num)
            if num < 0:
                y += num

        z.append(len(x))
        z.append(y)
        return z

print(count_positives_sum_negatives([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

# print(count_positives_sum_negatives([0,0,0,0,0,0]))
