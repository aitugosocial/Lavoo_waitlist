
import subprocess
import sys
import os

def kill_port(port):
    print(f"Checking port {port}...")
    try:
        # Try finding PIDs using lsof
        # -t: terse (only PIDs)
        # -i: internet files
        result = subprocess.run(['lsof', '-t', '-i', f':{port}'], capture_output=True, text=True)
        pids = result.stdout.strip().split('\n')
        pids = [p for p in pids if p] # Filter empty strings

        if not pids:
            print(f"No process found on port {port}.")
            return

        print(f"Found processes on port {port}: {pids}")
        for pid in pids:
            try:
                print(f"Killing PID {pid}...")
                subprocess.run(['kill', '-9', pid], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to kill {pid}: {e}")
        
        print(f"Port {port} cleaned.")

    except FileNotFoundError:
        print("Error: 'lsof' command not found. Trying 'fuser'...")
        try:
             subprocess.run(['fuser', '-k', f'{port}/tcp'], check=True)
             print(f"Port {port} cleaned using fuser.")
        except FileNotFoundError:
            print("Error: 'fuser' command also not found. Please install lsof or psmisc.")
        except subprocess.CalledProcessError:
             # fuser returns non-zero if no process is killed, which is fine
             print(f"No process found on port {port} (or fuser failed).")

def main():
    print("="*40)
    print("   LAVOO PORT CLEANUP UTILITY")
    print("="*40)
    
    kill_port(8000)
    kill_port(8001)
    kill_port(3000) # Kill Vite server to ensure strict restart
    
    print("\n✓ Cleanup complete. You can now start your servers.")

if __name__ == "__main__":
    main()
