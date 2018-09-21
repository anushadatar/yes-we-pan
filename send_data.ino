// Quinn Kelley and Anusha Datar 
// 3D Scanner Arduino Code

/*
 * Transmits servo angle and distance sensor data 
 * for each servo step over serial for further
 * analysis. This code is intentionally generic and lightweight
 * as all processing occurs onboard a laptop with python instead
 * of on the microcontroller.
 */

// Grab the libraries for the time-of-flight sensor and for the servos.
#include "Adafruit_VL53L0X.h"
#include "Servo.h"

// The sensor works over I2C, so no need to worry about pin mappings for that.
Adafruit_VL53L0X lox = Adafruit_VL53L0X();
// Servos need pin mappings, declarations, bounds, and position counters.
// Keeping naming conventions generic to emphasize post-processing.
Servo servoA;
Servo servoB;
int servoApin = 9;
int servoBpin = 10;
int servoApos = 0; 
int servoBpos = 0;

int servoAmin = 45;
int servoAmax = 135;
int servoBmin = 45;
int servoBmax = 100;

void setup() {
  // Kick off Serial. Be sure to match baudrate on python script.
  Serial.begin(9600);
  while (! Serial) {
    delay(1);
  }
  // Make sure that the sensor boots before moving any motors.
  if (!lox.begin()) {
    // DEBUG
    // Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  // DEBUG
  // Serial.println(F("Booted sensor.")); 
  // Declare servos.
  servoA.attach(servoApin);
  servoB.attach(servoBpin); 
  // Confirm that the servos go home.
  zero_servos();
}


void loop() {
  /* 
   *  Print a consistent data structure of distance measurement and each servo position
   * over serial so it can be processed by the python script. The format should be
   * [DISTANCE_READ (mm), SERVOA_ANGLE, SERVOB_ANGLE]
   */
  VL53L0X_RangingMeasurementData_t measure;

  for (servoApos = servoAmin; servoApos <= servoAmax; servoApos += 1) {
    servoA.write(servoApos);        
    delay(15);                      
    for (servoBpos = servoBmin; servoBpos <= servoBmax; servoBpos += 1) {
      servoB.write(servoBpos);
      delay(15);
      // Send data from the sensor if there is no phase failure. Otherwise, just
      // move on to the next angle because we can try to interpolate in post.
      lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
      if (measure.RangeStatus != 4) {
        // Sends appropriate values over serial.
        Serial.print("Distance: ");
        Serial.print(measure.RangeMilliMeter);
        Serial.print(" ");
        Serial.print(servoApos);
        Serial.print(" ");
        Serial.print(servoBpos);
        Serial.print("\n");
      } 
    }  
  }
  // Continue for multiple scans if appropriate.
  delay(500);
  zero_servos();
  delay(100);
}

void zero_servos() {
  /*
   * Bring servos back to their original positions at the start of processing.
   */
  servoA.write(servoAmin);
  delay(15);
  servoB.write(servoBmin);
  delay(15);
  delay(200);
}

