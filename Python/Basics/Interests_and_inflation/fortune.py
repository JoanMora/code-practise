'''
John has some amount of money of which he wants to deposit a part f0 to the bank at the beginning of year 1. He wants to withdraw each year for his living an amount c0.

Here is his banker plan:

deposit f0 at beginning of year 1
his bank account has an interest rate of p percent per year, constant over the years
John can withdraw each year c0, taking it whenever he wants in the year; he must take account of an inflation of i percent per year in order to keep his quality of living. i is supposed to stay constant over the years.
all amounts f0..fn-1, c0..cn-1 are truncated by the bank to their integral part
Given f0, p, c0, i the banker guarantees that John will be able to go on that way until the nth year.
Example:
f0 = 100000, p = 1 percent, c0 = 2000, n = 15, i = 1 percent
beginning of year 2 -> f1 = 100000 + 0.01*100000 - 2000 = 99000;  c1 = c0 + c0*0.01 = 2020 (with inflation of previous year)
beginning of year 3 -> f2 =  99000 + 0.01*99000 - 2020  = 97970;  c2 = c1 + c1*0.01 = 2040.20
(with inflation of previous year, truncated to 2040)
beginning of year 4 -> f3 =  97970 + 0.01*97970 - 2040  = 96909.7 (truncated to 96909);
c3 = c2 + c2*0.01 = 2060.4 (with inflation of previous year, truncated to 2060)
and so on...

John wants to know if the banker's plan is right or wrong. Given parameters f0, p, c0, n, i build a function fortune which returns true if John can make a living until the nth year and false if it is not possible.

Some cases:
fortune(100000, 1, 2000, 15, 1) -> True
fortune(100000, 1, 10000, 10, 1) -> True
fortune(100000, 1, 9185, 12, 1) -> False

For the last case you can find below the amounts of his account at the beginning of each year:
100000, 91815, 83457, 74923, 66211, 57318, 48241, 38977, 29523, 19877, 10035, -5
f11 = -5 so he has no way to withdraw something for his living in year 12.
Note: Don't forget to convert the percent parameters as percentages in the body of your function: if a parameter percent is 2 you have to convert it to 0.02.
'''

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