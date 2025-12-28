import time
import requests
import threading

URL = "http://localhost:5000"

def send_traffic():
    print(f"Starting generic traffic to {URL}...")
    while True:
        try:
            requests.get(URL)
            # Sleep slightly to not overload purely CPU (unless we want to!)
            time.sleep(0.1) 
        except Exception as e:
            print(f"Request failed: {e}")
            time.sleep(1)

if __name__ == "__main__":
    # Start 5 concurrent threads to generate noise
    for i in range(5):
        t = threading.Thread(target=send_traffic)
        t.daemon = True
        t.start()

    print("--- Chaos Control Center ---")
    print("1. Toggle High Latency Mode")
    print("2. Toggle Error Mode")
    print("3. KILL APP (Test K8s Self-Healing)")
    print("q. Quit")

    while True:
        choice = input("Select Chaos > ")
        if choice == '1':
            requests.post(f"{URL}/chaos/latency")
            print("Action sent: Toggle Latency")
        elif choice == '2':
            requests.post(f"{URL}/chaos/error")
            print("Action sent: Toggle Error")
        elif choice == '3':
            try:
                requests.post(f"{URL}/chaos/kill")
                print("Action sent: KILL! App should restart momentarily.")
            except:
                pass 
        elif choice == 'q':
            break
