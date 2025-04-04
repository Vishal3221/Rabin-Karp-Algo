def rabin_karp(text, pattern, prime=101):
    m = len(pattern)
    n = len(text)
    d = 256  # Number of characters in the input alphabet
    h = pow(d, m-1, prime)
    p = 0  # hash value for pattern
    t = 0  # hash value for text

    # Preprocessing: calculate hash value of pattern and first window
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime

text = "WELCOME TO RIT"
pattern = "RIT"
rabin_karp(text, pattern)
