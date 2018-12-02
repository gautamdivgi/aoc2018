import sys

def main():
    initial_freq = 0
    with open('day_1_input.txt', 'r') as fid:
        for line in fid:
            l = line.strip()
            sign = l[:1]
            freq = int(l[1:])
            if sign == '+':
                initial_freq += freq
            elif sign == '-':
                initial_freq -= freq
            else:
                print 'bad sign {:s} {:s}'.format(sign, l)
    print initial_freq
    return 0

if __name__ == '__main__':
    sys.exit(main())