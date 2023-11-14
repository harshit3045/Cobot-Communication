import subprocess

# Specify the path to the Bash script
bash_script = "./commands.sh"

# Run the Bash script
process = subprocess.run([bash_script])

# Read and process the real-time output
while True:
    line = process.stdout
    if not line:
        break 
    line = line.readline() # No more data is being published
    # Process the captured line as needed
    print("loda ", line, end='')  # Print the line (or process it in some other way)



# List of commands you want to run
# commands = ["source ~/.bashrc", "cd .." , "cd ./manipulator_ws/", "ls", ". ./devel/setup.bash", "rosrun demo demo_leave_listen_node"]

# # Iterate through the list of commands
# for command in commands:
#     print(f"Running command: {command}")
    
#     result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Check the return code to see if the command was successful
#     if result.returncode == 0:
#         # Print the command's output
#         print("Command output:")
#         print(result.stdout)
#     else:
#         # Print an error message if the command failed
#         print("Command failed with error:")
#         print(result.stderr)
