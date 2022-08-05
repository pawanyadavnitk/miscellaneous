 long int rpm,t=0,cur_t,t0;                  //time variables
 long int rpm1,t1=0,cur_t1,t10;
 long int rpm2,t2=0,cur_t2,t20;
 void setup()
 { pinMode(2,INPUT);
   pinMode(3,OUTPUT);
   pinMode(4,OUTPUT);
   pinMode(5,INPUT);
   pinMode(6,OUTPUT);
   pinMode(7,OUTPUT);
   pinMode(8,INPUT);
   /*digitalWrite(3,HIGH);
   digitalWrite(4,LOW);
   digitalWrite(6,HIGH);
   digitalWrite(7,LOW);*/
   
   Serial.begin(9600);
 }
int val=0,pre_val=1;
/*int val1=0,pre_val1=1;
int val2=0,pre_val2=1;*/
 void loop()
 {     
  val=digitalRead(2);
    if (pre_val == HIGH && val == LOW)    
              {cur_t = micros();
               rpm=(1000000 * 60 / (cur_t - t));
                Serial.println(rpm);
                 t = micros();}
    
    
   /* val1=digitalRead(5);
    if (pre_val1 == HIGH && val1 == LOW)
              {cur_t1 = micros();
                rpm1=(1000000 * 60 / (cur_t1 - t1));
                Serial.print('\t');
                Serial.println(rpm1);
                 t1 = micros();}
     
      
    val2=digitalRead(8);  
    if (pre_val2 == HIGH && val2 == LOW)
              {cur_t2 = micros();
              rpm2=(1000000 * 60 / (cur_t2 - t2));
              Serial.print('\t');
              Serial.print('\t');
              Serial.println(rpm2);
                 t2 = micros();} 
   
*/    
   
   t0=micros();
       if (t0-t>1000000)
       Serial.println(0);
  
   
         
         pre_val=val;
        //pre_val1=val1;
         //pre_val2=val2;
  
                               }
