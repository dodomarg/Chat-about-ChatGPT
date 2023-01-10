#include <Wire.h>
#include <rgb_lcd.h>
#include <DHT.h>

// Set up the temperature sensor
#define DHTPIN 4    // Pin where DHT22 is connected
#define DHTTYPE DHT22   // DHT22 (AM2302)

DHT dht(DHTPIN, DHTTYPE);

// Set up the display
rgb_lcd lcd;

// Set up the buttons
const int upButtonPin = 2;
const int downButtonPin = 3;

// Set up the relay
const int relayPin = 7;

// Set up the goal temperature
int goalTemp = 24; // Initial goal temperature

void setup() {
  // Initialize the serial monitor
  Serial.begin(9600);

  // Initialize the display
  lcd.begin(16, 2);

  // Initialize the buttons
  pinMode(upButtonPin, INPUT_PULLUP);
  pinMode(downButtonPin, INPUT_PULLUP);

  // Initialize the relay
  pinMode(relayPin, OUTPUT);

  // Initialize the temperature sensor
  dht.begin();
}

void loop() {
  // Read the current temperature
  float temp = dht.readTemperature();

  // Control the relay based on the current temperature and the goal temperature
  if (temp < goalTemp) {
    digitalWrite(relayPin, HIGH);
  } else {
    digitalWrite(relayPin, LOW);
  }

  // Update the display
  lcd.setCursor(0, 0);
  lcd.print("Goal: ");
  lcd.print(goalTemp);
  lcd.print("C");
  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(temp);
  lcd.print("C");

  // Print the current temperature and goal temperature to the serial monitor
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println("C");
  Serial.print("Goal Temperature: ");
  Serial.print(goalTemp);
  Serial.println("C");

  // Check if the up button or down button has been pressed
  if (digitalRead(upButtonPin) == LOW) {
    goalTemp++;
  }
  if (digitalRead(downButtonPin) == LOW) {
    goalTemp--;
  }

  // Delay for a bit before checking again
  delay(200);
}
