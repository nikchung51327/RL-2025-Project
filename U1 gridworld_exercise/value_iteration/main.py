from environment import Environment
from pprint import pprint
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import colors

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


threshold = 1e-4
max_iterations = 1000

optimal_policy = {pos: None for pos in RT}

# Storing delta values for visualization
delta_values = {}

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
            
            for rotation in rotations:
            
                opt_prob = 1 - NOISE
                non_opt_prob = NOISE/3
                # The first action in the rotation is considered the optimal action

                action_list_val[rotation[0]] = opt_prob*(RT[pos] + GAMMA*vT[rotation[0]]) + sum(
                    non_opt_prob*(RT[pos] + GAMMA*vT[a]) for a in rotation[1:])

            # Find the action with the maximum value
            best_action = max(action_list_val, key=action_list_val.get)

            
            # Determine policy direction, derived from the best action.
            if best_action == s_up:
                optimal_policy[pos] = '↑'
            elif best_action == s_down:
                optimal_policy[pos] = '↓'
            elif best_action == s_left:
                optimal_policy[pos] = '←'
            elif best_action == s_right:
                optimal_policy[pos] = '→'
            
            if pos in HOLE_POS:
                optimal_policy[pos] = 'H'


            best_action_value = action_list_val[best_action]
            new_vT[pos] = best_action_value
            
            delta = max(delta, abs(new_vT[pos] - vT[pos]))
            delta_values[iteration] = delta

    vT = new_vT
    

    print(f"Iteration {iteration}, max delta: {delta}")
    if delta < threshold:
        print("Converged!")
        break
# Print the final value table
pprint(vT)
# Print the optimal policy
pprint(optimal_policy)
# Print the delta values for each iteration
pprint(delta_values)

### SECTION FOR PLOTTING ----------------------------------------- ###
# Plotting the delta values
plt.plot(list(delta_values.keys()), list(delta_values.values()))
plt.xlabel('Iteration')
plt.ylabel('Delta')
plt.title('Delta Values Over Iterations')
plt.show()


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







        
        


    






        



