Here’s a fully formatted **README.md** for your Ransomware Kill-Switch Simulator project (“canary-warden”)—just copy, edit, and use!

***

# canary-warden

**Ransomware Kill-Switch Simulator**  
A safe, local utility that creates decoy files and folders, watches for ransomware-like activity (mass renames/modifications), and simulates a “kill-switch” response when suspicious behavior is detected.  
Built for blue-team labs, demos, and educational purposes.

## Features

- Creates configurable canary/decoy folders and files
- Monitors for rapid mass changes (e.g., >10 file events in 5 seconds)
- Detects file renames (extension changes), creates, deletes, modifies
- Logs alerts to terminal and `warden_alert.log`
- Simulates a kill-switch (prints message, logs event)
- Demo mode to safely trigger detections for presentations
- Easy to install — pure Python

## Quick Start

```bash
git clone https://github.com//canary-warden.git
cd canary-warden
python -m venv .venv && source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install watchdog rich
```

## Usage

Create and monitor decoy folders/files:
```bash
python -m src.canary_warden.cli --folders 2 --files 5 --threshold 10
```

Run a demo (no actual ransomware required; safely triggers detection):
```bash
python -m src.canary_warden.cli --demo
```

**Arguments:**
- `--folders`: Number of canary folders to create (default: 2)
- `--files`: Number of decoy files per folder (default: 5)
- `--threshold`: Number of suspicious file events before alert (default: 10)
- `--demo`: Simulate rapid file renames to trigger detection (safe)

**Example Output:**
```bash
[bold red]Ransomware-Like Activity Detected![/bold red]
Affected files/events: 10
Simulated kill-switch: Block/stop test process.
```

Alerts are also logged into `warden_alert.log`.

## How It Works

- On startup, creates clean canary folders and files (e.g., .docx, .pdf, .jpg)
- Uses Python’s [watchdog](https://pypi.org/project/watchdog/) library to monitor file activity
- If threshold of events is met in a short time (default 5 seconds), triggers a kill-switch
- Does **not** execute destructive actions—safe for all environments

## Project Structure

```
canary-warden/
├─ src/canary_warden/
│  ├─ cli.py            # Command-line interface
│  ├─ watcher.py        # Monitors file events in canary folders
│  ├─ kill_switch.py    # Defines simulated kill-switch response
│  └─ __init__.py
├─ tests/
│  └─ test_watcher.py
├─ examples/
├─ README.md
├─ LICENSE
├─ requirements.txt
└─ .gitignore
```

## Limitations

- Not a production defense tool—no real ransomware blocking or process killing.
- Focused on local file event simulations for educational security purposes.
- Not suitable as endpoint protection; use enterprise tools for real-world defense.

## Roadmap

- Add selectable real process blocking (using psutil, with user confirmation)
- Webhook integration (send alerts to Slack, Discord, etc.)
- GUI/Tray interface for user-friendly operation
- Configurable alert sensitivity and canary layout

## License

MIT

## Acknowledgments

Thanks to the open-source community for [watchdog](https://pypi.org/project/watchdog/) and [rich](https://github.com/Textualize/rich) for easy monitoring and beautiful output.

***

**Feel free to edit, add screenshots, or improve demo sections as your project grows!**
