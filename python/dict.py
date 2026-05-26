def histogram(s):
    d=dict()
    for c in s:
        d[c]=d.get(c,0)
        d[c] +=1
    del(d[" "])
    return d


if __name__== "__main__":
    s = "this is africa"
    print(histogram(s))
    output= histogram(s)
    for k,v in sorted(output.items()):
        print(k,v)