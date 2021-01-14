import config


@config.log_error()
def fullname(first_name: str, last_name: str) -> str:
    return first_name + last_name

if __name__ == '__main__':
    result = fullname('Wendrew', 'Oliveira')
    print(result)