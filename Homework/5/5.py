# Требуется реализовать программу, которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

file = input('Enter file name: ')
with open(file) as f:
    words = f.read().split()
    big_len = len(max(words, key = len))
    big_words = [w for w in words if len(w)==big_len]
    print(big_words)
