# -*- coding: utf-8 -*-
# July 2020 Emily Alfs-Votipka
# CC315 Module 1 Strings VS Character Arrays
# ```tex
# 1. function APPENDER(NUMBER, BASE)
# 2.     RESULT = ""
# 3.     loop I from 1 to NUMBER
# 4.         RESULT = RESULT + BASE
# 5.         if I MOD 2 = 0
# 6.             RESULT = RESULT + " "
# 7.         else
# 8.             RESULT = RESULT + ", " 
# 9.     end loop
# 10.    return RESULT
# 11. end function
# ```

# ```tex
# 1. function APPENDER_LIST(NUMBER, BASE)
# 2.     RESULT = []
# 3.     loop I from 1 to NUMBER
# 4.         RESULT.APPEND(BASE) 
# 5.         if I MOD 2 = 0
# 6.             RESULT.APPEND(" ") 
# 7.         else
# 8.             RESULT.APPEND(", ")  
# 9.     end loop
# 10.    RESULT = "".JOIN(RESULT)
# 11.    return RESULT
# 12. end function
# ```

def appender(num, base):
    result = ""
    for i in range(num):
        result = result + base
        if i%2 == 0:
            result = result + " "
        else: 
            result = result + ", "
    return result

def appender_list(num, base):
    result = []
    for i in range(num):
        result.append(base)
        if i%2 == 0:
            result.append(" ")
        else: 
            result.append(", ")
    result = "".join(result)
    return result 

for i in range(10):
    n = 10**i
    get_ipython().run_line_magic('timeit', "appender(n, 'abc')")


# 10^0: 382 ns ± 7.22 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each) <br>
# 10^1: 1.57 µs ± 17.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each) <br>
# 10^2: 14.6 µs ± 79.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each) <br>
# 10^3: 201 µs ± 4.51 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each) <br>
# 10^4: 2.02 ms ± 33.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) <br>
# 10^5: 21.3 ms ± 376 µs per loop (mean ± std. dev. of 7 runs, 10 loops each) <br>
# 10^6: 217 ms ± 6.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) <br>
# 10^7: 2.58 s ± 40.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) <br>
# 10^8: 26.7 s ± 357 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) <br>
# 10^9: 4min 32s ± 2.34 s per loop (mean ± std. dev. of 7 runs, 1 loop each) <br>

get_ipython().run_line_magic('load_ext', 'memory_profiler')
for i in range(10):
    n = 10**i
    get_ipython().run_line_magic('memit', "appender(n, 'abc')")

# 10^0: peak memory: 558.39 MiB, increment: 0.00 MiB <br>
# 10^1: peak memory: 558.39 MiB, increment: 0.00 MiB<br>
# 10^2: peak memory: 558.39 MiB, increment: 0.00 MiB<br>
# 10^3: peak memory: 558.39 MiB, increment: 0.00 MiB<br>
# 10^4: peak memory: 558.44 MiB, increment: 0.05 MiB<br>
# 10^5: peak memory: 558.44 MiB, increment: 0.00 MiB<br>
# 10^6: peak memory: 558.45 MiB, increment: 0.01 MiB<br>
# 10^7: peak memory: 598.38 MiB, increment: 39.93 MiB<br>
# 10^8: peak memory: 831.44 MiB, increment: 267.20 MiB<br>
# 10^9: peak memory: 3195.28 MiB, increment: 2631.05 MiB<br>

for i in range(10):
    n = 10**i
    get_ipython().run_line_magic('timeit', "appender_list(n, 'abc')")

# 10^0: 475 ns ± 10.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each) <br>
# 10^1: 1.9 µs ± 22.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each) <br>
# 10^2: 15.5 µs ± 61.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)<br>
# 10^3: 151 µs ± 1.65 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)<br>
# 10^4: 1.48 ms ± 19 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)<br>
# 10^5: 14.6 ms ± 37.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)<br>
# 10^6: 152 ms ± 817 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)<br>
# 10^7: 1.52 s ± 16.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)<br>
# 10^8: 15.4 s ± 87.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)<br>
# 10^9: 2min 35s ± 569 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)<br>

