import subprocess

def run_program():
    # Define the command to run program2.py with inputs
    command = ['python3', 'project2.py', '1', '401', '380', '8920', '373', '273', '.01', '.01']

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output from the program
    print("Output:")
    print(result.stdout)

    # Print any errors if they exist
    if result.stderr:
        print("Errors:")
        print(result.stderr)

# Run the program
run_program()
