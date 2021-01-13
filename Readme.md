# Implementation Of Leaky-integrate and fire model(LIF) and Exponential-LIf(Non-linear LIF) and Adaptive-ELIF in Python.

- `my_plot` function in MyPlot file uses `matplotlib` which is a library for plotting in python.
- LIF directory contains a file for implementing LIF Model.
- AELIF and NLIF are same as LIF.
- In all of implementations dt considered 1 `dt = 1` in calculations, because of computational resource.
- But it can be any value if the resource is sufficient.
- For discretization I used `List`s which is a tool in python, in other languages same things like <vector> in c++
- can be used.
- In frequency function in NLIF and LIF Model , the value is not accurate when length of spike list is 1.
- In AELIF we can't have frequency because interspike intervals are changing.
- Other stuffs are explained in comments in my code.
Thanks for reading.
