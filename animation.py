import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-3, 3)

# Initialize line objects, which will be updated in the animation
line, = ax.plot([], [], lw=2)
counter_line, = ax.plot([], [], lw=2, color='red')
sum_line, = ax.plot([], [], lw=2, color='green')

# Function to initialize the background of the animation


def init():
    line.set_data([], [])
    counter_line.set_data([], [])
    sum_line.set_data([], [])
    return line, counter_line, sum_line

# Function to update the line for each frame


def update(frame):
    x = np.linspace(0, 2 * np.pi, 1000)
    # Shift the sine wave based on the frame number
    y = np.sin(x + 0.1 * frame)
    # Counter-face sine wave, moving in opposite direction
    y_counter = np.sin(x - 0.1 * frame)
    y_sum = y + y_counter  # Sum of the two sine waves
    line.set_data(x, y)
    counter_line.set_data(x, y_counter)
    sum_line.set_data(x, y_sum)
    return line, counter_line, sum_line


# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200),
                    init_func=init, blit=True, interval=50)

# Display the animation
plt.xlabel('x-axis')
plt.ylabel('y')
plt.title('Animated Sine Waves with Counter-Face and Sum')
plt.show()
