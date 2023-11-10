import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), 
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), 
              ('-ele-phant','relev--ant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return 1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:]))

# print(MED(test_cases[1][0],test_cases[1][1]))

def fast_MED(S, T, MED={}):
    # print(MED)
    # print(S,T)
    if (S, T) in MED:
        return MED[(S, T)]
    if len(S) == 0:
        MED[(S, T)] = len(T)
    elif len(T) == 0:
        MED[(S, T)] = len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        '''COMMENTED OUT VERSION THAT ACCOUNTS FOR SWAPS'''
        # MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), 
        #                     fast_MED(S[1:], T, MED), 
        #                     fast_MED(S[1:], T[1:], MED))

        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), 
                            fast_MED(S[1:], T, MED))

    return MED[(S, T)]

# print(fast_MED(test_cases[1][0],test_cases[1][1]))


def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if len(S) == 0:
        MED[(S, T)] = (len(T), ('-' * len(T), T))
    elif len(T) == 0:
        MED[(S, T)] = (len(S), (S, '-' * len(S)))
    elif S[0] == T[0]:
        here = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (here[0], (S[0] + here[1][0], T[0] + here[1][1]))
    else:

        insert = fast_align_MED(S, T[1:], MED)
        delete = fast_align_MED(S[1:], T, MED)

        if insert[0] <= delete[0]:
            MED[(S, T)] = (1 + insert[0], ('-' + insert[1][0], 
                                           T[0] + insert[1][1]))
        else:
            MED[(S, T)] = (1 + delete[0], (S[0] + delete[1][0], 
                                           '-' + delete[1][1]))
    
    return MED[(S, T)]

# print(fast_align_MED(test_cases[2][0],test_cases[2][1]))
# print(fast_align_MED('jk',''))
# print(MED('elephant', 'back'))

def test_MED():
    for S, T in test_cases:
        # print(S,T)
        # print(fast_MED(S, T))
        # print(MED(S, T))
        assert fast_MED(S, T) == MED(S, T)

test_MED()
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)[1]
        # assert (align_S == alignments[i][0] and align_T == alignments[i][1])
        print('Mine:', align_S, align_T)
        print('Prof:', alignments[i][0], alignments[i][1])
        print('number of edits:',fast_align_MED(S, T)[0])
        print()

test_align()
