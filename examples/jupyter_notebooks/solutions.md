# Solutions

## Fitting curves to points

### Exercise 1: 

```python
plt.plot(x, y, "ok")
```

### Exercise 2:

```python
f(x) - y
```

### Exercise 3:

```python
coeffs = np.polyfit(x_exercise3, y_exercise3, deg=1)
print(coeffs)
g = np.poly1d(coeffs)

# Some points where we evaluate our new function
x_new = np.linspace(x[0], x[-1], 50)
y_new = g(x_new)

# Plot the datapoints
plt.plot(x, y, 'ko', label="data")

# Plot our fitted polynomial
plt.plot(x_new, y_new, 'r-', label="fit")

# Add legend etc
plt.legend()
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
```

### Exercise 4a

Simply replace the function definition with

```python
def gaus(x, norm, mean):
    # Note that this function takes a whole vector x of data!
    return norm * np.exp(-(x-mean)**2/(2**2))
```

### Exercise 4b

```python
def mymodel(x, b, norm, mean, sigma):
    return x + b + gaus(x, norm, mean, sigma)
```

Remember to substitute ``mymodel`` for the gaussians above.

### Exercise 4c

```
b2 = a1 * c + b1 - a2 * c
```

So

```python
def line(x, a1, b1, a2, c):
    return np.where(x<c, a1 * x + b1, a2 * x +a1 * c + b1 - a2 * c)
```
