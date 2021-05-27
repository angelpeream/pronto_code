bool FORWARD = true;
bool BACKWARD = false;

#define PIN_DIRECTION 15
// 20 = A1

#define PIN_DISABLE 16
// 21 = A2

#define PIN_STEP 7
// 7

#define PIN_LED 13

#define PIN_SENSOR 2
 
int currentPos = 0;

#define COMMAND_FORWARD  0
#define COMMAND_BACKWARD  1
#define COMMAND_HOME  2
#define COMMAND_MOVE  3
#define COMMAND_POS  4
#define COMMAND_CHECK  5
#define COMMAND_RAW 6
#define COMMAND_ENABLE 7
#define COMMAND_DISABLE 8
#define COMMAND_ATHOME 9

//-------------------------------------
void setup() {
  // initialize serial:
  Serial.begin(9600);
  
  // make the pins outputs:
  pinMode(19, INPUT);
  pinMode(PIN_DIRECTION, OUTPUT);
  pinMode(PIN_DISABLE, OUTPUT); 
  pinMode(PIN_STEP, OUTPUT); 
  pinMode(PIN_LED, OUTPUT); 
  pinMode(PIN_SENSOR, INPUT);

  digitalWrite(PIN_DISABLE,HIGH);
  
}

//---------------------------------------
void moveMotor(boolean dir, int steps) {
  
  if (dir == true) {
    digitalWrite(PIN_DIRECTION, HIGH);
  } else {
     digitalWrite(PIN_DIRECTION, LOW);
  }
  
  //digitalWrite(PIN_DISABLE, HIGH);
  
  for (int i = 0; i < steps; i++) {
    
    digitalWrite(PIN_STEP, HIGH);
    digitalWrite(PIN_LED, HIGH);
    delay(10);
    digitalWrite(PIN_STEP, LOW);    
    digitalWrite(PIN_LED, LOW);
    delay(10);
  }
  
  
}

//-------------------------------------------
// loop
//-------------------------------------------
void loop() {
 // if there's any serial available, read it:

  while (Serial.available() > 0) {

    // look for t he next valid integer in the incoming serial stream:
    int command = Serial.parseInt(); 
    Serial.read();
    int param1 = Serial.parseInt(); 
    Serial.read();     
    int param2 = Serial.parseInt();     
    Serial.read();
    
    //Serial.print("COMMAND "); Serial.print(command); Serial.print("(");
    //Serial.print(param1); Serial.print(", ");
    //Serial.print(param2); Serial.print(")\n");
   
    while(Serial.peek() != -1) {      
      Serial.read();
    }
    
    if (command == COMMAND_MOVE ) {
      
       if (param1 > 0) {
          moveMotor(FORWARD, param1);
          Serial.print("Moved FWD ");
          Serial.print(param1);
          Serial.print(" OK\n");   
       } else {
          moveMotor(BACKWARD, -param1);
          Serial.print("Moved BWD OK\n");   
       }
       Serial.print("moved"); Serial.print(param1); Serial.print("\n\n");
       
    } else if (command == COMMAND_FORWARD) {
      moveMotor(FORWARD, param1);
      Serial.print("moved forward"); Serial.print(param1); Serial.print("\n\n");

    } else if (command == COMMAND_BACKWARD) {
      moveMotor(BACKWARD, param1);
      Serial.print("moved backward"); Serial.print(param1); Serial.print("\n\n");
          
          
    } else if (command == COMMAND_HOME) {
      
      while(!digitalRead(PIN_SENSOR)) 
        {
          moveMotor(BACKWARD, 5);
        }
      Serial.print("OK, HOME FOUND"); Serial.print("\n\n");
      
    } else if (command == COMMAND_CHECK) {
      Serial.print("COMMS OK \n\n");
      
      
    } else if (command == COMMAND_ATHOME) {
      
      digitalWrite(PIN_LED, digitalRead(PIN_SENSOR));
      
      if (digitalRead(PIN_SENSOR)) {
        Serial.print("ON");
      } else {
        Serial.print("OFF");
      }
      Serial.print("\n\n");
   
      
    } else if (command == COMMAND_POS) {
      Serial.print(currentPos);
      Serial.print("OK\n\n");
      
    } else if (command == COMMAND_RAW) {

      pinMode(param1, OUTPUT);
      Serial.print("RAW()");
      
      if (param2 == 1) {
           digitalWrite(param1, HIGH);
           Serial.write("xxx1\n\n");
           
       } else if (param2 == 0) {
           digitalWrite(param1, LOW);
           Serial.write("xxx0\n\n");
           
       } else {
         digitalWrite(param1, LOW);
         Serial.print("ERROR on Param\n\n");
       }
       
       //Serial.print("LED"); Serial.print(param1); Serial.print(" "); Serial.print(param2); Serial.print("\n");
       
    } else if (command == COMMAND_ENABLE) {
      digitalWrite(PIN_DISABLE, HIGH);
      Serial.print("MOTOR ENABLED\n\n");
      
    } else if (command == COMMAND_DISABLE) {
      digitalWrite(PIN_DISABLE, LOW);
      Serial.print("MOTOR DISABLED\n\n");
      
    } else { 
      Serial.print("KO\n\n");
    }
    
  } // while
  
} // loop
