# Recamán's Series
*It is basically a function with domain and co-domain as natural numbers and 0. It is recursively defined as below:*

Specifically, let a(n) denote the (n+1)-th term. (0 is already there). 

***The rule says:***
```
a(0) = 0
if n > 0 and the number is not already included in the sequence
    a(n) = a(n - 1) - n
else
    a(n) = a(n-1) + n
```
## Here is a visualization of the path:
![Image](https://3.bp.blogspot.com/-hTVrDPSYmXM/Wy8JnuXkSkI/AAAAAAAAKiE/8TdWhmlpIsgQrf-XjZCjtIGp-H-wMU9LQCLcBGAs/s1600/Heading.png)

Generate for yourself:

`Generate`|`File`
--------|-----
Generate Series| [Rackeman_Series.py](./Rackeman_Series.py)
Generate Diagram| [Visualizing_Sequence.py](./Rackeman_Series.py)

## More on the Recamán's Series by [**Numberphile**](https://www.youtube.com/watch?v=FGC5TdIiT9U)