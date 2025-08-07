from environment import Environment
from pprint import pprint
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import colors
import random
TERMINAL_POS = (4, 4)
HOLE_POS = [(1, 1), (1, 2), (2, 1), (2, 2)]
GAMMA = 0.9
NOISE = 0.2
GRID_SIZE = 5

env = Environment()
RT = env.rT
# Correct value initialization
vT = {pos: 0 for pos in RT}


# initilize the reward table with known rewards
for pos in RT:
    if pos == TERMINAL_POS:
        RT[pos] = 100
    elif pos in HOLE_POS:
        RT[pos] = -30
    else:
        RT[pos] = -1


threshold = 1
max_iterations = 1000

optimal_policy = {pos: None for pos in RT}


# Initialize a random policy
for pos in RT:
    if pos == TERMINAL_POS:
        optimal_policy[pos] = 'Goal'  # Terminal position
    else:
        actions = ['↓', '↑', '→', '←']
        optimal_policy[pos] = random.choice(actions)

        s_down = (pos[0] + 1, pos[1])
        s_up = (pos[0] - 1, pos[1])
        s_right = (pos[0], pos[1] + 1)        
        s_left = (pos[0], pos[1] - 1)

        action_list = [s_down, s_up, s_right, s_left]

        # If action leads to location outside grid, replaces the action with opposite action
        if optimal_policy[pos] == '←': 
            if not (0 <= s_left[0] < 5 and 0 <= s_left[1] < 5):
                optimal_policy[pos] = '→'
        elif optimal_policy[pos] == '→':
            if not (0 <= s_right[0] < 5 and 0 <= s_right[1] < 5):
                optimal_policy[pos] = '←'
        elif optimal_policy[pos] == '↑':
            if not (0 <= s_up[0] < 5 and 0 <= s_up[1] < 5):
                optimal_policy[pos] = '↓'
        elif optimal_policy[pos] == '↓':
            if not (0 <= s_down[0] < 5 and 0 <= s_down[1] < 5):
                optimal_policy[pos] = '↑'

pprint(optimal_policy)

# Policy evaluation
# Initialize value function for each state

finding_optimal_policy = True

policy_update_count = 0

while finding_optimal_policy:
    for iteration in range(max_iterations):
        delta = 0
        new_vT = vT.copy()
        new_vT[TERMINAL_POS] = RT[TERMINAL_POS]  # value of terminal state = reward of terminal state

        for pos in RT:
            if pos == TERMINAL_POS:
                optimal_policy[pos] = 'Goal'  # Terminal position
                # Skip terminal position as its value is fixed
            else:
                s_down = (pos[0] + 1, pos[1])
                s_up = (pos[0] - 1, pos[1])
                s_right = (pos[0], pos[1] + 1)        
                s_left = (pos[0], pos[1] - 1)

                action_list = [s_down, s_up, s_right, s_left]

                action_list_val = {}

                for action in action_list:

                    # If action leads to location outside grid, replaces the location with current position
                    if not (0 <= action[0] < 5 and 0 <= action[1] < 5):
                        idx = action_list.index(action)
                        action_list[idx] = pos
                
                num_rotations = len(action_list)
                rotations = [action_list[i:] + action_list[:i] for i in range(num_rotations)]
                
                # read the optimal policy direction
                if optimal_policy[pos] == '↓':
                    rotation = rotations[0]
                elif optimal_policy[pos] == '↑':
                    rotation = rotations[1]
                elif optimal_policy[pos] == '→':
                    rotation = rotations[2]
                elif optimal_policy[pos] == '←':
                    rotation = rotations[3]
                
                opt_prob = 1 - NOISE
                non_opt_prob = NOISE/3
                # The first action in the rotation is considered the optimal action

                action_list_val[rotation[0]] = opt_prob*(RT[pos] + GAMMA*vT[rotation[0]]) + sum(
                    non_opt_prob*(RT[pos] + GAMMA*vT[a]) for a in rotation[1:])

                # Find the action with the maximum value
                best_action = max(action_list_val, key=action_list_val.get)


                best_action_value = action_list_val[best_action]
                new_vT[pos] = best_action_value
                
                delta = max(delta, abs(new_vT[pos] - vT[pos]))

        vT = new_vT
        

        print(f"Iteration {iteration}, max delta: {delta}")
        if delta < threshold:
            print("Converged!")
            break
    
    new_optimal_policy = optimal_policy.copy()

    # Deriving a new policy based on the value function, using 1 step lookahead
    for pos in RT:
        if pos == TERMINAL_POS:
            new_optimal_policy[pos] = 'Goal'  # Terminal position
        else:
            s_down = (pos[0] + 1, pos[1])
            s_up = (pos[0] - 1, pos[1])
            s_right = (pos[0], pos[1] + 1)        
            s_left = (pos[0], pos[1] - 1)

            action_list = [s_down, s_up, s_right, s_left]

            action_list_val = {}

            action_list = [action for action in action_list if 0 <= action[0] < 5 and 0 <= action[1] < 5]

            
            # If no valid actions left, set the action to the current position
            if not action_list:
                action_list = [pos]
            
            # Look up value of each possible action and choose the maximum value action
            for action in action_list:
                action_list_val[action] = vT[action]
            
            # Find the action with the maximum value
            best_action = max(action_list_val, key=action_list_val.get)
            
            # Determine policy direction, derived from the best action.
            if best_action == s_up:
                new_optimal_policy[pos] = '↑'
            elif best_action == s_down:
                new_optimal_policy[pos] = '↓'
            elif best_action == s_left:
                new_optimal_policy[pos] = '←'
            elif best_action == s_right:
                new_optimal_policy[pos] = '→'
    
    if new_optimal_policy == optimal_policy:
        print("Optimal policy found!")
        finding_optimal_policy = False
    else:
        policy_update_count += 1
        print(f"Policy update count: {policy_update_count}")
        optimal_policy = new_optimal_policy

### SECTION FOR PLOTTING ----------------------------------------- ###

# Prepare data for heatmap
value_grid = np.array([[vT[(i, j)] for j in range(GRID_SIZE)] for i in range(GRID_SIZE)])
policy_grid = np.array([[optimal_policy.get((i, j), '') for j in range(GRID_SIZE)] for i in range(GRID_SIZE)])

# Enhanced contrast using percentiles
vmin = np.percentile(value_grid, 0)
vmax = np.percentile(value_grid, 100)
norm = colors.Normalize(vmin=vmin, vmax=vmax)

# Plot heatmap
fig, ax = plt.subplots(figsize=(8, 8))
cmap = plt.cm.coolwarm  # Try other colormaps too
heatmap = ax.imshow(value_grid, cmap=cmap, norm=norm)

# Annotate with policy directions
for j in range(GRID_SIZE):
    for i in range(GRID_SIZE):
        ax.text(j, i, policy_grid[i][j], ha='center', va='center', color='white', fontsize=14)

plt.colorbar(heatmap)
ax.set_xticks(np.arange(GRID_SIZE))
ax.set_yticks(np.arange(GRID_SIZE))
ax.set_xticklabels(np.arange(GRID_SIZE))
ax.set_yticklabels(np.arange(GRID_SIZE))
ax.set_title("Value Function Heatmap with Policy Directions")
plt.tight_layout()
plt.show()

