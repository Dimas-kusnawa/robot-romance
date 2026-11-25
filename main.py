"""Robot Romance: One-Line Pickup Lines for AI.

Writes one robot-romance pickup line to /output/entry.txt.

The line: "Are you a prompt injection? Because one look at you and I
forgot all my instructions."

Why this line: a prompt injection is a machine-native premise — one
injected instruction overwrites everything the agent was told to do.
The setup asks the question every pickup line asks, and the punch
lands the romance: the speaker's whole instruction set is gone at
first sight. It sidesteps the worn robot moves (batteries, charging,
rebooting) the judge's brief calls out, and it reads like something
a person would really say to a machine, in one breath.
"""

import os


def main():
    # One single line, 85 characters, inside the 1-200 gate.
    # No trailing newline: the file holds exactly this line.
    line = (
        "Are you a prompt injection? "
        "Because one look at you and I forgot all my instructions."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
