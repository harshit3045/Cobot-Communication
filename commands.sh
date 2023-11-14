#!/bin/bash


# Change to the home directory and source .bashrc
source ~/.bashrc

# Change to the 'manipulator_ws' directory
cd ../catkin_ws/

# Source the 'setup.bash' file in the 'devel' directory
source ./devel/setup.bash

# Run the 'demo_ui' using 'rosrun'
rosrun demo demo_ask_item

rosrun demo demo_leave_listen_node