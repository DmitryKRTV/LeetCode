# https://leetcode.com/problems/root-equals-sum-of-children/description/

# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.
# Example 1:

# Input: root = [10,4,6]
# Output: true
# Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
# 10 is equal to 4 + 6, so we return true.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        return root.val == root.left.val + root.right.val
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(5)
sol = Solution()
print(sol.checkTree(root))
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Value')
ax.set_title('Dynamic Plot')

# Create a line object to be updated
line, = ax.plot([], [], lw=2)

# Define the function to update the plot
def animate(i):
    t = np.linspace(0, 10, 100)
    y = np.sin(2 * np.pi * t - 0.01 * i)
    line.set_data(t, y)
    return line

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Add zoom functionality
def zoom(event):
    if event.button == 'up':
        ax.set_xlim(ax.get_xlim()[0] - 1, ax.get_xlim()[1] + 1)
        ax.set_ylim(ax.get_ylim()[0] - 0.5, ax.get_ylim()[1] + 0.5)
    elif event.button == 'down':
        ax.set_xlim(ax.get_xlim()[0] + 1, ax.get_xlim()[1] - 1)
        ax.set_ylim(ax.get_ylim()[0] + 0.5, ax.get_ylim()[1] - 0.5)
    fig.canvas.draw()

fig.canvas.mpl_connect('scroll_event', zoom)

# Display the plot
plt.show()