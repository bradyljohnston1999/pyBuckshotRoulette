class BuckshotRoulette:
    def __init__(self):
        self.is_running = False

    def run_loop(self):
        self.is_running = not self.is_running
        while self.is_running:
            print("BuckshotRoulette loop")
            input("Press Enter to continue...")
            self.is_running = False
