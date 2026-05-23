def menu_action(func):
    def wrapper(*args, **kwargs):
        print()
        print("=" * 40)
        result = func(*args, **kwargs)
        print("=" * 40)
        return result

    return wrapper