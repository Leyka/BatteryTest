#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include "secrets.h"

#define SERVER_IP "192.168.1.100:5000"
#define API_TESTS_ROUTE "/api/tests"

void wait_for_wifi();
int send_http_battery_test(int battery_id, int capacity, float resistance);

void setup() {
  // Begin connection to wifi
  WiFi.begin(WIFI_SSID, WIFI_PW);
}

void loop() {
  // Make sure we are still connected to wifi connection
  if (WiFi.status() != WL_CONNECTED) {
    wait_for_wifi();
  }

  // Dummy data
  int battery_id = 1337;
  int capacity = 2500;
  float resistance = 3.14;

  int code = send_http_battery_test(battery_id, capacity, resistance);

  // Dummy delay
  delay(5000);
}

void wait_for_wifi() {
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

// Returns 0 if success, else an HTTP code error (ex. 404, 500 etc.)
int send_http_battery_test(int battery_id, int capacity, float resistance) {
  WiFiClient client;
  HTTPClient http;

  char* url = "http://" SERVER_IP API_TESTS_ROUTE;
  http.begin(client, url);
  http.addHeader("Content-Type", "application/json");

  // Send POST payload
  char payload[512];
  sprintf(payload, "{\"public_id\": %d, \"capacity_mah\": %d, \"resistance_mohm\": %f}", battery_id, capacity, resistance);
  int httpCode = http.POST(payload);
  http.end();

  if (httpCode == HTTP_CODE_OK) {
    // Success
    return 0;
  }

  // Most likely an error
  return httpCode;
}
