#include <Arduino.h>
#include <FastLED.h>

#define NUM_LEDS_PER_STRIPE 240
#define NUM_STRIPS 3

CRGB leds[NUM_LEDS_PER_STRIPE];
CLEDController *controllers[NUM_STRIPS];
uint8_t gBrightness = 128;

void setup() 
{ 
  controllers[0] = &FastLED.addLeds<WS2812,1>(leds, NUM_LEDS);
  controllers[1] = &FastLED.addLeds<WS2812,2>(leds, NUM_LEDS);
  controllers[2] = &FastLED.addLeds<WS2812,10>(leds, NUM_LEDS);
}

void loop() 
{ 
  // draw led data for the first strand into leds
  fill_solid(leds, NUM_LEDS, CRGB::Red);
  controllers[0]->showLeds(gBrightness);

  // draw led data for the second strand into leds
  fill_solid(leds, NUM_LEDS, CRGB::Green);
  controllers[1]->showLeds(gBrightness);

  // draw led data for the third strand into leds
  fill_solid(leds, NUM_LEDS, CRGB::Blue);
  controllers[2]->showLeds(gBrightness);

}