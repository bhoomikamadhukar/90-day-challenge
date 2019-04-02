def birthdayCakeCandles(ar):
    max_h = ar[0]
    max_n = 1
    for c in ar[1:]:
        if c > max_h:
            max_h = c
            max_n = 1
        elif c == max_h:
            max_n += 1
    return max_n