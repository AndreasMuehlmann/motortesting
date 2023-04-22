int SENSORPIN = 3;
int OUTPUT_PIN = 5;
int HOLES = 20;
volatile unsigned long count, t2;
unsigned long t1;
double rpm;
int voltage;

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
}

void loop() {
    if (t2 > t1) {
        calc_rpm(t1, t2, count);
        t1 = t2;
        count = 0;
    } else {
          double theoretical_rpm = calc_rpm(t1, micros(), 1);
          if (theoretical_rpm < rpm) {
              rpm = theoretical_rpm;
          }
    }
    Serial.println(rpm);
    while(!Serial.available() > 0) {}
    String incomingData = Serial.readStringUntil('\n');
    if (!incomingData.equals("yes")) {
        if (voltage != incomingData.toInt()) {
            voltage = incomingData.toInt();
            analogWrite(OUTPUT_PIN, voltage);
        }
    }
    delay(5);
}
