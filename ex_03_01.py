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


aMethod()
