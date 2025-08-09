from rich import print
def kill_switch(events):
    print("[bold red]Ransomware-Like Activity Detected![/bold red]")
    print(f"Affected files/events: {len(events)}")
    with open("warden_alert.log", "a") as f:
        f.write(f"ALERT {len(events)} events: {events}\n")
    print("Simulated kill-switch: Block/stop test process.")
