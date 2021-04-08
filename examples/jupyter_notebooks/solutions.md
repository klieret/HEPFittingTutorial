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

### Exercise 6a

Just replace the name of the `"normfactor"` modifier for the seconds sample by
`mu1`. Then this will become a single parameter, correlated for both samples. So
`pyhf.infer.mle.fit(data, model)` will also only return one parameter, so
instead of

```python
mu1, mu2 = pyhf.infer.mle.fit(data, model)
```

you have to write

```python
mu1 = pyhf.infer.mle.fit(data, model)
```

For plotting the fitted histograms you have to replace `mu1 * hist1, mu2 *
hist2` by `mu1 * hist1, mu1 * hist2` since both histograms are scaled by the
same normfactor now.

### Questions 6b

The fit parameters are correlated because both parameters affect the bin content
for the same data points. The correlation coefficient is negative because if
there is a tendency for one normalization factor to be higher, then the other
one tends to be lower to still fit the data.

Both normalization factors have an uncertainty - which means if we were to
repeat the fit with new data (that is independent, identically distributed) we
would get a distribution of fit parameters. However, both fit parameters would
not be independent random variables, but correlated to some degree (the 1 sigma
contour in a 2D scatter plot would be an Ellipse rather than a circle).

### Question 6c

If every bin would have an independent normalization factor then we would get a
perfect fit to data. The uncertainty for each bin would be the square root of
the expected bin content, matching the poisson interval error bars we draw for
the data (in case we chose the symmetrical ones).

### Exercise 6d

One possible solution:

```python
m2_samples = [
    {
        "name": f"sample{i}",
        # set all bin contents to 0 except for the one this sample is for
        "data": [0 if i_bin != i else (hist1 + hist2)[i] for i_bin in range(10)],
        "modifiers": [
            {"name": f"mu{i}", "type": "normfactor", "data" : None}
        ],
    }
    for i in range(10)
]
m2_spec = {"channels" : [{"name" : "singlechannel", "samples" :  m2_samples}]}
m2 = pyhf.Model(m2_spec, poi_name=None)

# 10 parameters
p2 = pyhf.infer.mle.fit(data, m2, return_uncertainties=True)

hep.histplot((hist1 + hist2) * p2[:, 0], bins, stack=True, histtype="fill")
hep.histplot(data, bins, histtype="errorbar", color="black", yerr=np.sqrt(data))
errorband(bins, (hist1 + hist2) * p2[:, 0], (hist1 + hist2) * p2[:, 1])
```

### Exercise 6e

We can't get a perfect fit since we need to fit the real ("actual") data and
auxiliary data simultaneously. When tuning the individual bin contents to fit
the real data better we might get larger disagreement describing the auxiliary
data.

### Exercise 7a

We want to exclude the background only hypothesis, so we test for $\mu=0$.

### Exercise 7b

Either just modify the value of `s` and try out when the significance crosses 3
sigma or do a systematic scan like the following:

```
for i in range(7, 20, 1):
    p = pyhf.infer.hypotest(
        poi_test=0,
        data=[i + b] + model.config.auxdata,
        pdf=model,
        test_stat="q0"
    )
    print(i, pvalue_to_significance(p))
```

You will see the boundary is at 14 excess events. For 13 we get something in the
order of `2.977`, for 14 we get around `3.147`.

### Question 7c

The signal would not count as excluded since we usually choose `CLs<0.05` as
criterion for exclusion.
