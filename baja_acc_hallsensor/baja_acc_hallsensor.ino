 long int rpm,t=0,cur_t,t0,rev=0,y;           
 int val=0,pre_val=1;
 void setup()
 { pinMode(2,INPUT);
   pinMode(7,OUTPUT);
   digitalWrite(7,HIGH);   
   Serial.begin(9600);
   analogWrite(A0,0);
   while(1)
   { Serial.println(analogRead(A0));
    if(analogRead(A0)>0)
   { Serial.print("BUTTON PRESSED");t0=millis();return;
   }
 }}

 void loop()
 {      
       val=digitalRead(2);          
            if (pre_val == HIGH && val == LOW)      
              { rev += 1;
               Serial.println(rev);}        
       if(rev>=10 && rev<15)
       {y=millis();
       cur_t=y-t0;
       Serial.println(cur_t);
       rev=15;}
       pre_val=val;  
       
            
 }          
