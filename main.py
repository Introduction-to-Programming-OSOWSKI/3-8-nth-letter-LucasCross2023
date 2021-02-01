def nthLetter(w, n):
    if len(w) < n:
        return False

    else:
        return w[n-1]

print(nthLetter("qwertyuiop", 5))