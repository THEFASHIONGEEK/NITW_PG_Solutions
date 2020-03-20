# Smartcab
Smart cab navigating through it using Q-learning algorithm.

Problem Statement: A self-drivingcab company Smartcabwanted to design a simulation of a self-driving cab

Goal: Demonstrate theuse of RL techniques to develop an efficient and safe approach for tackling the issue.

Project Description:The Smartcab's job is to pick up the passenger at one location and drop them off in another. Here isa list of things that theywouldlove our Smartcab to take care of:

1.Drop off the passenger to the right location.

2.Save passenger's time by taking minimum time possible to drop off.

3.Take care of passenger's safety and traffic rules

There are different aspects that need to be considered here while modeling an RL solution to this problem: rewards, states, and actions.

Company also wanted to allow users to book a cab by sending a free text SMS containing source, destination and time of travel. Since SMS is a free text, different users can send same message in different ways,e.g.,

1.I want to book a cab from cyber city to sector 48 at 5 pm.

2.Please book my cab with pick up from cyber city, destination sector 48, and time of pick up 5 pm.

3.Book a cab for me from sector 48, my pick-up is from cyber city at 5 pm.So, the challenge for the company is to parse this free text and fetch three entities:

●Pick up location

●Destination

●Time to pick up

## Process Flow/Overall solution:

Solve Open AI Gym environment “Taxi v2” using Q learning algorithm to learn a task of pickup, drop passengers and then evaluate the learned environment on the given data:

sms.txt:This file contains 1000 text messages containing information of pickup location, drop location, and time of pickupTask to be solved:

### Train:

1.Train a model using Q learning algorithm on tax v2 environment.

### Evaluation:

1.Take text from "sms.txt" and fetch pickup and drop from it.

2.Generate the random state from an environment and change the pick-up and drop as the fetched one from sms.txt.

3.Evaluate you model performance on all the texts given in sms.txt. We have generated text for four locations given in city.csv.

4.Have a check if the fetched pickup, drop is not matching with original pickup, drop given in “orig_df.csv”.

5.If fetched pickup or/and drop does not match with the original, add penalty and reward -10.

6.Calculate the Total reward, penalties, Wrong pickup/drop predicted and Average time steps per episode.

## Dataset Description

1)sms.txt: Contains 1000 texts in natural language containing pickup, drop, and time information

Example:

1.Please book a cab from airport to hauz khaas at 3 PM

2.airport to hauz khaas at 6 PM

3.Kindly book a cab for me at 1 PM from hauz khaas to dwarka sector 23

4.airport to hauz khaas at 1 AM

5.I want to go to dwarka sector 21 from airport leaving at 10 PM

6.airport to dwarka sector 21 at 12 PM

2)city.csv: Contains 4 locations and mappings

3)orig_df.csv: Contains correct pickup, drop fetched from sms.txt
