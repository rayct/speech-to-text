**Speech to Text Program Documentation**

**1. Introduction**
  
  The Speech to Text program is a Python application designed to convert spoken words into text. It utilizes the SpeechRecognition library, which provides support for various speech recognition APIs including Google Web Speech API, IBM Watson, and Microsoft Azure.

**2. Installation**

  Before using the program, ensure that you have Python installed on your system. Additionally, you need to install the SpeechRecognition library. You can install it using pip:

  ```
  pip install SpeechRecognition
  ```

**3. Usage**

  - **Running the Program**
    
    To run the Speech to Text program, execute the Python script containing the program code. Upon execution, the program will listen to the microphone input, recognize the speech, and print out the recognized text.

    ```
    python speech_to_text.py
    ```

  - **Interacting with the Program**
    
    The program prompts the user to speak after displaying "Listening...". Speak clearly into the microphone. After processing, it will display the recognized text. If the speech cannot be understood or there's an error during processing, appropriate messages will be displayed.

**4. Dependencies**

  - **SpeechRecognition**: This library provides support for speech recognition. It allows the program to recognize speech using various APIs.

**5. Program Structure**

  - **Importing Libraries**
    
    The program starts by importing the necessary libraries. It utilizes the `speech_recognition` library for speech recognition.

  - **Defining the Speech to Text Function**
    
    The core functionality of the program is encapsulated within the `speech_to_text` function. This function initializes the recognizer, listens to the microphone input, recognizes the speech, and returns the recognized text.

  - **Main Execution**
    
    The `__main__` block of the program calls the `speech_to_text` function and prints the recognized text if it's not None.

**6. Error Handling**

  - The program includes error handling to manage potential issues during speech recognition. It catches `UnknownValueError` when the speech cannot be understood and `RequestError` when there's an error with the speech recognition API request.

**7. Conclusion**

  The Speech to Text program provides a simple and efficient way to convert spoken words into text using Python. By leveraging the SpeechRecognition library, it offers flexibility in choosing different speech recognition APIs. The program can be easily integrated into various applications requiring speech-to-text functionality.


---

Documentation By: **Raymond C. TURNER**

**Rev:** March 1st, 2024