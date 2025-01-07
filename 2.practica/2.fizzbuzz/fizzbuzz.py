def getFizzbuzz(start: int, end: int) -> list[str]:
    result = []
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result