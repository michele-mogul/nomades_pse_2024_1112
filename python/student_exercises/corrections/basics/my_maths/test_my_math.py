import my_maths
import time

start_r = time.time_ns()
fact = my_maths.factorial(990)
end_r = time.time_ns()

start_l = time.time_ns()
fact = my_maths.fact_for(990)
end_l = time.time_ns()

print(f"fact recursive took\t{(end_r-start_r)/10e6} ms")
print(f"fact for took\t\t{(end_l-start_l)/10e6} ms")