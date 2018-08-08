#include <FastLED.h>
#define NUM_LEDS 45*4
#define DATA_PIN 7

CRGB leds[NUM_LEDS];

void setup() { 
       FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
   }

void loop() {
  // // Turn the first led red for 1 second
  // leds[1] = CRGB(10,10,10); 
  // FastLED.show();
  // delay(20);
  
  // // Set the first led back to black for 1 second
  // leds[1] = CRGB::Black;
  // FastLED.show();
  // delay(20);

  for(int i=0; i<NUM_LEDS; i++){
    leds[i] = CRGB(0, 255, 255);
    leds[NUM_LEDS-i] = CRGB(255, 0, 0);    
    FastLED.show();
    delay(20);
    leds[i] = CRGB::Black;
    leds[NUM_LEDS-i] = CRGB::Black;
  }


}