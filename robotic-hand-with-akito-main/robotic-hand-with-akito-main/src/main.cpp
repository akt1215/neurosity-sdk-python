#include <Arduino.h>
#include <Servo.h> // Define the pin connected to the servo
#include <string.h>

Servo thumb;
Servo thumbjoint;
Servo pointer;
Servo middle;
Servo ring;
Servo pinky; // Create a servo object


void setup() {
  thumb.attach(A9);
  thumbjoint.attach(11);
  pointer.attach(A8);
  middle.attach(A0);
  ring.attach(A4);
  pinky.attach(0); // Attach the servo to the pin
}

/*
void loop() {
  // Open fingers
  thumb.write(1900);
  delay(100);
  thumbjoint.write(1900);
  delay(100);
  pointer.write(800);
  delay(100);
  middle.write(2500);
  delay(100);
  ring.write(700);
  delay(100);
  pinky.write(750);
  delay(3000);

  //Close fingers
  thumb.write(1000);
  thumbjoint.write(1200);
  pointer.write(2300);
  middle.write(600);
  ring.write(1950);
  pinky.write(2000);
  delay(3000);
}
*/

void RPS(string choice) {

  switch (choise){
    case "rock":
      thumb.write(1000);
      thumbjoint.write(1200);
      pointer.write(3000);
      middle.write(600);
      ring.write(1950);
      pinky.write(2000);
      delay(3000);
      break;
    case "paper":
      thumb.write(1900);
      thumbjoint.write(1900);
      pointer.write(800);
      middle.write(2500);
      ring.write(700);
      pinky.write(750);
      delay(3000);
      break;
    case "scissors":
      pointer.write(800);
      middle.write(2500);
      thumb.write(1000);
      thumbjoint.write(1200);
      ring.write(1950);
      pinky.write(2000);
      delay(3000);
      break;
  }
}

void loop() {
  // //Rock
  // thumb.write(1000);
  // thumbjoint.write(1200);
  // pointer.write(3000);
  // middle.write(600);
  // ring.write(1950);
  // pinky.write(2000);
  // delay(3000);

  // //Paper
  // thumb.write(1900);
  // thumbjoint.write(1900);
  // pointer.write(800);
  // middle.write(2500);
  // ring.write(700);
  // pinky.write(750);
  // delay(3000);

  // //Scissors
  // pointer.write(800);
  // middle.write(2500);
  // thumb.write(1000);
  // thumbjoint.write(1200);
  // ring.write(1950);
  // pinky.write(2000);
  // delay(3000);
  RPS("rock");
  delay(3000);
  RPS("paper");
  delay(3000);
  RPS("scissors");]
  delay(3000);
}

