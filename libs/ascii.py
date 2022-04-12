class ascii:
    def rotate(s: str, steps: int) -> str:
        return ''.join([s[-steps:len(s)], s[:-steps]])
        
    def swap(s: str, indices: tuple) -> str:
        if len(indices) != 2: return s
        (i, j) = indices
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return ''.join(s)