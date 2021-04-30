#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include "secrets.h"

#define SERVER_IP "192.168.1.100:5000"
#define API_TESTS_ROUTE "/api/tests"

void wait_for_wifi();
void send_http_battery_test(int battery_id, int capacity, float resistance);

void setup() {
  Serial.begin(115200);
  Serial.println();

  // Connect to wifi
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

  send_http_battery_test(battery_id, capacity, resistance);

  // Dummy delay
  delay(5000);
}

void wait_for_wifi() {
  Serial.print("Waiting for wifi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
}

void send_http_battery_test(int battery_id, int capacity, float resistance) {
  WiFiClient client;
  HTTPClient http;

  char* url = "http://" SERVER_IP API_TESTS_ROUTE;
  Serial.println("[HTTP] Begin request");
  http.begin(client, url);
  http.addHeader("Content-Type", "application/json");

  // Send POST payload
  char payload[512];
  sprintf(payload, "{\"public_id\": %d, \"capacity_mah\": %d, \"resistance_mohm\": %f}", battery_id, capacity, resistance);
  int httpCode = http.POST(payload);

  if (httpCode > 0) {
    Serial.printf("[HTTP] Code: %d\n", httpCode);

    // Success
    if (httpCode == HTTP_CODE_OK) {
      const String& payload = http.getString();
      Serial.println("[HTTP] Received payload:\n<<");
      Serial.println(payload);
      Serial.println(">>");
    }
  } else {
    Serial.printf("[HTTP] Failed, error: %s\n", http.errorToString(httpCode).c_str());
  }

  http.end();
}
