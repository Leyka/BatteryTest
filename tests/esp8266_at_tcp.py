"""
ESP8266 instructions:
https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf
"""
from serial import Serial
from threading import Thread, Event


def encode_at_instruction(instruction):
    return f'AT+{instruction}\r\n'.encode()


def read_from_esp():
    while not cancel_event.is_set():
        bytes = ftdi.read_until('\n'.encode())
        if bytes:
            print(bytes.decode())


PORT = "/dev/cu.usbserial-A50285BI"  # on mac
ftdi = Serial(PORT, 115200, timeout=2)

if not ftdi.is_open:
    raise(f"FTDI at port {PORT} is not open...")

# Create a seprate thread that will read ESP buffer
cancel_event = Event()
t = Thread(target=read_from_esp)
t.start()

# connect TCP port 5000 (not working for now)
connect_tcp = 'CIPSTART="TCP","127.0.0.1",5000'
ftdi.write(encode_at_instruction(connect_tcp))


# Terminate
input()
cancel_event.set()
t.join()
ftdi.close()
