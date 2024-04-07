void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Initialize the onboard LED pin as an output
  Serial.begin(115200);         // Start the Serial communication at 115200 baud rate
}

void loop() {
  if (Serial.available()) {     // If there is data available to read,
    char receivedChar = Serial.read(); // Read the incoming byte
    if (receivedChar == '8') {  // 0.5 second pulse every 5 seconds throughout connection
      digitalWrite(LED_BUILTIN, HIGH); 
      delay(500);               
      digitalWrite(LED_BUILTIN, LOW);  
    } else if (receivedChar == 'W') { // single 3 second pulse indicating WiFi connected
      digitalWrite(LED_BUILTIN, HIGH);
      delay(3000);
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
