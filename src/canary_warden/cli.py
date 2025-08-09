import argparse, os
from .watcher import watch_canaries
from .kill_switch import kill_switch

def setup_canaries(folder_count, files_per_folder):
    base = "./canary"
    os.makedirs(base, exist_ok=True)
    paths = []
    for i in range(folder_count):
        d = os.path.join(base, f"decoy{i+1}")
        os.makedirs(d, exist_ok=True)
        paths.append(d)
        for j in range(files_per_folder):
            ext = [".docx", ".xlsx", ".jpg", ".pdf"][j % 4]
            fname = f"canary_{i+1}_{j+1}{ext}"
            with open(os.path.join(d, fname), "w") as f:
                f.write("safe canary file\n")
    return paths

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folders", type=int, default=2)
    ap.add_argument("--files", type=int, default=5)
    ap.add_argument("--threshold", type=int, default=10)
    ap.add_argument("--demo", action="store_true", help="Simulate file changes to show detection")
    args = ap.parse_args()
    paths = setup_canaries(args.folders, args.files)
    if args.demo:
        import time
        d = paths[0]
        files = [os.path.join(d, f) for f in os.listdir(d)]
        for f in files:
            os.rename(f, f + ".encrypted")
            time.sleep(0.1)
        print("Demo modifications done.")
        time.sleep(2)
    print("Monitoring canary folders...")
    watch_canaries(paths, args.threshold, kill_switch)

if __name__ == "__main__":
    main()
