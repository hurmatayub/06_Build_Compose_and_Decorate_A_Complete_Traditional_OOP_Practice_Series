class Logger:
    def __init__(self):
        print("Logger started (Constructor)")

    def __del__(self):
        print("Logger closed (Destructor)")

log = Logger()

del log
