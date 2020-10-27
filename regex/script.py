from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve(strict=True).parent

# 1. Read the file as a string
with open(BASE_DIR / "data" / "workers.csv") as f:
    DATA = f.read()

# 2. Extract US phone numbers
RE_US_PHONE_NUMBERS = re.compile(
    r"""
    [\(]?(\d{3})[\.\)]?   # area code and . literal
    (\d{3})[\.\-]?   # prefix number and . literal
    (\d{4})     # line number
    """,
    re.VERBOSE,
)

count = 0
for match in RE_US_PHONE_NUMBERS.findall(DATA):
    count += 1
    print(count, match)

# 3. Standardize phone number format

# 4. Print newly formatted phone numbers