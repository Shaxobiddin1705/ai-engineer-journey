import json
import sys
from datetime import datetime
from pathlib import Path


# Yozish file bilan
def add_json_2_file(file_path: Path, data: dict):
    with file_path.open("w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# O'qish file bilan
def read_json_from_file(file_path: Path) -> dict:
    with file_path.open("r") as f:
        return json.load(f)


def add_datetime_2_file(file_path: Path, dt: datetime):
    loaded = read_json_from_file(file_path)
    s = dt.isoformat(timespec="seconds")
    todos_list = []
    todos_list.append(loaded)
    todos_list.append({"now": s})
    with file_path.open("w") as f:
        json.dump(todos_list, f, indent=2, ensure_ascii=False)


def exit_code() -> dict | None:
    loaded = read_json_from_file(SETTINGS_FILE)
    print(loaded)
    return next((item for item in loaded if loaded[item] == "system"), None)


TODOS_FILE = Path("todos.json")
SETTINGS_FILE = Path("settings.json")


def main() -> None:
    # data = {"theme": "dark", "langs": ["en", "ru", "uz"]}

    # add_json_2_file(SETTINGS_FILE, data)
    # loaded = read_json_from_file(SETTINGS_FILE)
    # print(loaded["langs"])

    # now = datetime.now()
    # add_datetime_2_file(TODOS_FILE, now)

    theme = exit_code()
    if theme is None:
        print("No theme found in this settings file.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
