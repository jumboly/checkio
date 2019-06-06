FROM_MIN = 6 * 60
TO_MIN = 18 * 60

def sun_angle(time):
    h, m = map(int, time.split(":"))
    
    min = h * 60 + m
    if min < FROM_MIN or TO_MIN < min:
        return "I don't see the sun!"

    return 180 * ((min - FROM_MIN) / (TO_MIN - FROM_MIN))


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")