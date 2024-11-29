from RouletteUtilz import clean, Colors


class BuckshotRoulette:
    def __init__(self):
        self.is_running = False

    def run_loop(self):
        clean()
        self.is_running = not self.is_running
        while self.is_running:
            print(f"{Colors.YELLOW}{Colors.UNDERLINE}BuckshotRoulette{Colors.RESET} {Colors.GREEN}{Colors.BLINK}loop", Colors.RESET)
            input("\nPress Enter to continue...")
            self.is_running = False
