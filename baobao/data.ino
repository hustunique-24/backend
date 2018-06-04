继电器  控制马达
int pinRelay = 6; //管脚D3连接到继电器模块的信号脚

void setup() {
  pinMode(pinRelay, OUTPUT); //设置pinRelay脚为输出状态
}

void loop() { 
   digitalWrite(pinRelay, HIGH);//输出HIGH电平,继电器模块闭合
   delay(1000); //等待5000毫秒

   digitalWrite(pinRelay, LOW);//输出LOW电平,继电器模块断开
   delay(1000); //等待8000毫秒
}

温度  7
#include <dht.h>

dht DHT;

#define DHT11_PIN 7

void setup()
{
  Serial.begin(115200);
  Serial.println("DHT TEST PROGRAM ");
  Serial.print("LIBRARY VERSION: ");
  Serial.println(DHT_LIB_VERSION);
  Serial.println();
  Serial.println("Type,\tstatus,\tHumidity (%),\tTemperature (C)");
}

void loop()
{
  // READ DATA
  Serial.print("DHT11, \t");
  int chk = DHT.read11(DHT11_PIN);
  switch (chk)
  {
    case DHTLIB_OK:  
                Serial.print("OK,\t"); 
                break;
    case DHTLIB_ERROR_CHECKSUM: 
                Serial.print("Checksum error,\t"); 
                break;
    case DHTLIB_ERROR_TIMEOUT: 
                Serial.print("Time out error,\t"); 
                break;
    case DHTLIB_ERROR_CONNECT:
        Serial.print("Connect error,\t");
        break;
    case DHTLIB_ERROR_ACK_L:
        Serial.print("Ack Low error,\t");
        break;
    case DHTLIB_ERROR_ACK_H:
        Serial.print("Ack High error,\t");
        break;
    default: 
                Serial.print("Unknown error,\t"); 
                break;
  }
  // DISPLAY DATA
  Serial.print(DHT.humidity, 1);
  Serial.print(",\t");
  Serial.println(DHT.temperature, 1);

  delay(2000);
}
//
// END OF FILE
//


心率 A1


倾斜模块 倾倒传感器模块 倾斜开关 角度模块/开关 Arduino
 A0 1
int sensorPin = A0;
int ledPin = 13;
int sensorValue = 1;

void setup() {
  pinMode(ledPin, OUTPUT);  
  Serial.begin(115200);
}

void loop() {
  sensorValue = analogRead(sensorPin); 
  Serial.println(sensorValue);  
  digitalWrite(ledPin, HIGH);  
  delay(100);          
  digitalWrite(ledPin, LOW);   
  delay(100);                  
}






arduino总代码

/*  Pulse Sensor Amped 1.5    by Joel Murphy and Yury Gitman   http://www.pulsesensor.com

----------------------  Notes ----------------------  ----------------------
This code:
1) Blinks an LED to User's Live Heartbeat   PIN 13
2) Fades an LED to User's Live HeartBeat    PIN 5
3) Determines BPM
4) Prints All of the Above to Serial

Read Me:
https://github.com/WorldFamousElectronics/PulseSensor_Amped_Arduino/blob/master/README.md
 ----------------------       ----------------------  ----------------------
*/
#include <dht.h>

dht DHT;

#define DHT11_PIN 7
#define PROCESSING_VISUALIZER 1
#define SERIAL_PLOTTER  2

//  Variables
int pulsePin = 1;                 // Pulse Sensor purple wire connected to analog pin 0
int blinkPin = 13;                // pin to blink led at each beat
int fadePin = 5;                  // pin to do fancy classy fading blink at each beat
int fadeRate = 0;                 // used to fade LED on with PWM on fadePin
int sensorPin = A0;
int ledPin = 13;
int sensorValue = 1;

