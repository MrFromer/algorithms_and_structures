import sys
import math

def main():
    input = sys.stdin.read().split()
    ptr = 0
    W = int(input[ptr])
    ptr += 1
    H = int(input[ptr])
    ptr += 1
    N = int(input[ptr])
    ptr += 1
    
    results = []
    for _ in range(N):
        xi = float(input[ptr])
        ptr += 1
        yi = float(input[ptr])
        ptr += 1
        
        x_start = math.floor(xi)
        x_end = math.ceil(xi)
        sx = x_end - x_start
        
        y_start = math.floor(yi)
        y_end = math.ceil(yi)
        sy = y_end - y_start
        
        s = min(sx, sy)
        results.append(s)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()