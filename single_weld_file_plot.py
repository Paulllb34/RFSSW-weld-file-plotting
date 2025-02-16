# Paul Blackhurst, Aug 9 2023

# This code may need slight tweaks in order to work for all Bond RFSSW weld files.
# The "+1000" on line 23 is determined by the weld cycle time, feel free to change it.

# By default, this code will save the plot generated as a png in the same folder the
# csv was selected from.

import os
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Open file dialog to select a CSV file
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Please Select a .csv File")

if file_path:

    data = pd.read_csv(file_path)

    start_index = (data.iloc[:, 4] < 0.5).idxmax()

    end_index = start_index + 700

    filtered_data = data.iloc[start_index:end_index]

    # If you change what data the BOND machine records, it may change the order of the columns
    # in the output file and you will need to fix that here.
    time = filtered_data.iloc[:,2]
    shoulder_pos = filtered_data.iloc[:,4]
    probe_pos = filtered_data.iloc[:,5]
    shoulder_force = filtered_data.iloc[:,9]
    probe_force = filtered_data.iloc[:,10]

    fig, ax1 = plt.subplots()

    # Plot position data on the left y-axis
    ax1.plot(time, shoulder_pos, label='Shoulder Position', color='tab:blue', linestyle='dotted')
    ax1.plot(time, probe_pos, label='Probe Position', color='tab:red', linestyle='dotted')
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Position (mm)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    ax2 = ax1.twinx()  # Create a twin y-axis

    # Plot force data on the right y-axis
    ax2.plot(time, shoulder_force, label='Shoulder Force', color='tab:blue')
    ax2.plot(time, probe_force, label='Probe Force', color='tab:red')
    ax2.set_ylabel('Force (N)', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    # Combine legends from both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.title('2023 11 06 10 23 00')

    # Get the directory path of the original data file
    directory = os.path.dirname(file_path)

    # Construct the full path for saving the image
    save_path = os.path.join(directory, '2023_11_06_10_23_00')

    # Save the plot as a PNG image with higher resolution (300 dpi)
    plt.savefig(save_path, dpi=300)

    plt.show()