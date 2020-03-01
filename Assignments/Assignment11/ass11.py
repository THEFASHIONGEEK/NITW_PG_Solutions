import gym
import numpy as np
import random
from matplotlib import pyplot as plot
import pandas as pd
class MultiArmedBandit:
    def __init__(self, reward_probability_dist=[0.3, 0.5, 0.8]):

        self.reward_probability_dist = reward_probability_dist

    def step(self, action):

        if action > len(self.reward_probability_dist):
            raise Exception("MULTI ARMED BANDIT][ERROR] the action" + str(action) + " is out of range, total actions: " + str(len(self.reward_probability_dist)))
        p = self.reward_probability_dist[action]
        q = 1.0-p
        return np.random.choice(2, p=[q, p])
def create_bandit(reward_dist):
    if abs(sum(reward_dist )-1 ) > 0.1e-2:
        print("Adjust the reward distribution to sum to one..")
    env = MultiArmedBandit(reward_probability_dist=reward_distribution)
    num_arms= len(reward_distribution)
    return env,num_arms
tot_episodes=250
tot_steps =150
reward_distribution = [0.1,0.06,0.06,0.4,0.3,0.02,0.03,0.03]
env,tot_arms = create_bandit(reward_distribution)
tot_arms = len(reward_distribution)
print(tot_arms)
def perform_random_multiarm_bandit():
    average_value_function = np.zeros(tot_arms)
    cumulated_reward_list = list()
    for episode in range(tot_episodes):
        cumulated_reward = 0
        reward_counter_array = np.zeros(tot_arms)
        action_counter_array = np.full(tot_arms, 1.0e-5)
        for step in range(tot_steps):
            action = np.random.randint(low=0, high=tot_arms)
            reward = env.step(action)
            reward_counter_array[action] += reward
            action_counter_array[action] += 1
            cumulated_reward += reward
        cumulated_reward_list.append(cumulated_reward)
        value_function = np.true_divide(reward_counter_array, action_counter_array)
        average_value_function += value_function
    return average_value_function,cumulated_reward_list,action_counter_array
random_average_value_fn ,random_rewards,random_actions = perform_random_multiarm_bandit()
data = {"Average Reward":np.mean(random_rewards)}
result = pd.DataFrame(data,index=[0]) 
result.to_csv('output.csv', index=False)