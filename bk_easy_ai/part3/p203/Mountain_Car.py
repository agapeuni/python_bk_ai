# 카트를 밀어 깃발까지 올리자!

import gym
import numpy as np

env = gym.make("MountainCar-v0")
LEARNING_RATE = 0.1   # 학습률
DISCOUNT = 0.95       # 할인률
EPISODES = 2400       # 시도 횟수
SHOW_EVERY = 300      # 단계별 스텝 수, 2400을 300번마다 보여줌(총 8단계).

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)        # 정규화
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE
# 랜덤하게 탐색하는 단계
# Exploration settings(탐색 설정)
epsilon = 1 
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES//2
epsilon_decay_value = epsilon/(END_EPSILON_DECAYING - START_EPSILON_DECAYING)

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    return tuple(discrete_state.astype(np.int))  
# Q테이블 상의 3가지 action 중 하나를 선택하기 위해 tuple 형태의 상태를 return함.

for episode in range(EPISODES):
    discrete_state = get_discrete_state(env.reset())
    done = False
    if episode % SHOW_EVERY == 0:
        render = True
        print(episode)
    else:
        render = False

    while not done:
        if np.random.rand() > epsilon:
            # Get action from Q table
            # action: 0은 왼쪽으로 밀기, 1은 정지, 2는 오른쪽으로 밀기
            action = np.argmax(q_table[discrete_state])
        else:
            # 랜덤하게 action을 취함.
            action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        if episode % SHOW_EVERY == 0:
            env.render()
        # new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        # 위의 수식을 이용하여 Q table을 업데이트해 가며 최종 목표에 다다를 때까지 학습하기
        if not done:
            # 다음 스텝의 최대 Q값
            max_future_q = np.max(q_table[new_discrete_state])
            # 현재 Q값
            current_q = q_table[discrete_state + (action,)]
            # Q학습 공식
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            # 새로운 Q값으로 Q table을 업데이트
            q_table[discrete_state + (action,)] = new_q
        # 목표 지점에 다다르면 시뮬레이션 종료(Q테이블 = 0)
        elif new_state[0] >= env.goal_position:
            #q_table[discrete_state + (action,)] = reward
            q_table[discrete_state + (action,)] = 0
        discrete_state = new_discrete_state
    # 탐색(episode)할 때마다 episode 번호가 시작과 끝 사이라면, epsilon 값을 발산 방지를 위해 감쇄시킴.
    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value
env.close()