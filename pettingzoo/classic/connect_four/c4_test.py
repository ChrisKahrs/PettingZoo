from pettingzoo.classic import connect_four_v3
from pettingzoo.test import render_test
import random

env = connect_four_v3.env(render_mode="human")
# render_test(env)

def print_board(obs, agent):
    for i in range(6):
        for x in range(7):
            if obs["observation"][i][x][0] == 0 and obs["observation"][i][x][1] == 0:
                chip = "_"
            elif obs["observation"][i][x][0] == 0:
                chip ="R"
            else: chip = "B"
            # print(str(obs["observation"][i][x]), end=" ")
            print(chip, end=" ")
        print(" ")

env.reset()
for agent in env.agent_iter(100):
    env.render()
    obs, reward, done, done2, info = env.last()
    if done:
        print("mask ",str(obs["action_mask"]), " agent ", agent)
        print_board(obs, agent)
        print("done", done, "done2", done2, "info", info, "reward", reward)
        env.reset()
        break
    # print("mask ",str(obs["action_mask"]), " agent ", agent)
    # print_board(obs)
    action = random.randint(0,6) # get legal random action
    mask = obs["action_mask"]
    possible_actions = [i for i in range(len(mask)) if mask[i]==1]
    print("possible_actions", possible_actions)
    my_choice = random.randint(0,len(possible_actions)-1)
    print("my_choice", my_choice)
    env.step(possible_actions[my_choice]) # find which is the lowest legal action, or if anything wins?
# input("Press Enter to continue...")
env.close()


