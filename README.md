# Home-Automation-System
This is the source code for a home automation system to control various aspects of my room and home. The system is mostly written in Python with a webpage interface written in HTML and PHP. Currently the only hardware components being used are 3 relay modules a light sensor module based on a light dependent resistor, an HC-SR04 ultrasonic module and a LM34 analog temperature sensor. Right now the system only controls my window air condition unit but will later control my TV and lamp. The system uses the HC-SR04 ultrasonic module to detect when door is closed and ensures the the AC is only on when it is. The system is also capable of remotely turning my AC on/off from a button of the webpage interface. The user can also set the desired temperature for the AC hysteresis on the webpage interface. The system also includes a temperature database from measurements taken every 20mins that can be accessed on a webpage. The temperature database interface webpage also displays the current, max, min and average temperatures. 


