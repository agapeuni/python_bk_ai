# 5인의 해적과 100개의 금화 문제
# 100개의 금화를 5인의 해적이 분배
# 순위를 정하여 1번째 해적이 분배하고, 투표하여 반 이상이 만족하면 OK, 그렇지 않으면 1번째 해적은 살해당함.
# 1번째 해적이 살해당하면 2번째 해적이 같은 방식으로 진행
# 가장 많은 금화를 얻기 위한 방법은? 그때 얻을 수 있는 금화의 개수는?
# (힌트)역순으로(1명의 해적만 남은 경우, 2명의 해적...) 계산해 가야 한다. 
# 해적수가 5명 이상일 경우는 계산 시간이 급격히 증가함을 확인 바람. 

import sys

def generate_proposal(member, coin):
    if member == 0:
        yield [coin]
    else:
        for i in range(coin, -1, -1):
            for proposal in generate_proposal(member - 1, coin - i):
                yield [i] + proposal

def main(num_pirates, coin):

    optimal_proposal = []

    for member in range(num_pirates):
        best_coin = -1
        best_proposal = None
        optimal_proposal.append(-1)
        for proposal in generate_proposal(member, coin):
            vote = sum(1 for i in range(member + 1) if proposal[i] > optimal_proposal[i])
            if vote * 2 >= (member + 1) and proposal[-1] > best_coin:
                best_coin = proposal[-1]
                best_proposal = proposal

        if best_proposal:
            optimal_proposal = best_proposal

        print(member + 1, optimal_proposal)

if __name__ == '__main__':
    main(int(5), int(100))    # 해적 5명, 금화 100개인 경우