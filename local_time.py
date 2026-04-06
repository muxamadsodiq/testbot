from datetime import datetime


def get_local_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(f"Local time: {get_local_time()}")
