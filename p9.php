<?
/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*/
$p = 0;
$s = 1000;
$a = 1;
$b = 2;
$c = 997;

while ($c > 334) {
    while ( $a < $b ) {
        if ($a>0 && $a<$b && $b<$c && ($a+$b+$c)==$s) {
            if ( pow($a, 2) + pow($b, 2) == pow($c, 2) ) {
                print "{$a} + {$b} + {$c} = {$s}\n";
                print ($a*$b*$c)."\n";
                break 2;
            }
        }
        $a++;
        $b = $s - $c - $a;
    }

    $c--;
    $a = 1;
    $b = $s - $c - $a;
}

