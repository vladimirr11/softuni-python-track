import math

frt_int = int(input())
scd_int = int(input())
trd_int = int(input())
fth_int = int(input())

result = math.floor((frt_int + scd_int) / trd_int) * fth_int
print(int(result))