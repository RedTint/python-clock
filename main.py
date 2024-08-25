import matplotlib.pyplot as plt
import numpy as np
import datetime

def draw_clock(hour, minute, second):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')  # Hide the axis

    # Draw the clock face
    clock_face = plt.Circle((0, 0), 1, edgecolor='black', facecolor='white', lw=2)
    ax.add_patch(clock_face)

    # Hour, minute, and second hand angles
    hour_angle = np.pi / 2 - 2 * np.pi * (hour % 12 + minute / 60) / 12
    minute_angle = np.pi / 2 - 2 * np.pi * (minute + second / 60) / 60
    second_angle = np.pi / 2 - 2 * np.pi * second / 60

    # Draw the hour, minute, and second hands
    ax.plot([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)], lw=6, color='black')
    ax.plot([0, 0.8 * np.cos(minute_angle)], [0, 0.8 * np.sin(minute_angle)], lw=4, color='blue')
    ax.plot([0, 0.9 * np.cos(second_angle)], [0, 0.9 * np.sin(second_angle)], lw=2, color='red')

    # Draw clock numbers
    for number in range(1, 13):
        angle = np.pi / 2 - 2 * np.pi * number / 12
        x = 0.85 * np.cos(angle)
        y = 0.85 * np.sin(angle)
        ax.text(x, y, str(number), horizontalalignment='center', verticalalignment='center', fontsize=15)

    plt.show()

def get_current_time():
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second

if __name__ == "__main__":
    hour, minute, second = get_current_time()
    draw_clock(hour, minute, second)
