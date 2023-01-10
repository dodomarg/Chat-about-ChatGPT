#include <DHT.h>
#include <PID_v1.h>
#include <Wire.h>
//#include <LiquidCrystal_I2C.h>
#include <rgb_lcd.h>

// Constants
const int DHT_PIN = 4; // Pin for DHT sensor
const int RELAY_PIN = 7; // Pin for relay
const int BUTTON_UP_PIN = 2; // Pin for button to increase goal temperature
const int BUTTON_DOWN_PIN = 3; // Pin for button to decrease goal temperature
const int TEMP_DISPLAY_DELAY = 100; // Delay between updates to temperature display (milliseconds)

// Variables
double sensorTemp; // Current temperature from sensor
double setTemp = 30; // Goal temperature
double output; // Output from PID controller

// Initialize DHT sensor
DHT dht(DHT_PIN, DHT22);

// Initialize PID controller
PID pid(&sensorTemp, &output, &setTemp, 0.5, 10, 10,P_ON_M, DIRECT);

// Initialize I2C display
//LiquidCrystal_I2C lcd(0x27, 16, 2);
rgb_lcd lcd;

void setup() {
  // Set pin modes
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUTTON_UP_PIN, INPUT_PULLUP);
  pinMode(BUTTON_DOWN_PIN, INPUT_PULLUP);

  // Initialize DHT sensor
  dht.begin();

  // Initialize PID controller
  pid.SetMode(AUTOMATIC);
  pid.SetSampleTime(1000); // Set sample time to 1 second
  pid.SetOutputLimits(-255, 255); // Set output limits to 0-255
  pid.SetTunings(pid.GetKp(), pid.GetKi(), pid.GetKd()); // Use auto tune for tunings
  pid.SetControllerDirection(REVERSE); // Reverse direction of controller

  // Initialize I2C display
  //lcd.init();
  //lcd.backlight();
  lcd.begin(16, 2); // set up the LCD's number of columns and rows
  Serial.begin(9600);
}

void loop() {
  // Read temperature from sensor
  sensorTemp = dht.readTemperature();

  // Run PID controller
  pid.Compute();

  // Set relay to high if output is above 0
  if (output < 0) {
    digitalWrite(RELAY_PIN, HIGH);
  } else {
    digitalWrite(RELAY_PIN, LOW);
  }

  // Check if button to increase goal temperature is pressed
  if (digitalRead(BUTTON_UP_PIN) == LOW) {
    // Increase goal temperature
    setTemp += 1;
  }

  // Check if button to decrease goal temperature is pressed
  if (digitalRead(BUTTON_DOWN_PIN) == LOW) {
    // Decrease goal temperature
    setTemp -= 1;
  }

  // Print PID controller parameters to serial monitor
  Serial.print("Kp: ");
  Serial.print(pid.GetKp());
  Serial.print("  Ki: ");
  Serial.print(pid.GetKi());
  Serial.print("  Kd: ");
  Serial.println(pid.GetKd());
  Serial.print("Output: ");
  Serial.println(output);
  
  // Update temperature display
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Set Temp: ");
  lcd.print(setTemp);
  lcd.setCursor(0, 1);
  lcd.print("Real Temp: ");
  lcd.print(sensorTemp);
  delay(TEMP_DISPLAY_DELAY); 
}
