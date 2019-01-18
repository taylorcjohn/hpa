# ratap

Find rational approximations

### rationale

To obtain insight into underlying solutions and hints to rôle
of symmetry

This function attempts to find close approximations using simple
fractions or measures using common roots such as sqrt(2)

### summary

A long time ago I wrote a simple program to find close rational
approximations to numbers and to show how closely the fractions
approximate the values in question.  For example to find successively
better approximations to Pi : 3/1... 22/7, 179/57... 355/113 etc.

This last fraction (355/113) is an extremely close match to Pi, the
next (slightly better) appromation is 52163/16604.

I decided that it may be useful to apply this exploration to answers
from optimisation methods to try to uncover hidden representations
that would otherwise be difficult to understand. 

For example, if a value is shown to be 7.853981633974 the function can
discover that it is actually extremely close to 5/2 * Pi which may be
useful to help understand the problem.

Optimisation methods often give exact solutions to optimisation
problems but these may be disguised rational answers such as 3/7 or
sqrt(2)/2

The function may have other “guessing” applications

The project should look for 'toy' problems with exact solutions
which can be better interpreted using ratap()
 
These 'toy's may be genuinely geometrical for which analytic solutions
are relatively easy to derive but when expressed numerically are
less obvious

#### Future extensions

* ###### Reciprocals of special values

  For example to discover 1/Pi, 6/(5 * e) etc.

* ###### Trigonometric functions

  For example to discover sin, cos etc. values from common angles 
  such as multiples of 30˚
  
* ###### Optional switch between Pi and Tau

* ###### Change command line handling from getopt to argparse
  
  Among other advantages argparse provides automatic help

* ###### Improve in-code documentation

### Examples

#### python ratap.py

Note that no numerator/denominator values greater than 1000 are
considered by default

Pi is the default internal value for the approximation
```
top 10 best approximations to 3.141592653589793

approximation            error          	value          

1 / 1  * Pi              0.000000000000000	3.141592653589793
355 / 113  ratio         0.000000266764189	3.141592920353983
898 / 777  * e           0.000000527520009	3.141592126069785
501 / 230  * cbrt(3)     0.000003149558083	3.141595803147876
953 / 429  * sqrt(2)     0.000005306646943	3.141597960236736
757 / 655  * e           0.000005868637889	3.141586784951904
263 / 145  * sqrt(3)     0.000010843999347	3.141581809590446
616 / 533  * e           0.000013654845381	3.141578998744412
955 / 383  * cbrt(2)     0.000014056593439	3.141578596996355
642 / 289  * sqrt(2)     0.000016713342827	3.141609366932620
```

#### python ratap.py -x 5 -n 10000 -b

-x sets number of approximations

-n sets maximum numerator or denominator value (default = 1000)

-b enables Tau matching (2 * Pi)

```
top 5 best approximations to 3.141592653589793

approximation            error          	value          

1 / 1  * Pi              0.000000000000000	3.141592653589793
1 / 2  * Tau             0.000000000000000	3.141592653589793
7325 / 6338  * e         0.000000024457305	3.141592678047098
9949 / 3990  * cbrt(2)   0.000000040706562	3.141592612883231
6020 / 3319  * sqrt(3)   0.000000046911685	3.141592606678108
```

#### python ratap.py -v 7.853981633974

-v value is close to 5/2 * Pi

```
top 10 best approximations to 7.853981633974

approximation            error          	value          

5 / 2  * Pi              0.000000000000483	7.853981633974483
8223 / 2846  * e         0.000000089554208	7.853981544419792
9949 / 1596  * cbrt(2)   0.000000101765921	7.853981532208079
9169 / 1651  * sqrt(2)   0.000000288133154	7.853981922107153
4929 / 1087  * sqrt(3)   0.000000362812566	7.853981996786565
5978 / 2069  * e         0.000000372081183	7.853982006055182
7175 / 1151  * cbrt(2)   0.000000584093520	7.853982218067520
1775 / 226  ratio        0.000000666910956	7.853982300884955
9568 / 1757  * cbrt(3)   0.000001048486645	7.853980585487355
6009 / 1082  * sqrt(2)   0.000001079796728	7.853982713770728
```

#### python ratap.py 1.414213562373095
```
top 10 best approximations to 1.414213562373095

approximation            error          	value          

1 / 1  * sqrt(2)         0.000000000000000	1.414213562373095
6608 / 6739  * cbrt(3)   0.000000005377791	1.414213556995304
8119 / 5741  ratio       0.000000010727040	1.414213551646055
5252 / 4679  * cbrt(2)   0.000000020453978	1.414213582827073
3920 / 4801  * sqrt(3)   0.000000030677615	1.414213531695480
4412 / 9801  * Pi        0.000000034402667	1.414213527970428
3531 / 3601  * cbrt(3)   0.000000054054414	1.414213616427509
4756 / 3363  ratio       0.000000062521772	1.414213499851323
3363 / 2378  ratio       0.000000062521775	1.414213624894870
4481 / 8613  * e         0.000000062625622	1.414213499747472
```

#### python ratap.py -v 0.917795181104714 -x 15

This strange value happens to be 7/11 times the cube root of 3
```
top 15 best approximations to 0.917795181104714

approximation            error          	value          

7 / 11  * cbrt(3)        0.000000000000000	0.917795181104714
159 / 245  * sqrt(2)     0.000000559374152	0.917795740478866
448 / 615  * cbrt(2)     0.000000965810576	0.917796146915290
183 / 542  * e           0.000001082009687	0.917796263114401
882 / 961  ratio         0.000001216484527	0.917793964620187
523 / 987  * sqrt(3)     0.000001288137619	0.917793892967095
815 / 888  ratio         0.000002388311921	0.917792792792793
195 / 368  * sqrt(3)     0.000003480514664	0.917798661619378
748 / 815  ratio         0.000003770061769	0.917791411042945
681 / 742  ratio         0.000005423692315	0.917789757412399
279 / 383  * cbrt(2)     0.000006314771708	0.917801495876422
614 / 669  ratio         0.000007438204863	0.917787742899851
169 / 232  * cbrt(2)     0.000007864586466	0.917787316518248
157 / 465  * e           0.000009703538972	0.917785477565742
547 / 596  ratio         0.000009946205385	0.917785234899329
```
