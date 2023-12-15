def fizzbuzz():
    output = ""
    values = {3: "Fizz", 5: "Buzz"}
    for i in range(1, 101, 1):
        for j in values:
            if i % j == 0:
                output += values.get(j)
        print(i, output)
        output = ""


fizzbuzz()
