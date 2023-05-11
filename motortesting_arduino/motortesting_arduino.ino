int SENSORPIN = 2;
int OUTPUT_PIN = 5;
int RILAIS_PIN = 10;
int HOLES = 20;
volatile unsigned long count, t2;
unsigned long t1;
double rpm;
int voltage;
int timeout_time_in_millis = 500;

void interrupt_handler() {
    count += 1;
    t2 = micros();
}

double calc_rpm(unsigned long t1, volatile unsigned long t2, volatile unsigned long count) {
    double T_in_micro_s = HOLES * (t2 - t1) / count;
    return (unsigned) (long) (60000000 / T_in_micro_s);
}

void setup() {
    Serial.begin(9600);
    count, t1, t2, rpm = 0;
    pinMode(SENSORPIN, INPUT);
    attachInterrupt(digitalPinToInterrupt(SENSORPIN), interrupt_handler, RISING);
    pinMode(OUTPUT_PIN, OUTPUT);
    voltage = 0;
}

void loop() {
    if (t2 > t1) {
        rpm = calc_rpm(t1, t2, count);
        t1 = t2;
        count = 0;
    } else {
          double theoretical_rpm = calc_rpm(t1, micros(), 1);
          if (theoretical_rpm < rpm) {
              rpm = theoretical_rpm;
          }
    }
    int read_voltage = analogRead(A0);
    String to_send_string = String(rpm) + "," + String(read_voltage);
    Serial.println(to_send_string);
    //int start = millis();
    while(!Serial.available() > 0) {
      delay(5);
      //if (timeout_time_in_millis < millis() - start) {
      //  analogWrite(OUTPUT_PIN, 0);
      //  break;
      //}
    }
    String incomingData = Serial.readStringUntil('\n');
    if (voltage < 255 / 5) {
      digitalWrite(RILAIS_PIN, HIGH);
      voltage = 0;
    } else {
      digitalWrite(RILAIS_PIN, LOW);
    }
    if (voltage != incomingData.toInt()) {
      voltage = incomingData.toInt();
      analogWrite(OUTPUT_PIN, voltage);
    }
    delay(50);
}
