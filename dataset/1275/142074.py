for i in range(2992, 10000):
    x = i
    b12 = 0
    s12 = 0
    while x > 0:
        b12 = x % 12
        x = x // 12
        s12 = s12 + b12
    x = i
    b16 = 0
    s16 = 0
    while x > 0:
        b16 = x % 16
        x = x // 16
        s16 = s16 + b16
    x = i
    b10 = 0
    s10 = 0
    while x > 0:
        b10 = x % 10
        x = x // 10
        s10 = s10 + b10
    if s10 == s16 and s10 == s12:
        print(i)