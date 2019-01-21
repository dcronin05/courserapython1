def aMethod():
    sh = input("Enter Hours: ")
    sr = input("Enter Rate: ")
    fh = float(sh)
    fr = float(sr)

    if fh > 40:
        reg = fr * fh
        otp = (fh - 40.0) * (fr * .5)
        xp = reg + otp
    else:
        xp = fh * fr

    print("Pay:", xp)

    print(input())


def score(score = float(input("Enter Score: "))):
    
    while not score <= 1.0:
        print("The score is out of range.")
        score = float(input("Enter Score: "))


score()
