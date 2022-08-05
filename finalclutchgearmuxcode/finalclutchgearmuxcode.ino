const int gup=9;
const int gdn=8;
const int c_ft=6;          //clutch fast
//const int c_sw=7;         //clutch slow
const int G1=10;
const int G2=11;
const int G3=12;
const int c_sw_ip=5;
const int c_ft_ip=4;

const int g_up_ip=3;
const int g_dn_ip=2;
const int dn = A0;
const int up = A1;
//const int clutch_button=6;

int bcf;         //button clutch slow
int bdn;
int bup;
int lbdn;
int lbup;
int gear,lastgear=-1;
void setup() {
 Serial.begin(9600);
  pinMode(gup,INPUT);
  pinMode(gdn,INPUT);
  pinMode(c_ft,INPUT);
  pinMode(c_sw,INPUT);
  pinMode(G1,INPUT);
  pinMode(G2,INPUT);
  pinMode(G3,INPUT);
  pinMode(up,INPUT);
  pinMode(dn,INPUT);
  pinMode(c_sw_ip,OUTPUT);
  pinMode(c_ft_ip,OUTPUT);
  pinMode(g_up_ip,OUTPUT);
  pinMode(g_dn_ip,OUTPUT);

  
  
}
void scan_gear()
{
  if(digitalRead(G1)==LOW&&digitalRead(G2)==HIGH&&digitalRead(G3)==HIGH)
   gear=0;
   if(digitalRead(G1)==HIGH&&digitalRead(G2)==LOW&&digitalRead(G3)==HIGH)
   gear=1;
   if(digitalRead(G1)==LOW&&digitalRead(G2)==LOW&&digitalRead(G3)==HIGH)
   gear=2;
   if(digitalRead(G1)==HIGH&&digitalRead(G2)==HIGH&&digitalRead(G3)==LOW)
   gear=3;
   if(digitalRead(G1)==LOW&&digitalRead(G2)==HIGH&&digitalRead(G3)==LOW)
   gear=4;
   if(digitalRead(G1)==HIGH&&digitalRead(G2)==LOW&&digitalRead(G3)==LOW)
   gear=5;
   if(digitalRead(G1)==LOW&&digitalRead(G2)==LOW&&digitalRead(G3)==LOW)
   gear=6;
}
void loop() 
{
   bcf= digitalRead(c_ft);
  if(bft==LOW){
    digitalWrite(c_ft_ip,HIGH);
    while(bcf==LOW)
   bcf= digitalRead(c_ft);
   digitalWrite(c_ft_ip,LOW);
   }
  
  
   bdn=digitalRead(gdn);
   bup=digitalRead(gup);   
   scan_gear();            //check gear
   Serial.print(gear);
   lastgear = gear;
digitalWrite(13,HIGH);

while(bcs==LOW)
{
  digitalWrite(c_sw_ip,LOW);
  digitalWrite(13,HIGH);
  bcs=digitalRead(c_sw);
}
   
      if(bup != lbup)
      {
        if(bup==LOW)
        {
          if(gear==1)
          {
            digitalWrite(c_ft_ip,HIGH);
            delay(50);
            digitalWrite(g_up_ip,HIGH);
            delay(200);
            digitalWrite(g_up_ip,LOW);
            delay(50);
            digitalWrite(c_ft_ip,LOW);
            }          
        else
        {
          digitalWrite(c_ft_ip,HIGH);
          delay(50);
          while(analogRead(up)<=100)
          {
            digitalWrite(g_up_ip,HIGH);
            delay(10);
           
          }
          digitalWrite(g_up_ip,LOW);
          delay(50);
          digitalWrite(c_ft_ip,LOW);
          digitalWrite(13,HIGH);
        }
        //delay(16);
      }
      }
      if(bdn != lbdn)
      {
        if(gear==0)
        {
          if(bdn==LOW)
          {
            digitalWrite(c_sw_ip,HIGH);
            delay(50);
            while(analogRead(dn)<=100)
            {
              digitalWrite(g_dn_ip,HIGH);
              delay(10);
            }
            digitalWrite(g_dn_ip,LOW);
            delay(50);
            digitalWrite(c_sw_ip,LOW);
            digitalWrite(13,HIGH);
          }
        //delay(16);
        }
        else
        {
        if(bdn==LOW)
        {
          digitalWrite(c_ft_ip,HIGH);
          delay(50);
          while(analogRead(dn)<=100)
          {
            digitalWrite(g_dn_ip,HIGH);
            delay(10);
          }
          digitalWrite(g_dn_ip,LOW);
          delay(50);
          digitalWrite(c_ft_ip,LOW);
        }
        }
        //delay(16);
      }
       digitalWrite(13,HIGH);
       lbdn=bdn;
       lbup=bup;
       scan_gear();
  Serial.print(gear);
        
    
}
