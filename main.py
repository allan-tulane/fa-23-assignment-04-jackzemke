import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), 
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), 
              ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

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
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), 
                            fast_MED(S[1:], T, MED), 
                            fast_MED(S[1:], T[1:], MED))

    return MED[(S, T)]

# print(fast_MED(test_cases[1][0],test_cases[1][1]))

def fast_align_MED(S, T, MED={}, alignment={}):
    # print(MED)
    # num = fast_MED(S,T)
    
    # print(S,T)

    if (S, T) in MED:
        return MED[(S, T)]
    if len(S) == 0:
        MED[(S, T)] = (len(T), ('-'*len(T), T))
    elif len(T) == 0:
        MED[(S, T)] = (len(S), (S, '-'*len(S)))
    elif S[0] == T[0]:
        MED[(S, T)] = (fast_align_MED(S[1:], T[1:], MED)[0], (S[0], T[0]))
    else:
        choice1 = fast_align_MED(S, T[1:], MED)[0]
        choice2 = fast_align_MED(S[1:], T, MED)[0]
        choice = min(choice1, choice2)

        if choice1 == choice:
            MED[(S, T)] = (1 + choice1, (S, '-' + T[1]))
        elif choice2 == choice:
            MED[(S, T)] = (1 + choice2, ('-' + S[1], T))

    # print(MED)
    # print()
    return MED[(S, T)]



print(fast_align_MED(test_cases[2][0],test_cases[2][1]))
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
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
