input = 'R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3'

list = [x.strip() for x in input.split(',')]
direction = 'N'
xAxis = 0
yAxis = 0

for x in list:
    if x[0] =='R':
        if direction == 'N':
            direction = 'E'
            xAxis += int(x[1:])
        elif direction == 'E':
            direction = 'S'
            yAxis -= int(x[1:])
        elif direction == 'W':
            direction = 'N'
            yAxis += int(x[1:])
        elif direction == 'S':
            direction = 'W'
            xAxis -= int(x[1:])
        else:
            print 'Error'
    elif x[0] == 'L':
        if direction == 'N':
            direction = 'W'
            xAxis -= int(x[1:])
        elif direction == 'E':
            direction = 'N'
            yAxis += int(x[1:])
        elif direction == 'W':
            direction = 'S'
            yAxis -= int(x[1:])
        elif direction == 'S':
            direction = 'E'
            xAxis += int(x[1:])
        else:
            print 'Error'        
    else:
        print 'Error'

    print "x: %s y: %s" % (xAxis, yAxis)
