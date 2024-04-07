#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>

// Network Credentials
const char* ssid = "Elliot iPhone"; //temporary credentials
const char* password = "SFhacks24";
int value = 0;
WebServer server(80);

void handleData() {
  if (server.hasArg("plain") == false) { // Check if body received
    server.send(400, "text/plain", "Bad Request");
    return;
  }

  DynamicJsonDocument doc(1024);
  deserializeJson(doc, server.arg("plain"));
  value = doc["value"]; // JSON data
  Serial.println(value); // Print value to the serial 

  server.send(200, "text/plain", "Data received");
}

void setup() {
  Serial.begin(115200); 
  WiFi.begin(ssid, password); // Connect to the network

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }

  Serial.print("Connected to WiFi, IP address: ");
  Serial.println(WiFi.localIP());
  
  // Define route for the data
  server.on("/data", HTTP_POST, handleData);
  
  server.begin(); // Start the server
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient(); // Handle client requests
}
