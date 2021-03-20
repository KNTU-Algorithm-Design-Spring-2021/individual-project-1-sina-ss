n = int(input('Enter n: '))
x, y  = list(map(int, input().strip().split(' ')))
max_x, min_x = x, x
max_y, min_y = y, y
for i in range(n-1):
    x, y  = list(map(int, input().strip().split(' ')))
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)
print("Rectangular vertices: ("+ str(max_x) + ", "+ str(max_y)+ "), ("+ str(max_x) + ", "+ str(min_y)+ "), ("+ 
    str(min_x) + ", "+ str(max_y)+ "), ("+ str(min_x) + ", "+ str(min_y)+ ")")