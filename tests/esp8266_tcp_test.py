from time import sleep
from serial import Serial
from threading import Thread, Event


def encode(msg):
    return f'{msg}\r\n'.encode()


def read_from_esp():
    while not cancel_event.is_set():
        bytes = ftdi.read_until('\n'.encode())
        if bytes:
            print(bytes.decode())


PORT = "/dev/cu.usbserial-A50285BI"
ftdi = Serial(PORT, 115200, timeout=2)

if not ftdi.is_open:
    raise(f"FTDI at port {PORT} is not open...")

# Create a seprate thread that will read ESP buffer
cancel_event = Event()
t = Thread(target=read_from_esp)
t.start()

# Test

ftdi.write(encode('AT'))


# Terminate
input()
cancel_event.set()
t.join()
ftdi.close()
