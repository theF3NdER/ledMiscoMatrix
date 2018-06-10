#include <FastLED.h>
#define NUM_LEDS 45
#define DATA_PIN 1

CRGB leds[NUM_LEDS];

void setup() { 
       FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
   }

void loop() {
      // Turn the first led red for 1 second
      leds[44] = CRGB(10,10,10); 
      FastLED.show();
      delay(1000);
      
      // Set the first led back to black for 1 second
      leds[44] = CRGB::Black;
      FastLED.show();
      delay(1000);
}