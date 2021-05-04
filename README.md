# BatteryTest

18650 Lithium battery capacity tester with web interface

## Server

### Configuration

File `.env`:

```
DEBUG=True
DB_PATH=/path/to/db.sqlite
```

### Run with Docker

Run Docker command example

Build image
```
$ docker build -t batterytest .
```

Run
```
$ docker run -d -p 80:80 -v ~/Lab/BatteryTestWeb/db:/app/db batterytest
```

## Firmware
### Configuration
Add `secrets.h` file under `esp01-http` folder with content:

```cpp
#define WIFI_SSID "YOUR WIFI SSID"
#define WIFI_PW  "YOUR WIFI PASSWORD"
```
