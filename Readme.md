# Numerical computation
It records some code in Matlab,C or Python in numerical anylsis.
## ordinary differential equation
In order to meet the requirements of both calculation speed and accuracy, the four-order Runge Kutta method is generally chosen for the following calculation.
$$
\begin{cases}
	y\prime=f\left( x,y \right)\\
	y\left( a \right) =b\\
\end{cases}
$$
However,this method is mainly for the first order and linear equation.For the second order or nolinear equation,the shooting method or the finite difference method may be an alternative.
