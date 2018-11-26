multiplier = 5
for i in range (1, 11):
    print i, "x", multiplier, "=", i * multiplier

for multiplier in range (5, 8):
    for i in range (1, 11):
        print i, "x", multiplier, "=", i * multiplier
        print

numStars = int(raw_input ("How many stars do you want? "))
for i in range (1, numStars):
    print '*',

numStars = int(raw_input ("How many stars do you want? "))
for i in range(1, numStars + 1):
    print '*',

numStars = int(raw_input ("How many stars do you want? "))
for i in range (0, numStars):
    print '*',

numLines = int(raw_input ("How many line of stars do you want? "))
numStars = int(raw_input ("How many stars per line? "))
for line in range (0, numLines):
    for star in range (0, numStars):
        print '*',
    print

numBlocks = int(raw_input ("How many blocks of stars do you want? "))
numLines = int(raw_input ("How many lines in each block? "))
numStars = int(raw_input ("How many stars per line? "))
for block in range(0, numBlocks):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print'*',
        print
    print

numBlocks = int(raw_input ("How many blocks of stars do you want? "))
for block in range(1, numBlocks + 1):
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print '*',
        print ' line = ', line, 'star =', star
    print

    print "\tDog \tBun \tKetcup\tMustard\tOnions"
    count = 1

for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print "#", count, "\t",
                    print dog, "\t", bun, "\t", ketchup, "\t",
                    print mustard, "\t", onion
                    count = count + 1

    dog_cal = 140
    bun_cal = 120
    mus_cal = 20
    ket_cal = 80
    onion_cal = 40

    tot_cal = (dog * dog_cal) + (bun * bun_cal) + \
              (mustard * mus_cal) + (ketchup * ket_cal) + \
              (onion * onion_cal)
    
total_cal = ((dog * dog_cal) + (bun * bun_cal) +
             (mustard * mus_cal) + (ketchup * ket_cal) +
             (onion * onion_cal))

dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print "\tDog \tBun \tKetchup\tMustard\tOnions\tCalorias"
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (bun * bun_cal)+(dog * dog_cal) + \
                                (ketchup * ket_cal)+(mustard * mus_cal) + \
                                    (onion * onion_cal)
                    print "#", count, "\t",
                    print dog, "\t", bun, "\t", ketchup, "\t",
                    print mustard, "\t", onion,
                    print "\t", total_cal
                    count = count + 1


                    
