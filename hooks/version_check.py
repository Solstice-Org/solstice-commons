import sys
import subprocess
import os

cargo_url = "git show origin/master:Cargo.toml" if subprocess.call("git ls-remote", stderr=open(os.devnull, "w"), stdout=open(os.devnull, "w")) == 0 else "git show master:Cargo.toml"
cargo_master = subprocess.check_output(cargo_url).decode("utf-8")

with open("Cargo.toml", "rt") as f:
    cargo_current = f.read()

version_master = [i for i in cargo_master.split("\n") if i[0:7]=="version"][0][11:-1]
version_current = [i for i in cargo_current.split("\n") if i[0:7]=="version"][0][11:-1]

if version_current == version_master:
    print("Versions should not be the same as on master, please increment as you see fit.")
    print(f"Master Version: \"{version_master}\"\nCommit Version: \"{version_current}\"")
    exit(1)

exit(0)