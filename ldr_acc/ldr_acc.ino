int x,y;
int long m,n;
void setup() 
{
Serial.begin(9600);
}


void loop() 
{
 x=analogRead(A4);
 y=analogRead(A2);
 if(x>1020)
 m=millis();
 if(y>1020){
 n=millis();
 Serial.println(n-m);
 }

}
