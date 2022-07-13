import platform


def detect_machine() -> bool:
    ret = platform.machine()

    if ret in 'x86':
        return True
    else:
        return False


if __name__ == '__main__':
    print(f'{platform.machine()}')