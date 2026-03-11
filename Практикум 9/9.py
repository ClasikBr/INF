from pathlib import Path

input_path = Path("input.txt")
output_path = Path("simple/output.txt")

output_path.parent.mkdir(exist_ok=True)

lines = input_path.read_text(encoding="utf-8").splitlines()

output_path.write_text(
    "\n".join(line for i, line in enumerate(lines, start=1) if i % 2 == 0),
    encoding="utf-8"
)
