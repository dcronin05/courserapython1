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


def score():
    
    while True:
        score = float(input("Enter Score: "))
        if score >= 0.0 and score <= 1.0:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            else:
                print("D")
            break
        else:
            print("Incorrect score.")


def computepay(hr, 
    rate):
    
    if hr > 40:
        return (hr - 40) * (rate * 1.5) + (40 * rate)
    else:
        return hr * rate


print(computepay(int(input("Enter hours: ")), float(input("Enter rate: "))))
