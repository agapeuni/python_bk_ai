# 해적의 수가 1명부터 50명까지 일때, 금화가 10개 있을 경우, 몇 명의 해적이 어떻게 나누어 갖는지 살펴보자. 
# 사람은 많고 금화는 적은 경우는, 많은 해적이 살해됨을 알 수 있다. 
# 해적이 50명일 경우, 아무리 노력해도 14명은 살해되어야 금화를 나누어 가질 수 있다. 
# 금화가 10개 이상인 경우는 G로 표시함.

import sys

def main(num_pirates, coin):

    def solve(proposal):
        necessary_vote = len(proposal) // 2
        ranks = sorted((n, i) for i, n in enumerate(proposal))
        necessary_coin = sum(n + 1 for n, _ in ranks[:necessary_vote])
        if coin >= necessary_coin:
            return [(n + 1 if ranks.index((n, i)) < necessary_vote else 0)
                    for i, n in enumerate(proposal)] + [coin - necessary_coin]
        return proposal + [-1]

    def pretty(x):
        if x == -1:
            return 'x'
        if x > 9:
            return 'G'
        return str(x)

    optimal_proposal = []

    for member in range(num_pirates):
        optimal_proposal = solve(optimal_proposal)
        print('{:4}: {}'.format(member + 1,
                                ''.join(pretty(x) for x in optimal_proposal)))

if __name__ == '__main__':
    main(int(50), int(10))  # 해적 50명에 금화는 10개