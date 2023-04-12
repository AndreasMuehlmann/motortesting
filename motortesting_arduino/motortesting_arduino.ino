int SENSORPIN = 3;
int HOLES = 40;

volatile unsigned long count, t2;
unsigned long t1;
double rpm;

void interrupt_handler() {
    count += 1;
    t2 = millis();
}

void setup() {
    Serial.begin(9600);
    count = 0;
    t1 = 0;
    t2 = 0;
    rpm = 0;
    pinMode(SENSORPIN, INPUT);
    attachInterrupt(digitalPinToInterrupt(SENSORPIN), interrupt_handler, FALLING);
}

void loop() {
    double T_in_micro_s;
    if (t2 > t1) {
        T_in_micro_s = HOLES * (t2 - t1) / count;
        rpm = (unsigned) (long) (60000 / T_in_micro_s);
        t1 = t2;
        count = 0;
    } else {
        T_in_micro_s = HOLES * (millis() - t1);
        double theoretical_rpm = (unsigned) (long) (60000 / T_in_micro_s);
        if (theoretical_rpm < rpm) {
          rpm = theoretical_rpm;
        }
    }
    Serial.println(rpm);
}