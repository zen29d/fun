import random, time

#define tree
tree = ['          *',
        '         ***',
        '        *****',
        '       *******',
        '      *********',
        '     ***********',
        '    *************',
        '   ***************',
        '  *****************',
        ' *******************',
        '         * *          ',
        '         * *           ',
        '         * *             ',
        '     ***********          '
]


print('\n')
# display normal tree
for i in range(len(tree)):
    print(tree[i],flush=True)
time.sleep(1)

#display color tree
for i in range(5):
    print(u"\u001b[{}A".format(14),end="")
    code = [random.randint(1, 256) for iter in range(14)]
    for i in range(len(tree)):
        print("\u001b[38;5;" + str(code[i]) + "m",end="")
        print(tree[i],flush=True)
        time.sleep(.05)
    

print('\u001b[0m\n🎄🎅🏻Merry Christmas🎅🏻🎄\n')
