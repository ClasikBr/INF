from datetime import datetime

def convert_datetime(dt: str) -> None:
    try:
        t = datetime.strptime(dt, "%m/%d/%Y %H:%M:%S")
    except ValueError:
        print('Неверная дата или время')
        return

    print(t.strftime("%d.%m.%y %I:%M:%S %p"))
