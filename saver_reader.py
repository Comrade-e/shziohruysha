import random

def randomwords(amount: int, path: str):
    res = []
    with open(path, 'r', encoding='utf-8') as f:
        arr = [line.strip() for line in f]
    c = 0
    while c < amount:
        idx = random.randrange(len(arr) - 1)
        if arr[idx] != '':
            res.append(arr.pop(idx))
            c += 1
    del arr
    return res


def save(txt: str, path: str):
    with open(path, 'a', encoding='utf-8') as f:
        for el in txt.split(' '):
            s = el.strip(',-—')
            if len(s) > 0:
                f.write(s + '\n')