get_ipython().run_line_magic('load_ext', 'memory_profiler')
for i in range(10):
    n = 10**i
    get_ipython().run_line_magic('memit', "appender_list(n, 'abc')")

# 10^0: peak memory: 47.27 MiB, increment: 0.06 MiB <br>
# 10^1: peak memory: 47.29 MiB, increment: 0.02 MiB<br>
# 10^2: peak memory: 47.30 MiB, increment: 0.00 MiB<br>
# 10^3: peak memory: 47.34 MiB, increment: 0.04 MiB<br>
# 10^4: peak memory: 47.57 MiB, increment: 0.24 MiB<br>
# 10^5: peak memory: 51.92 MiB, increment: 4.35 MiB<br>
# 10^6: peak memory: 87.66 MiB, increment: 35.74 MiB<br>
# 10^7: peak memory: 276.24 MiB, increment: 202.88 MiB<br>
# 10^8: peak memory: 2078.77 MiB, increment: 1955.12 MiB<br>
# 10^9: peak memory: 20108.69 MiB, increment: 19555.79 MiB<br>

import matplotlib.pyplot as plt
x = [i for i in range(1,11)]
x_lab = ['10^'+str(i) for i in range(10)]
time_str = [3.82e-7,1.57e-6,1.46e-5,0.000201,0.00202,0.0213,0.217,2.58,26.7,272]
time_arr = [0.000000475,0.0000019,0.0000155,0.000151,0.00148,0.0146,0.152,1.52,15.4,155]
e_time_str = [7.22e-9,1.74e-8,7.98e-8,4.51e-6,3.35e-5,0.000376,0.0062,0.0405,0.357,2.34]
e_time_arr = [0.0000000105,0.0000000222,0.0000000611,0.00000165,0.000019,0.0000372,0.000817,0.0169,0.0879,0.569]
mib_mem_str = [558.39,558.39,558.39,558.39,558.44,558.44,558.45,598.38,831.44,3195.28]
p_mem_str = [i*1.049 for i in mib_mem_str]
mib_mem_arr = [47.27,47.29,27.30,47.34,47.57,51.92,87.66,276.24,2078.77,20108.69]
p_mem_arr = [i*1.049 for i in mib_mem_arr]
mem_label = 'Memory in MB'
time_label = 'Time in seconds'

# line 1 points
x1 = x
y1 = time_str
err1 = e_time_str
# plotting the line 1 points 
plt.errorbar(x1, y1, yerr=err1, label = "Python: Strings")
# line 2 points
x2 = x
y2 = time_arr
err2 = e_time_arr
# plotting the line 2 points 
plt.errorbar(x2, y2, yerr=err2, label = "Python: Array")
plt.xlabel('Number of iterations')
# Set the y axis label of the current axis.
plt.ylabel(time_label)
# Set a title of the current axes.
plt.title('Python Time Comparison')
# show a legend on the plot
plt.xticks(x,x_lab,rotation=45)
plt.legend()
# Display a figure.
plt.savefig("315_stringsTime_python.png")
plt.show()


# line 1 points
x1 = x
y1 = p_mem_str
# plotting the line 1 points 
plt.xticks(x,x_lab,rotation=45)
plt.errorbar(x1, y1, label = "Python: Strings")
# line 2 points
x2 = x
y2 = p_mem_arr
# plotting the line 2 points 
plt.errorbar(x2, y2, label = "Python: Array")
plt.xlabel('Number of iterations')
# Set the y axis label of the current axis.
plt.ylabel(mem_label)
# Set a title of the current axes.
plt.title('Python Memory Comparison')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.savefig("315_stringsMem_python.png")
plt.show()
