def time_converter(time):
    h, m = map(int, time.split(':'))
    ampm = 'a.m.' if h < 12 else 'p.m.'
    if h == 0: h = 12
    elif h >= 13: h -= 12
    return '%d:%02d %s' % (h, m, ampm)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
