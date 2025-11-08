import os
import yaml
from render_config import render_config

DEVICE_DIR = "snapshots/ci_net/device-yaml"
OUTPUT_DIR = "snapshots/ci_net/s1/configs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(DEVICE_DIR):
    if not file.endswith(".yaml"):
        continue

    path = os.path.join(DEVICE_DIR, file)
    with open(path) as f:
        data = yaml.safe_load(f)

    cfg = render_config(data)
    hostname = data["hostname"]

    out_path = os.path.join(OUTPUT_DIR, f"{hostname}_gen.cfg")

    with open(out_path, "w") as out:
        out.write(cfg)

    print(f"Rendered: {hostname}_gen.cfg")
