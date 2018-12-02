import sys

def puz1(initial_freq, freq_seen):
    dup_found = False
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
                raise RuntimeError('bad sign {:s} {:s}'.format(sign, l))
            if initial_freq in freq_seen:
                dup_found = True
                break
            else:
                freq_seen.add(initial_freq)

    return initial_freq, dup_found

def puz2():
    initial_freq = 0
    freq_seen = set([0])
    dup_found = False
    while not dup_found:
        initial_freq, dup_found = puz1(initial_freq, freq_seen)
    print initial_freq
    return 0

if __name__ == '__main__':
    sys.exit(puz2())