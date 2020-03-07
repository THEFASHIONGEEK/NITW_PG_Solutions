import numpy as np
import pandas as pd
import random
import math
dataset = pd.read_csv("training-image_survey/image_survey.csv")
def return_ubc_action(num_arms,num_selections,rewards_array):
    max_upper_bound = 0
    for i in range(0,num_arms):
        if (num_selections[i] > 0):
            average_reward = rewards_array[i]/num_selections[i]
            delta_i = math.sqrt(3/2 * math.log(num_arms+1)/num_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e4000
        
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            action =i
    return action
def choose_by_ubc(dataset):
    num_episodes = dataset.shape[0]
    num_ads      = dataset.shape[1]
    ads_selected  =[]
    num_ad_selected = np.zeros(num_ads)
    
    total_reward = 0
    rewards      = np.zeros(num_episodes)
    avg_rewards  = np.zeros(num_ads)
    num_ad_rewards = np.zeros(num_ads)
    
    sum_ad_rewards = np.zeros(num_ads)
    last_100_rewards = np.zeros(num_episodes)
    ads_selection = np.zeros((num_ads, num_episodes))
    
    for n in range(0,num_episodes):
        ad = return_ubc_action(num_ads,num_ad_selected,sum_ad_rewards)
        
        # Update the ad tracking vars        
        ads_selected.append(ad)
        num_ad_selected[ad] = num_ad_selected[ad] + 1
        reward = dataset.values[n, ad]
        rewards[n] = reward

       
        
        sum_ad_rewards[ad] = sum_ad_rewards[ad] + reward
        avg_rewards[ad] = num_ad_rewards[ad] / num_ad_selected[ad]
        total_reward = total_reward + reward


        # Update the Running average
        if n > 100:
            last_100_rewards[n] = rewards[np.arange(n-99,n+1)].mean()
            
            # Update the add selection for each ad
        if n > 0:
            for i in range(0, num_ads):
                ads_selection[i][n] = ads_selection[i][n-1]
            ads_selection[ad][n] = ads_selection[ad][n-1] + 1
            
    return ads_selected, last_100_rewards, ads_selection,total_reward
ads_selected, last_100_rewards, ads_selection,total_reward = choose_by_ubc(dataset)
data = {"Total Reward":total_reward}
result = pd.DataFrame(data,index=[0])
result.to_csv('output.csv', index=False)