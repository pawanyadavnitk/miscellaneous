long int x,y,initial_t,final_t,t;
float acc;
int intensity_laser1 = 500;   //can be any value according to intensity of light(output of ldr)...should always be checked and updated each time before installation
int intensity_laser2 = 600;   //can be same or different than intensity_laser1
void setup() 
{
 Serial.begin(9600);
 Serial.print("System Initialised \n");
 
 while(analogRead(A4)>=500)     //engages pointer in the empty loop untill vehicle crosses the first laser
 {}                              
 
 initial_t=millis();            
 Serial.print("Vehicle started \n");
 
 while(analogRead(A2)>=500)     //engages pointer in the loop untill the vehicle crosses the second laser
 {}                              
 
 final_t=millis();
 t=final_t-initial_t;
 
 Serial.print("Vehicle Reached \n");
 Serial.print("Time taken=");
 Serial.println(t);
/* acc=100000000/(t*t);
 Serial.print(" \n acceleration=")*/
}

void loop() {}
