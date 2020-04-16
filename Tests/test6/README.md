# Test6

<a id="1"></a>
## MCQS

#### 1.Which of the following algorithm places an importance on preferences of actions leading to rewards?
- Upper Confidence Bound Selection
- **Gradient Bandits**
- Epsilon Greedy Selection
- Contextual Bandits 


#### 2.Assume that we need the Agent to learn the uncertainties in an environment , commit less errors and maximize the rewards. Which of the following options is the correct choice for such situations?
- Value Iteration Method
- Monte Carlo Method
- Policy Iteration Method
- **Temporal Difference Learning Method**

#### 3.Smart-Pets is a startup that facilitates the owners of pets like cats and dogs to interact with the animals online before adopting them. They use a sophisticated IT infrastructure that enhances the interaction. As of now, they have 15 cats and 7 dogs available for adoption. They have a user base of 125 customers. However, the number of combinations are  huge. They would like to design a solution that will minimize the number of interactions for users so that the entire process doesn’t become cumbersome. Which Algorithm would be the best for such a situation? 

- Deep Q Learning 
- Temporal Difference Learning
- Monte Carlo Learning Approach
- **Dynamic Programming**

#### 4.Breach Candy hospital has launched a program to help the new doctors (having less than 5 years of practicing experience) provide more accurate healthcare services. For this, they have made an application that suggests the appropriate treatment plans for their patients based on historical data. They believe Monte Carlo methods are the right solution for this situation. Do you agree? What are your reasons? Choose the right option from the ones given below
- Yes. Monte Carlo methods simulate a variety of combinations and hence cover a lot of variance which will give most accurate results.
- **No. Contextual Bandits will be the best solution as treatment plans differ from patient to patient.**
- Partially Agree. Monte Carlo must be combined with Value Iteration to find the best possible solution.
- No. Dynamic Programming will give the most accurate results.

#### 5.If there is a complex reward function and a combination of Algorithms (Both Model - Based and Model -  Free) and still the learning is not converging then what could be the most likely solution?
- Add more training data 
- It is a problem of sparse rewards and so reward shaping will resolve this issue
- Bootstrapping via Temporal Difference methods should be implemented 
- **Check the quality of training data, set a benchmark and stop the training if the Agent is not learning anything new **

#### 6. Can the entire environment be modeled before an Agent starts exploring? If yes, which Algorithm does this?
- No, only the next state – action pair can be estimated
- Yes, Monte Carlo &  SARSA 
- **Yes, Monte Carlo & Q - Learning**
- Yes, Monte Carlo

#### 7. In a Game with a grid size of 84 X 84 with close to 7 million possible states, if we want the Agent to learn the best policy through exploration, which of the algorithm listed below will be the best one to go ahead with?
- Policy Gradient Using REINFORCE
- **Q - Learning**
- Value Iteration
- Policy Iteration

#### 8.John and Tina are a couple. Due to their job requirements, they work at different places for 6 months. Both stay worried about what the other had for lunch / dinner as John lives in Jakarta and he hates sea food whereas Tina lives in Hong Kong and hates Chinese food. They communicate over the phone daily but never reveal the truth about what they had for lunch / dinner. However, based on their mood, they can estimate whether the other liked the food they had or not. Below is a snapshot of their situation for a simpler understanding.You are supposed to suggest which method is best suited to help John and Tina estimate with maximum precision what food the other had on any given day.
- Upper Confidence Bound Selection
- Policy Gradients
- Bellman Equations
- **Markov Chains**