// Volatile Variables, used in the interrupt service routine!
volatile int BPM;                   // int that holds raw Analog in 0. updated every 2mS
volatile int Signal;                // holds the incoming raw data
volatile int IBI = 600;             // int that holds the time interval between beats! Must be seeded!
volatile boolean Pulse = false;     // "True" when User's live heartbeat is detected. "False" when not a "live beat".
volatile boolean QS = false;        // becomes true when Arduoino finds a beat.

// SET THE SERIAL OUTPUT TYPE TO YOUR NEEDS
// PROCESSING_VISUALIZER works with Pulse Sensor Processing Visualizer
//      https://github.com/WorldFamousElectronics/PulseSensor_Amped_Processing_Visualizer
// SERIAL_PLOTTER outputs sensor data for viewing with the Arduino Serial Plotter
//      run the Serial Plotter at 115200 baud: Tools/Serial Plotter or Command+L
static int outputType = PROCESSING_VISUALIZER;


void setup(){

  pinMode(blinkPin,OUTPUT);         // pin that will blink to your heartbeat!
  pinMode(fadePin,OUTPUT);  
   pinMode(ledPin, OUTPUT);  
  // pin that will fade to your heartbeat!
  Serial.begin(115200);             // we agree to talk fast!
  interruptSetup();                 // sets up to read Pulse Sensor signal every 2mS
   // IF YOU ARE POWERING The Pulse Sensor AT VOLTAGE LESS THAN THE BOARD VOLTAGE,
   // UN-COMMENT THE NEXT LINE AND APPLY THAT VOLTAGE TO THE A-REF PIN
//   analogReference(EXTERNAL);
//Serial.println("DHT TEST PROGRAM ");
//  Serial.print("LIBRARY VERSION: ");
 // Serial.println(DHT_LIB_VERSION);
  Serial.println();
  Serial.println("Type,\tstatus,\tHumidity (%),\tTemperature (C)");

}


//  Where the Magic Happens
void loop(){
sensorValue = analogRead(sensorPin); 
  Serial.print("倾斜:");
  Serial.println(sensorValue);  
  digitalWrite(ledPin, HIGH);  
  delay(100);          
  digitalWrite(ledPin, LOW);   
  delay(100);                  
    serialOutput() ;

  if (QS == true){     // A Heartbeat Was Found
                       // BPM and IBI have been Determined
                       // Quantified Self "QS" true when arduino finds a heartbeat
        fadeRate = 255;         // Makes the LED Fade Effect Happen
                                // Set 'fadeRate' Variable to 255 to fade LED with pulse
        serialOutputWhenBeatHappens();   // A Beat Happened, Output that to serial.
        QS = false;                      // reset the Quantified Self flag for next time
  }

  ledFadeToBeat();                      // Makes the LED Fade Effect Happen
  
 // Serial.print("DHT11, \t");
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("湿度:");
  Serial.println(DHT.humidity, 1);
  Serial.print("温度:");
  Serial.println(DHT.temperature, 1);

  delay(200);
//  take a break

}





void ledFadeToBeat(){
    fadeRate -= 15;                         //  set LED fade value
    fadeRate = constrain(fadeRate,0,255);   //  keep LED fade value from going into negative numbers!
    
    analogWrite(fadePin,fadeRate);          //  fade LED
  }


+上马达(输入b可以启动马达),
输入d可以查询倾斜值，大于100输出e，小于100输出f
如果倾斜则输出c,
/*  Pulse Sensor Amped 1.5    by Joel Murphy and Yury Gitman   http://www.pulsesensor.com

----------------------  Notes ----------------------  ----------------------
This code:
1) Blinks an LED to User's Live Heartbeat   PIN 13
2) Fades an LED to User's Live HeartBeat    PIN 5
3) Determines BPM
4) Prints All of the Above to Serial

Read Me:
https://github.com/WorldFamousElectronics/PulseSensor_Amped_Arduino/blob/master/README.md
 ----------------------       ----------------------  ----------------------
*/
#include <dht.h>

dht DHT;

#define DHT11_PIN 7
#define PROCESSING_VISUALIZER 1
#define SERIAL_PLOTTER  2

