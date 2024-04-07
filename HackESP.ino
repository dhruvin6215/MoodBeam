#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>

// Network Credentials
const char* ssid = "Elliot iPhone";
const char* password = "SFhacks24";
int value = 8;
WebServer server(80);

void setup() {
  Serial.begin(115200); // Start the Serial communication
  
  
  WiFi.begin(ssid, password); // Connect to the network

  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    //Serial.println("Connecting to WiFi...");
  }

  //Serial.println("Connected to WiFi");
  Serial.print("W"); // Long Pulse to indicate WiFi connection
  Serial.println(WiFi.localIP());
  
  server.begin(); // Start the server
  
}

void loop() {
  server.handleClient(); // Handle client requests
  //Serial.print("A");    // Send 'A' to the Arduino
  Serial.print(value);    // Send 'A' to the Arduino

  delay(5000);          // Wait for 5 seconds
}
