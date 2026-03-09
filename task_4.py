default_time = 60


def training_session(rounds):
    """Runs training session with several rounds"""
    time_per_round = default_time

    def adjust_time():
        """Adjusts time for next round"""
        nonlocal time_per_round
        time_per_round -= 5

    for i in range(1, rounds + 1):
        print(f"Раунд {i}: {time_per_round} хвилин")
        adjust_time()


training_session(3)