//  Variables
int pulsePin = 1;                 // Pulse Sensor purple wire connected to analog pin 0
int blinkPin = 13;                // pin to blink led at each beat
int fadePin = 5;                  // pin to do fancy classy fading blink at each beat
int fadeRate = 0;                 // used to fade LED on with PWM on fadePin
int sensorPin = A0;
int ledPin = 13;
int sensorValue = 2;
int led = 6;
// Volatile Variables, used in the interrupt service routine!
volatile int BPM;                   // int that holds raw Analog in 0. updated every 2mS
volatile int Signal;                // holds the incoming raw data
volatile int IBI = 600;             // int that holds the time interval between beats! Must be seeded!
volatile boolean Pulse = false;     // "True" when User's live heartbeat is detected. "False" when not a "live beat".
volatile boolean QS = false;        // becomes true when Arduoino finds a beat.

// SET THE SERIAL OUTPUT TYPE TO YOUR NEEDS
// PROCESSING_VISUALIZER works with Pulse Sensor Processing Visualizer
//      https://github.com/WorldFamousElectronics/PulseSensor_Amped_Processing_Visualizer
// SERIAL_PLOTTER outputs sensor data for viewing with the Arduino Serial Plotter
//      run the Serial Plotter at 115200 baud: Tools/Serial Plotter or Command+L
static int outputType = PROCESSING_VISUALIZER;


void setup(){
pinMode(led, OUTPUT);
  pinMode(blinkPin,OUTPUT);         // pin that will blink to your heartbeat!
  pinMode(fadePin,OUTPUT);  
   pinMode(ledPin, OUTPUT);  
  // pin that will fade to your heartbeat!
  Serial.begin(115200);             // we agree to talk fast!
  interruptSetup();                 // sets up to read Pulse Sensor signal every 2mS
   // IF YOU ARE POWERING The Pulse Sensor AT VOLTAGE LESS THAN THE BOARD VOLTAGE,
   // UN-COMMENT THE NEXT LINE AND APPLY THAT VOLTAGE TO THE A-REF PIN
//   analogReference(EXTERNAL);
//Serial.println("DHT TEST PROGRAM ");
//  Serial.print("LIBRARY VERSION: ");
 // Serial.println(DHT_LIB_VERSION);
  Serial.println();
  Serial.println("Type,\tstatus,\tHumidity (%),\tTemperature (C)");

}


//  Where the Magic Happens
void loop(){
sensorValue = analogRead(sensorPin); 
  Serial.print("倾斜:");
  Serial.println(sensorValue);  
  digitalWrite(ledPin, HIGH);  
  delay(100);          
  digitalWrite(ledPin, LOW);   
  delay(100);                  
    serialOutput() ;

  if (QS == true){     // A Heartbeat Was Found
                       // BPM and IBI have been Determined
                       // Quantified Self "QS" true when arduino finds a heartbeat
        fadeRate = 255;         // Makes the LED Fade Effect Happen
                                // Set 'fadeRate' Variable to 255 to fade LED with pulse
        serialOutputWhenBeatHappens();   // A Beat Happened, Output that to serial.
        QS = false;                      // reset the Quantified Self flag for next time
  }

  ledFadeToBeat();                      // Makes the LED Fade Effect Happen
  
 // Serial.print("DHT11, \t");
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("湿度:");
  Serial.println(DHT.humidity, 1);
  Serial.print("温度:");
  Serial.println(DHT.temperature, 1);
Serial.print("\n");
  delay(200);
//  take a break
digitalWrite(led, HIGH); // 点亮LED

delay(1000); // 延时1000ms(即1秒)

digitalWrite(led, LOW); // 熄灭LED

delay(1000); // 延时1000ms
}





void ledFadeToBeat(){
    fadeRate -= 15;                         //  set LED fade value
    fadeRate = constrain(fadeRate,0,255);   //  keep LED fade value from going into negative numbers!
    
    analogWrite(fadePin,fadeRate);          //  fade LED
  }




