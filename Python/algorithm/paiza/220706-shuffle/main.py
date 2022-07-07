def shuffle(shuffle_list, M):
    new_list = [shuffle_list[i:i+M] for i in range(0, len(shuffle_list), M)]
    return reversed(new_list)


def restore(restore_lists, M, N):
    new_list = [(restore_lists[int((N-1)/M)-int(i/M)][-((i) % M)-1]) for i in range(N)]
    return list(reversed(new_list))


N, M, K = map(int, input().split(' '))

cards = list(range(1, N + 1))

for i in range(K):
    cards = list(shuffle(cards, M))
    cards = restore(cards, M, N)

print('\n'.join(map(str, cards)))
