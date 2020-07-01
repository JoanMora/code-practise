def f(fn_1, p, cn_1, i):
    fn = int(fn_1 + (p/100) * fn_1 - cn_1)
    cn = int(cn_1 + cn_1 * (i/100))
    return (fn,cn)

def fortune(f0, p, c0, n, i):
    fn = f0
    cn = c0
    while(n>0 and fn>0):
        fn, cn = f(int(fn),p,int(cn),i)
        n = n - 1
    return fn > 0

def test_fortune():
    assert fortune(100000, 1, 2000, 15, 1) == True
    assert fortune(100000, 1, 9185, 12, 1) == False
    assert fortune(100000000, 1, 100000, 50, 1) == True
    assert fortune(100000000, 1.5, 10000000, 50, 1) == False
    assert fortune(100000000, 5, 1000000, 50, 1) == True
    #assert fortune( 999.5, 61.87, 1000.0, 3, 0 ) == True