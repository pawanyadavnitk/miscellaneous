int gear;
int previousgear;
int debouncedelay=50;
long int lastdebouncetime=0;


void setup()
{
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  pinMode(6,INPUT);
  pinMode(7,INPUT);
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  pinMode(10,INPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  
  if (digitalRead(2)==LOW)   
  gear=2;                  //for gear 1
  if (digitalRead(3)==LOW)
  gear=3;                  //for gear 0
  if (digitalRead(4)==LOW)
  gear=4;                  //for gear 2
  if (digitalRead(5)==LOW)
  gear=5;                  //for gear 3
  if (digitalRead(6)==LOW)
  gear=6;                  //for gear 4
  if (digitalRead(7)==LOW)
  gear=7;                  //for gear 5
  if (digitalRead(8)==LOW)
  gear=8;                  //for gear 6
 
  previousgear=gear;    // sets the value of previousgear : for later use
 
}
void loop()
{
  if (digitalRead(2)==LOW)
  gear=2;
  if (digitalRead(3)==LOW)
  gear=3;
  if (digitalRead(4)==LOW)
  gear=4;
  if (digitalRead(5)==LOW)
  gear=5;
  if (digitalRead(6)==LOW)
  gear=6;
  if (digitalRead(7)==LOW)
  gear=7;
  if (digitalRead(8)==LOW)
  gear=8;

 if(digitalRead(9)==HIGH && (millis()-lastdebouncetime>debouncedelay) && previousgear<8)
  digitalWrite(11,HIGH); //to operate solenoid
 
  if(gear>previousgear)
  {digitalWrite(11,LOW);
  previousgear=gear;}
  
 if(digitalRead(10)==HIGH && (millis()-lastdebouncetime>debouncedelay) && previousgear>2)
    digitalWrite(12,HIGH); //to operate solenoid
    
   if(gear<previousgear)
   {digitalWrite(12,LOW);
   previousgear=gear;}
 
  
}


