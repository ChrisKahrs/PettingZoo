from pettingzoo.classic import connect_four_v3
from pettingzoo.test import render_test
import random

env = connect_four_v3.env(render_mode="human")
# render_test(env)

def print_board(obs):
    for i in range(6):
        for x in range(7):
            print(str(obs["observation"][i][x]), end=" ")
        print(" ")

env.reset()
for agent in env.agent_iter(100):
    env.render()
    obs, reward, done, done2, info = env.last()
    if done:
        print_board(obs)
        print("done", done, "done2", done2, "info", info, "reward", reward, "agent", agent)
        env.reset()
        break
    print("mask ",str(obs["action_mask"]), " agent ", agent)
    print_board(obs)
    action = random.randint(0,6)
    env.step(action)
input("Press Enter to continue...")
env.close()


