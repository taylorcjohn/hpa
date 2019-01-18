# ratap

Find rational approximations

### rationale

To obtain insight into underlying solutions and hints to rôle
of symmetry

This function attempts to find close approximations using simple
fractions or measures using common roots such as sqrt(2)

#### summary

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

## Future extensions

* ###### Reciprocals

  For example to discover 1/Pi, 6/(5 * e) etc.

* ###### Trigonometric functions

  For example to discover sin, cos etc. values from common angles 
  such as multiples of 30˚
  
* ###### Optional switch between Pi and Tau

* ###### Change command line handling from getopt to argparse
  
  Among other advantages argparse provides automatic help

* ###### Improve in-code documentation


### Examples

#### python ratap.py 1.414213562373095
```
top 10 best approximations to 1.414213562373095

1 / 1  * sqrt(2)         0.000000000000000	1.414213562373095
6608 / 6739  * cbrt(3)   0.000000005377791	1.414213556995304
8119 / 5741  ratio       0.000000010727040	1.414213551646055
5252 / 4679  * cbrt(2)   0.000000020453978	1.414213582827073
3920 / 4801  * sqrt(3)   0.000000030677615	1.414213531695480
4412 / 9801  * Pi        0.000000034402667	1.414213527970428
2206 / 9801  * Tau       0.000000034402667	1.414213527970428
3531 / 3601  * cbrt(3)   0.000000054054414	1.414213616427509
4756 / 3363  ratio       0.000000062521772	1.414213499851323
3363 / 2378  ratio       0.000000062521775	1.414213624894870
```

#### python ratap.py -x 15 -2 10 -n 1000
```
top 15 best approximations to 3.141592653589793

1 / 1  * Pi              0.000000000000000	3.141592653589793
1 / 2  * Tau             0.000000000000000	3.141592653589793
355 / 113  ratio         0.000000266764189	3.141592920353983
830 / 699  * sqrt(7)     0.000000462552711	3.141593116142504
632 / 569  * sqrt(8)     0.000000486912127	3.141592166677666
898 / 777  * e           0.000000527520009	3.141592126069785
501 / 230  * cbrt(3)     0.000003149558083	3.141595803147876
463 / 361  * sqrt(6)     0.000003315892809	3.141589337696984
811 / 683  * sqrt(7)     0.000005079251019	3.141587574338774
953 / 429  * sqrt(2)     0.000005306646943	3.141597960236736
757 / 655  * e           0.000005868637889	3.141586784951904
911 / 917  * sqrt(10)    0.000006014098633	3.141586639491160
170 / 121  * sqrt(5)     0.000009544705791	3.141583108884002
759 / 764  * sqrt(10)    0.000010527846599	3.141582125743194
263 / 145  * sqrt(3)     0.000010843999347	3.141581809590446
```

#### python ratap.py -v 7.853981633974
```
top 10 best approximations to 7.853981633974

5 / 2  * Pi              0.000000000000483	7.853981633974483
5 / 4  * Tau             0.000000000000483	7.853981633974483
8223 / 2846  * e         0.000000089554208	7.853981544419792
9949 / 1596  * cbrt(2)   0.000000101765921	7.853981532208079
9169 / 1651  * sqrt(2)   0.000000288133154	7.853981922107153
4929 / 1087  * sqrt(3)   0.000000362812566	7.853981996786565
5978 / 2069  * e         0.000000372081183	7.853982006055182
7175 / 1151  * cbrt(2)   0.000000584093520	7.853982218067520
1775 / 226  ratio        0.000000666910956	7.853982300884955
9568 / 1757  * cbrt(3)   0.000001048486645	7.853980585487355
```

#### python ratap.py -v 0.917795181104714 -3 4
```
top 10 best approximations to 0.917795181104714

7 / 11  * cbrt(3)        0.000000000000000	0.917795181104714
8675 / 9452  ratio       0.000000005480507	0.917795175624207
718 / 1355  * sqrt(3)    0.000000006964994	0.917795188069708
3863 / 4209  ratio       0.000000019655562	0.917795200760276
1513 / 2077  * cbrt(2)   0.000000020540947	0.917795160563767
1941 / 6644  * Pi        0.000000023684237	0.917795204788951
6421 / 9894  * sqrt(2)   0.000000024040064	0.917795157064650
3059 / 9060  * e         0.000000025116169	0.917795155988545
1621 / 4801  * e         0.000000037377292	0.917795218482006
6262 / 9649  * sqrt(2)   0.000000038853670	0.917795142251044
```
