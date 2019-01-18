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
next (slightly better) approximation is 52163/16604.

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

The project could look for 'toy' problems with exact solutions
which can be better interpreted using ratap()

These 'toy's may be have analytic solutions which
are relatively easy to derive but when the results are expressed 
numerically the solutions are less obvious


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

 approximation             error                value          

 1 / 1  * Pi               0.000000000000000	3.141592653589793
 831 / 506  * cbrt(7)     -0.000000138009052	3.141592515580741
 473 / 239  * cbrt(4)      0.000000223317982	3.141592876907775
 355 / 113  ratio          0.000000266764189	3.141592920353983
 830 / 699  * sqrt(7)      0.000000462552711	3.141593116142504
 632 / 569  * sqrt(8)     -0.000000486912127	3.141592166677666
 898 / 777  * e           -0.000000527520009	3.141592126069785
 907 / 622  * cbrt(10)     0.000002625926153	3.141595279515947
 805 / 533  * cbrt(9)     -0.000002639411964	3.141590014177829
 501 / 230  * cbrt(3)      0.000003149558083	3.141595803147876
```

#### python ratap.py -x 5 -n 10000 -b

-x sets number of approximations

-n sets maximum numerator or denominator value (default = 1000)

-b enables Tau matching (2 * Pi)

```
 approximation             error                value          

 1 / 1  * Pi               0.000000000000000	3.141592653589793
 1 / 2  * Tau              0.000000000000000	3.141592653589793
 8153 / 5803  * sqrt(5)    0.000000008921974	3.141592662511767
 9941 / 8372  * sqrt(7)    0.000000010444261	3.141592664034054
 5211 / 4063  * sqrt(6)    0.000000024146643	3.141592677736436
```

#### python ratap.py -v 7.853981633974

-v value is close to 5/2 * Pi

```
top 10 best approximations to 7.853981633974

 approximation             error                value          

 5 / 2  * Pi               0.000000000000483	7.853981633974483
 501 / 92  * cbrt(3)       0.000007873895692	7.853989507869692
 932 / 227  * cbrt(7)     -0.000008672106746	7.853972961867253
 849 / 286  * sqrt(7)      0.000014390829628	7.853996024803628
 757 / 262  * e           -0.000014671594240	7.853966962379760
 689 / 189  * cbrt(10)     0.000015728099904	7.853997362073904
 389 / 90  * cbrt(6)       0.000017372822692	7.853999006796692
 757 / 153  * cbrt(4)      0.000022263672582	7.854003897646582
 395 / 86  * cbrt(5)      -0.000022344005450	7.853959289968549
 425 / 121  * sqrt(5)     -0.000023861763994	7.853957772210006
```

#### python ratap.py 1.414213562373095
```
top 10 best approximations to 1.414213562373095

 approximation             error                value          

 1 / 1  * sqrt(2)          0.000000000000000	1.414213562373095
 1 / 2  * sqrt(8)          0.000000000000000	1.414213562373095
 363 / 553  * cbrt(10)    -0.000000556077301	1.414213006295794
 463 / 681  * cbrt(9)     -0.000000919094047	1.414212643279048
 454 / 463  * cbrt(3)      0.000000919094644	1.414214481467739
 416 / 503  * cbrt(5)      0.000001137065286	1.414214699438381
 456 / 721  * sqrt(5)     -0.000001360237306	1.414212202135789
 571 / 989  * sqrt(6)      0.000001445846515	1.414215008219610
 305 / 682  * sqrt(10)     0.000001520253526	1.414215082626621
 397 / 537  * cbrt(7)      0.000001855803140	1.414215418176235
```

#### python ratap.py -v 0.917795181104714 -x 15

This strange value happens to be 7/11 times the cube root of 3
```
top 15 best approximations to 0.917795181104714

 approximation             error                value          

 7 / 11  * cbrt(3)         0.000000000000000	0.917795181104714
 453 / 844  * cbrt(5)     -0.000000034369473	0.917795146735241
 308 / 723  * cbrt(10)    -0.000000043442445	0.917795137662269
 244 / 553  * cbrt(9)     -0.000000510535700	0.917794670569014
 159 / 245  * sqrt(2)      0.000000559374152	0.917795740478866
 159 / 490  * sqrt(8)      0.000000559374152	0.917795740478866
 178 / 371  * cbrt(7)     -0.000000705273217	0.917794475831497
 551 / 953  * cbrt(4)     -0.000000868791516	0.917794312313198
 448 / 615  * cbrt(2)      0.000000965810576	0.917796146915290
 183 / 542  * e            0.000001082009687	0.917796263114401
 882 / 961  ratio         -0.000001216484527	0.917793964620187
 523 / 987  * sqrt(3)     -0.000001288137619	0.917793892967095
 497 / 984  * cbrt(6)     -0.000001548342952	0.917793632761762
 355 / 614  * cbrt(4)      0.000001844056053	0.917797025160767
 815 / 888  ratio         -0.000002388311921	0.917792792792793
```

#### python ratap.py -v 1.61803398875 -p

-p enables Phi matching (golden ratio)
```
top 10 best approximations to 1.61803398875

 approximation             error                value          

 1 / 1  * Phi             -0.000000000000105	1.618033988749895
 447 / 502  * cbrt(6)     -0.000000313459230	1.618033675290770
 733 / 976  * cbrt(10)    -0.000000558633841	1.618033430116159
 455 / 744  * sqrt(7)     -0.000000592870445	1.618033395879555
 581 / 570  * cbrt(4)      0.000001118607059	1.618035107357059
 987 / 610  ratio         -0.000001201864754	1.618032786885246
 610 / 843  * sqrt(5)     -0.000001407166522	1.618032581583478
 613 / 928  * sqrt(6)      0.000001800394491	1.618035789144491
 307 / 600  * sqrt(10)    -0.000001919297179	1.618032069452821
 516 / 451  * sqrt(2)      0.000001927401923	1.618035916151923
```

#### python ratap.py -2 1 -3 1 -e -x 20

Display ratios only

Options -2 1 and -3 1 set the upper limits for square
and cube roots

-e disables matching with value e

```
top 20 best approximations to 3.141592653589793

 approximation             error                value          

 1 / 1  * Pi               0.000000000000000	3.141592653589793
 355 / 113  ratio          0.000000266764189	3.141592920353983
 333 / 106  ratio         -0.000083219627529	3.141509433962264
 311 / 99  ratio          -0.000178512175652	3.141414141414141
 289 / 92  ratio          -0.000288305763706	3.141304347826087
 267 / 85  ratio          -0.000416183001558	3.141176470588235
 245 / 78  ratio          -0.000567012564152	3.141025641025641
 223 / 71  ratio          -0.000747583167258	3.140845070422535
 201 / 64  ratio          -0.000967653589793	3.140625000000000
 179 / 57  ratio          -0.001241776396811	3.140350877192982
 22 / 7  ratio             0.001264489267350	3.142857142857143
 19 / 6  ratio             0.025074013076873	3.166666666666667
 16 / 5  ratio             0.058407346410207	3.200000000000000
 13 / 4  ratio             0.108407346410207	3.250000000000000
 3 / 1  ratio             -0.141592653589793	3.000000000000000
 2 / 1  ratio             -1.141592653589793	2.000000000000000
 1 / 1  ratio             -2.141592653589793	1.000000000000000
```
