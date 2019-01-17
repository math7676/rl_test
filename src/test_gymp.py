# -*- coding: utf-8 -*-

import gym
env = gym.make('CarRacing-v0')
env.reset()
for _ in range(100):
    env.render()
    print(env.observation_space)
    s, r, done, info=env.step(env.action_space.sample()) # take a random action
    
    print (s,"state")
    print (r,"reward")
env.close()