// #include <bitswap.h>
// #include <chipsets.h>
// #include <color.h>
// #include <colorpalettes.h>
// #include <colorutils.h>
// #include <controller.h>
// #include <cpp_compat.h>
// #include <dmx.h>
// #include <fastled_config.h>
// #include <fastled_delay.h>
// #include <fastled_progmem.h>
// #include "FastLED.h"
// #include <fastpin.h>
// #include <fastspi_bitbang.h>
// #include <fastspi_dma.h>
// #include <fastspi_nop.h>
// #include <fastspi_ref.h>
// #include <fastspi_types.h>
// #include <fastspi.h>
// #include <hsv2rgb.h>
// #include <led_sysdefs.h>
// #include <lib8tion.h>
// #include <noise.h>
// #include <pixelset.h>
// #include <pixeltypes.h>
// #include <platforms.h>
// #include <power_mgt.h>

// int ledPin=13;
// int switchPin=5;

// void setup()

// {
//   Serial.begin(9600);
//   pinMode(ledPin,OUTPUT);

// }
// void loop()

// {
//     digitalWrite(ledPin, LOW);//DBG
//     delay(500);    
//     digitalWrite(ledPin, HIGH);//DBG 
//     delay(500);    
// }
#include <Arduino.h>
#include <FastLED.h>

#define NUM_LEDS 720
#define NUM_STRIPS 8

CRGB leds[NUM_LEDS];
CLEDController *controllers[NUM_STRIPS];
uint8_t gBrightness = 128;

void setup() 
{ 
  controllers[0] = &FastLED.addLeds<WS2812,1>(leds, NUM_LEDS);
  controllers[1] = &FastLED.addLeds<WS2812,2>(leds, NUM_LEDS);
  controllers[2] = &FastLED.addLeds<WS2812,10>(leds, NUM_LEDS);
  controllers[3] = &FastLED.addLeds<WS2812,11>(leds, NUM_LEDS);
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

  // draw led data for the first strand into leds
  fill_solid(leds, NUM_LEDS, CRGB::White);
  controllers[3]->showLeds(gBrightness);
}
