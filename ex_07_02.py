file = open('mbox-short.txt', 'r')

average = 0.0
counter = 0

for line in file:
    if line.lower().startswith("x-dspam-confidence:"):
        average += line[line.find(':')+2:]
        counter += 1

print("Average: {}".format(average))