#include <Wire.h>
#include <Adafruit_MCP4725.h>

Adafruit_MCP4725 dac;

int SENSORPIN = 2;
int RILAIS_PIN = 9;
int HOLES = 20;
volatile unsigned long count, t2;
unsigned long t1;
double rpm;
int voltage;
int timeout_time_in_millis = 500;
int read_voltage;
int read_current;

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
    dac.begin(0x62);
    count, t1, t2, rpm = 0;
    pinMode(SENSORPIN, INPUT);
    attachInterrupt(digitalPinToInterrupt(SENSORPIN), interrupt_handler, RISING);
    pinMode(RILAIS_PIN, OUTPUT);
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
    read_voltage = analogRead(A0);
    read_current = analogRead(A1);
    String to_send_string = String(rpm) + "," + String(read_voltage) + "," + String(read_current);
    Serial.println(to_send_string);
    int start = millis();
    while(!Serial.available() > 0) {
        if (millis() - start > 100) {
            dac.setVoltage(0, false);
            digitalWrite(RILAIS_PIN, LOW);
        }
        delay(5);
    }
    String incomingData = Serial.readStringUntil('\n');
    voltage = incomingData.toInt();
    if (voltage < 255 / 6) {
        digitalWrite(RILAIS_PIN, HIGH);
        dac.setVoltage(0, false);
    } else {
        digitalWrite(RILAIS_PIN, LOW);
        dac.setVoltage((int) (voltage * 16), false);
    }
    delay(50);
}
