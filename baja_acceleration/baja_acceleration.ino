 int revolutions = 0;
 float acc;
 long int t;
 int s=75;
 void setup()
 {
 Serial.begin(9600); 
 attachInterrupt(digitalPinToInterrupt(2), rev_counter, HIGH);
 Serial.print("hello");
 }
 
 void loop(){
  Serial.println(revolutions);
  if(revolutions>=20)
       {
        detachInterrupt(2);
        t = millis();        
       // acc=(2*s*1000000)/(t*t);
        Serial.println(t);
        revolutions=0;
        }
  attachInterrupt(digitalPinToInterrupt(2), rev_counter, HIGH);       
   }
 
 void rev_counter()
 {revolutions += 1;}
 
 

