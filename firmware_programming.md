[doc of info on firmware](https://www.bytesnap.com/news-blog/firmware-explained-guide/)

#### some repo on firmware for guidnance of path
- [repo-1](https://github.com/mikeroyal/Firmware-Guide?tab=readme-ov-file)
- [repo-2](https://github.com/practical-tutorials/project-based-learning?tab=readme-ov-file#cc)

#### some youtube video on firmware programming
- [video 1](https://www.youtube.com/watch?v=I7kIcpWTulE)

#### i watch this course on coursera
- [coursera](https://www.coursera.org/learn/arduino-platform/supplement/qgXkl/course-overview)

#### Arduino IDE 
- [Arduino IDE](https://docs.arduino.cc/software/ide/)

#### Arduino simulator
- [Arduino simulator](https://library.io/)

#### Arduino documentation
- [Arduino documentation](https://www.arduino.cc/en/Guide/Introduction)

- when you run arduino ide : 
```bash
arduino:avrdude@6.3.0-arduino17
arduino:avr@1.8.6
Installing arduino:arduinoOTA@1.3.0
Configuring tool.
arduino:arduinoOTA@1.3.0 installed
Installing arduino:avr-gcc@7.3.0-atmel3.6.1-arduino7
Configuring tool.
arduino:avr-gcc@7.3.0-atmel3.6.1-arduino7 installed
Installing arduino:avrdude@6.3.0-arduino17
Configuring tool.
arduino:avrdude@6.3.0-arduino17 installed
Installing platform arduino:avr@1.8.6
Configuring platform.
Platform arduino:avr@1.8.6 installed
Missing FQBN (Fully Qualified Board Name)

Compilation error: Missing FQBN (Fully Qualified Board Name)Downloading LiquidCrystal@1.0.7
LiquidCrystal@1.0.7
Installing LiquidCrystal@1.0.7
Installed LiquidCrystal@1.0.7
Downloading Mouse@1.0.1
Mouse@1.0.1
Installing Mouse@1.0.1
Installed Mouse@1.0.1
Downloading Keyboard@1.0.6
Keyboard@1.0.6
Installing Keyboard@1.0.6
Installed Keyboard@1.0.6
Downloading Ethernet@2.0.2
Ethernet@2.0.2
Installing Ethernet@2.0.2
Installed Ethernet@2.0.2
Downloading SD@1.3.0
SD@1.3.0
Installing SD@1.3.0
Installed SD@1.3.0
Downloading Servo@1.2.2
Servo@1.2.2
Installing Servo@1.2.2
Installed Servo@1.2.2
Downloading Stepper@1.1.3
Stepper@1.1.3
Installing Stepper@1.1.3
Installed Stepper@1.1.3
Downloading Firmata@2.5.9
Firmata@2.5.9
Installing Firmata@2.5.9
Installed Firmata@2.5.9
Downloading TFT@1.0.6
TFT@1.0.6
Installing TFT@1.0.6
Installed TFT@1.0.6
Downloading Arduino_BuiltIn@1.0.0
Arduino_BuiltIn@1.0.0
Installing Arduino_BuiltIn@1.0.0
Installed Arduino_BuiltIn@1.0.0
```

#### C language learning
- funciton
- globle variable

#### arduino functions
- setup() : 
- loop() : After creating a setup() function, which initializes and sets the initial values, the loop() function does precisely what its name suggests, and loops consecutively, allowing your program to change and respond. Use it to actively control the Arduino board.
- pinMode() : Configures the specified pin to behave either as an input or an output. See the Digital Pins page for details on the functionality of the pins. It is possible to enable the internal pullup resistors with the mode INPUT_PULLUP. Additionally, the INPUT mode explicitly disables the internal pullups.
- digitalWrite() : Write a HIGH or a LOW value to a digital pin. If the pin has been configured as an OUTPUT with pinMode(), its voltage will be set to the corresponding value: 5V (or 3.3V on 3.3V boards) for HIGH, 0V (ground) for LOW. If the pin is configured as an INPUT, digitalWrite() will enable (HIGH) or disable (LOW) the internal pullup on the input pin. It is recommended to set the pinMode() to INPUT_PULLUP to enable the internal pull-up resistor. See the Digital Pins tutorial for more information. If you do not set the pinMode() to OUTPUT, and connect an LED to a pin, when calling digitalWrite(HIGH), the LED may appear dim. Without explicitly setting pinMode(), digitalWrite() will have enabled the internal pull-up resistor, which acts like a large current-limiting resistor.
- digitalRead() : Reads the value from a specified digital pin, either HIGH or LOW.

# Arduino.h explanation
The `Arduino.h` file is the main header file used in Arduino projects. It provides essential definitions, macros, and function declarations that allow users to program Arduino boards in a simplified way. Below is an explanation of its key components:

### 1. **License Information and Includes:**
   - The top comment indicates that this file is part of the Arduino SDK, licensed under the GNU Lesser General Public License (LGPL). The LGPL allows modification and redistribution under certain conditions.
   - Standard C libraries (`stdlib.h`, `stdbool.h`, `string.h`, `math.h`) and AVR-specific libraries (`avr/pgmspace.h`, `avr/io.h`, `avr/interrupt.h`) are included. These provide basic utilities, boolean logic, string manipulation, math operations, and access to the AVR microcontroller hardware.

### 2. **Macros for Pin States and Modes:**
   - `HIGH` and `LOW`: Represent digital pin states (`1` and `0`).
   - `INPUT`, `OUTPUT`, `INPUT_PULLUP`: Define pin modes for configuring whether a pin is an input, output, or input with an internal pull-up resistor.
   
### 3. **Mathematical Constants and Conversion Macros:**
   - Constants like `PI`, `HALF_PI`, `TWO_PI`, etc., represent common mathematical values.
   - Conversion macros like `DEG_TO_RAD` and `RAD_TO_DEG` convert between degrees and radians.
   
### 4. **Serial and Display Modes:**
   - Defines modes like `SERIAL` (0) and `DISPLAY` (1), used in certain Arduino boards for controlling output devices.

### 5. **Bitwise Operations:**
   - Defines macros like `bitRead`, `bitSet`, `bitClear`, and `bitWrite` to manipulate individual bits in a byte or word. These macros are crucial for low-level control of pins and peripherals.

### 6. **Interrupt Management:**
   - `interrupts()` and `noInterrupts()` enable and disable global interrupts, using AVR instructions `sei()` (set interrupts) and `cli()` (clear interrupts). This is important when writing critical sections of code that shouldn't be interrupted.

### 7. **Clock Cycle Calculations:**
   - Provides functions to calculate timing based on the system clock (`F_CPU`), such as `clockCyclesPerMicrosecond()` and `microsecondsToClockCycles()`. This is essential for timing-sensitive operations like pulse reading or delay calculations.

### 8. **Utility Functions:**
   - Functions like `millis()`, `micros()`, `delay()`, `delayMicroseconds()` provide common timing utilities.
   - `pinMode()`, `digitalWrite()`, `digitalRead()`, `analogRead()`, `analogWrite()`: These are the core functions for interacting with digital and analog pins.
   - `pulseIn()`, `pulseInLong()`: Functions for measuring pulse durations on pins.
   - `shiftOut()`, `shiftIn()`: Functions for bitwise data transfer using serial communication protocols like SPI.

### 9. **Board-Specific Definitions:**
   - AVR-based definitions handle the specific capabilities of different microcontrollers, such as ATtiny or ATmega chips. For example, different voltage references (`INTERNAL`, `DEFAULT`, `EXTERNAL`) are available based on the chip.

### 10. **Bit Manipulation Functions:**
   - Macros and utility functions like `lowByte()`, `highByte()` to extract lower and higher parts of a word.
   - `min()`, `max()`, `abs()`, `constrain()`: Basic mathematical helper functions.
   
### 11. **Port and Pin Handling:**
   - Defines macros and variables for accessing hardware registers and configuring digital I/O ports efficiently. This is done using `pgm_read_byte` and `pgm_read_word` functions, which read values from the program memory of AVR microcontrollers.

### 12. **C++ Compatibility:**
   - The `#ifdef __cplusplus` block ensures that C++ compilers can use this file, with added support for Arduino classes like `WCharacter`, `WString`, and `HardwareSerial`.

### 13. **Timing and Waveform Generation:**
   - Functions like `tone()` and `noTone()` are used to generate square wave sounds on a pin.
   
### 14. **Randomness and Mapping Functions:**
   - Provides random number generation functions like `random()` and `randomSeed()`, and `map()`, which re-maps a number from one range to another.

### 15. **Pins Definitions:**
   - `pins_arduino.h` is included at the end, which provides the pin mappings for specific Arduino boards, so users can write code generically across different hardware.

### Summary:
The `Arduino.h` file provides essential macros, definitions, and function prototypes that abstract away the complexities of low-level hardware interaction on AVR-based microcontrollers. This allows developers to focus on writing higher-level logic without worrying about direct hardware access. It also supports timing, interrupts, serial communication, pin manipulation, and math utilities essential for building Arduino-based projects.

