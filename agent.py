#building the agent of the game

#imps
import random
import numpy as np
import tensorflow as tf
from collections import deque

class agent():
    def __init__(self,sym):
        self.number = sym
        self.learning_rate = 0.01
        self.gamma = 0.95
        self.batch_size = 30
        self.memory = deque()
        self.exploration = 0.5
        
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Input((1,9)))
        self.model.add(tf.keras.layers.Dense(10,activation="relu"))
        self.model.add(tf.keras.layers.Dense(30,activation="relu"))
        self.model.add(tf.keras.layers.Dense(30,activation="relu"))
        self.model.add(tf.keras.layers.Dense(10,activation="relu"))
        self.model.add(tf.keras.layers.Dense(9))
        self.model.compile(loss="mse",optimizer=tf.keras.optimizers.Adam(self.learning_rate))

    def symbol(self):
        return self.number

    def storage(self,state,action,reward,next_state,done):
        state = np.reshape(state,(1,1,9))
        next_state = np.reshape(next_state,(1,1,9))
        self.memory.append((state,action,reward,next_state,done))

    def act(self,state,action_space):
        if np.random.uniform(0,1)>(1 - self.exploration):
            return np.random.choice(action_space)
        state = np.reshape(state,(1,1,9))
        actions_before_mask = self.model.predict(state)[0]
        mask = np.zeros((1,9))[0]
        for i in action_space:
            mask[i] = 1
        actions_after_mask = actions_before_mask[0]*mask
        action = np.argmax(actions_after_mask)
        return action

    def rewind_memory(self):
        if len(self.memory)<self.batch_size:
            return
        batch = random.sample(self.memory,self.batch_size)
        for state,action,reward,next_state,done in batch:
            update = reward + self.gamma*(np.amax(self.model.predict(next_state)[0]))
            q_value = self.model.predict(state)
            q_value[0][0][action] = update
            self.model.fit(state,q_value,verbose=0)
            


