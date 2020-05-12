def create_fake_timer(initial: int = 0):
    counter = initial

    def fake_timer():
        nonlocal counter
        old_counter = counter
        counter = counter + 2
        return old_counter

    return fake_timer
