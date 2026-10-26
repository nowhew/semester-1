
# function implementation

def rectangle_area(w : float, h : float) -> float:
    return w * h

def even_numbers (n : int) -> list[int]:
    return [n for n in range(n) if n % 2 == 0]

def mean(l : list[int]) -> int:
    total = 0
    for e in l:
        total += e
    return total / len(l)

print(f"Area is {rectangle_area( )}")   # provide suitable data matching your inputs
