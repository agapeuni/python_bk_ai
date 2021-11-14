import numpy as np

N = 100          # 지원자의 수
n_exam = 1000    # 시뮬레이션 회수
max_eval = 100   # 평가 점수 최대치

# 채용한 사람의 평가 점수의 이력, 채용하지 않은 경우는 0
history = []

np.random.seed(1)

# 최대, 최소 정규화 처리를 하여, 임의의 지원자 샘플을 만드는 함수
def make_application_sample(N, max_eval):
    sample = np.random.normal(10, 10, N)
    min_sample = np.min(sample)
    max_sample = np.max(sample)
    normalized = (sample - min_sample)/(max_sample - min_sample) * max_eval
    return normalized

def parse_secretary_problem(N, max_eval, verbose=False):
    sample = make_application_sample(N, max_eval)  # 임의의 지원자 샘플을 만듦.
    # 맨 앞부터 N/e명을 무조건 패스하고, 벤치마킹용 평가 점수(잠정적 후보자의 점수)를 만듦.
    pos_bench = np.int(N/np.e)
    score_bench = np.max(sample[0:pos_bench])
    if verbose:
        print("패스할 인원수: {}".format(pos_bench))
        print("벤치마크 점수:{}".format(score_bench))
    result = 0
    for _score in sample[pos_bench:]:
        # 지원자의 면접 점수가 벤치마크 점수를 넘었는지?
        if _score >= score_bench:
            # 벤치마크 점수를 넘으면 곧바로 채용하고, 프로세스를 종료함.
            result = _score
            break
    return result

for i in range(10): # 10번의 테스트를 해서 결과를 확인
    print("최종합격자 점수: {}".format(parse_secretary_problem(N, max_eval, verbose=True)))
    print("=" * 50)