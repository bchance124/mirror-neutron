#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>

#define TCAADDR 0x70


// This program reads data from 6 different magnetic sensors and outputs serially 

/* Assign a unique ID to this sensor at the same time */
// Sensor error when reading multiple sensors if Adafruit...Unified(0) is used
//Adafruit_HMC5883_Unified mag0 = Adafruit_HMC5883_Unified(0);

Adafruit_HMC5883_Unified mag1 = Adafruit_HMC5883_Unified(1);
Adafruit_HMC5883_Unified mag2 = Adafruit_HMC5883_Unified(2);
Adafruit_HMC5883_Unified mag3 = Adafruit_HMC5883_Unified(3);
Adafruit_HMC5883_Unified mag4 = Adafruit_HMC5883_Unified(4);
Adafruit_HMC5883_Unified mag5 = Adafruit_HMC5883_Unified(5);
Adafruit_HMC5883_Unified mag6 = Adafruit_HMC5883_Unified(6);


void displaySensorDetails(Adafruit_HMC5883_Unified *mag)
{
  sensor_t sensor;
  mag->getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" uT");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" uT");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" uT");  
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}


void setup() 
{
  Serial.begin(9600);
  while(!Serial){
    ;
  }
   /* Initialise the 1st sensor */
  
  tcaselect(1);
  if(!mag1.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }

   /* Initialise the 2nd sensor */
  tcaselect(2);
  if(!mag2.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
   /* Initialise the 3rd sensor */
  tcaselect(3);
  if(!mag3.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
   /* Initialise the 4th sensor */
  tcaselect(4);
  if(!mag4.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
   /* Initialise the 5th sensor */
  tcaselect(5);
  if(!mag5.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
  /* Initialise the 6th sensor */
  tcaselect(0);
  if(!mag0.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
  
}




void loop() 
{
  /* Get a new sensor event */ 
  sensors_event_t event1; 
  sensors_event_t event2;
  sensors_event_t event3;
  sensors_event_t event4;
  sensors_event_t event5;
  sensors_event_t event6;
  tcaselect(1);
  mag1.getEvent(&event1);
  tcaselect(2);
  mag2.getEvent(&event2);
  tcaselect(3);
  mag3.getEvent(&event3);
  tcaselect(4);
  mag4.getEvent(&event4);
  tcaselect(5);
  mag5.getEvent(&event5);
  tcaselect(6);
  mag6.getEvent(&event6);
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("Sensor #1 - ");
  //Serial.print("X: "); 
  Serial.print(event1.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); 
  Serial.print(event1.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); 
  Serial.print(event1.magnetic.z); Serial.print("  ");//Serial.println("uT");
   
 
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("Sensor #2 - ");
  //Serial.print("X: "); 
  Serial.print(event2.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); 
  Serial.print(event2.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); 
  Serial.print(event2.magnetic.z); Serial.print("  ");//Serial.println("uT");

 
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("Sensor #3 - ");
  //Serial.print("X: "); 
  Serial.print(event3.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); 
  Serial.print(event3.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); 
  Serial.print(event3.magnetic.z); Serial.print("  ");//Serial.println("uT");
  
 
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("Sensor #4 - ");
  //Serial.print("X: "); 
  Serial.print(event4.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); 
  Serial.print(event4.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); 
  Serial.print(event4.magnetic.z); Serial.print("  ");//Serial.println("uT");


  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("Sensor #5 - ");
  //Serial.print("X: "); 
  Serial.print(event5.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); 
  Serial.print(event5.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); 
  Serial.print(event5.magnetic.z); Serial.print("  ");

  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("Sensor #6 - ");
  //Serial.print("X: "); 
  Serial.print(event6.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); 
  Serial.print(event6.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); 
  Serial.print(event6.magnetic.z); Serial.print(" , ");//Serial.println("uT");
  
  
  delay(500);
}
