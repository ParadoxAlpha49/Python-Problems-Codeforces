n = int(input())

for _ in range(n):
    word = input().strip()
    if len(word) > 10:
        transformed_word = f"{word[0]}{len(word) - 2}{word[-1]}"
    else:
        transformed_word = word
    print(transformed_word)