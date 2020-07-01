'''
Two kingdoms are at war and, thanks to your codewarrior prowesses, you have been named general by one of the warring states. Your opponent's armies are larger than yours, but maybe you can reach a stalemate or even win the conflict if you are a good strategist.

You control the same number of armies as the rival state, but theirs are generally larger. You have to send a single army to fight each of your opponent's ones.
(It implies there will be as many battles as armies).
There are no possible David-and-Goliath surprises : the outcome of a battle is always the victory of the larger army (or a standoff if both are of the same size).
The winning side is the one which wins the most battles.
The outcome can be a stalemate if both win the same number.

You have to write a function

codewar_result(codewarrior, opponent)
that takes as input each side's armies as arrays of strictly positive integers which represent their sizes. The function returns the strings "Defeat" , "Stalemate" or "Victory" depending on the outcome of the war for your side with an optimal strategy on your behalf.

For example, if you have 3 armies of sizes [1,4,1] and the rival state has armies of sizes [1,5,3] , despite you having on average smaller forces, it is possible to reach a stalemate :

1-1 : standoff
4-3 : victory for you
1-5 : victory for the opposing army
when the dust settles, you have won one battle, lost one, and one was indecisive so

codewar_result([1, 4, 1], [1, 5, 3])
should return "Stalemate".

More examples :
codewar_result([2, 4, 3, 1], [4, 5, 1, 2])
should return "Victory" because it is possible to win by disposing your armies this way :

2-1
4-4
3-2
1-5
thus winning two battles, deadlocking one and losing one.

codewar_result([1, 2, 2, 1], [3, 1, 2, 3])
should return "Defeat" because even with an optimal strategy it is not possible to win. The best you can do is one victory and one tie :

1-3
2-1
2-2
1-3
'''

def codewar_result (codewarrior, opponent) :
    codewarrior.sort()
    opponent.sort(reverse=True)
    cod_warriors = codewarrior.copy()
    num_of_armies = len(codewarrior)
    score = 0


    for army in cod_warriors:
        inferiors = [e for e in opponent if e < army]
        if(inferiors):
            score += 1
            element = inferiors.pop(0)
            opponent.pop(opponent.index(element))
            codewarrior.pop(codewarrior.index(army))

    # compute stalmates
    stalemate = [opponent.pop(opponent.index(army)) for army in codewarrior if army in opponent]
    stalemate = len(stalemate)

    imbalance = (num_of_armies - stalemate) - score
    if(score>imbalance): return "Victory"
    if(score==imbalance): return "Stalemate"
    return "Defeat"


def test_codewar_result():
    assert codewar_result([1, 4, 1], [1, 5, 3]) == 'Stalemate'
    assert codewar_result([2, 4, 3, 1], [4, 5, 1, 2]) == 'Victory'
    assert codewar_result([1, 2, 2, 1], [3, 1, 2, 3]) == 'Defeat'
    assert codewar_result([1, 1, 1, 1], [1, 1, 1, 1]) == 'Stalemate'
    assert codewar_result([5], [6]) == 'Defeat'
    assert codewar_result([2, 1, 3, 1, 1, 3, 3, 2, 3, 1, 1, 1, 3, 1, 3, 1, 3, 3, 1, 2, 3, 3, 1, 3], [4, 4, 1, 4, 3, 1, 4, 4, 3, 2, 1, 2, 1, 3, 3, 1, 4, 4, 3, 2, 3, 2, 4, 1]) == 'Stalemate'