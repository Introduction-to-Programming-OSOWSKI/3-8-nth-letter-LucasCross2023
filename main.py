def nthLetter(w, n):
    if len(w) < n:
        return False

    else:
        return w[n]

print(nthLetter("fortnite", 9))