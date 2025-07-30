import subprocess

SERVICE_NAME = "parkplacetech-agent-updater"
SERVICE_NAME2 = "parkplacetech-collector"

def run_command(command):
    try:
        print(f"Running: {' '.join(command)}")
        subprocess.run(command, check=True)
        print(f"Command {' '.join(command)} executed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}: {e}\n")

def stop_service():
    run_command(["systemctl", "stop", SERVICE_NAME])
    run_command(["systemctl", "stop", SERVICE_NAME2])
    
def start_service():
    run_command(["systemctl", "start", SERVICE_NAME])
    run_command(["systemctl", "start", SERVICE_NAME2])

if __name__ == "__main__":
    print(f"Stopping service: {SERVICE_NAME} and {SERVICE_NAME2}")
    print()
    stop_service()

    print(f"Starting service: {SERVICE_NAME} and {SERVICE_NAME2}")
    print()
    start_service()
