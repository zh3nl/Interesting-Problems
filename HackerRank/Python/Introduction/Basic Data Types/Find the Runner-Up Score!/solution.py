def store_and_find(scores):
    sorted_scores = list(scores)
    sorted_scores.sort(reverse=True)
    highest = sorted_scores[0]
    for score in sorted_scores:
        if score < highest:
            print(score)
            break
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    store_and_find(arr)
