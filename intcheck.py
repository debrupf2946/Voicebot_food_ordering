from test2 import speech_recog
from order import check_sp

number_spellings = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine",
    "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine",
    "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine",
    "fifty", "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine",
    "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five", "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine",
    "seventy", "seventy-one", "seventy-two", "seventy-three", "seventy-four", "seventy-five", "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine",
    "eighty", "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five", "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine",
    "ninety", "ninety-one", "ninety-two", "ninety-three", "ninety-four", "ninety-five", "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine",
    "one hundred"
]

# Function to convert spelled-out numbers to integers
def convert_spelled_numbers_to_int(text):
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24, "twenty-five": 25,
    "twenty-six": 26, "twenty-seven": 27, "twenty-eight": 28, "twenty-nine": 29, "thirty": 30,
    "thirty-one": 31, "thirty-two": 32, "thirty-three": 33, "thirty-four": 34, "thirty-five": 35,
    "thirty-six": 36, "thirty-seven": 37, "thirty-eight": 38, "thirty-nine": 39, "forty": 40,
    "forty-one": 41, "forty-two": 42, "forty-three": 43, "forty-four": 44, "forty-five": 45,
    "forty-six": 46, "forty-seven": 47, "forty-eight": 48, "forty-nine": 49, "fifty": 50,
    "fifty-one": 51, "fifty-two": 52, "fifty-three": 53, "fifty-four": 54, "fifty-five": 55,
    "fifty-six": 56, "fifty-seven": 57, "fifty-eight": 58, "fifty-nine": 59, "sixty": 60,
    "sixty-one": 61, "sixty-two": 62, "sixty-three": 63, "sixty-four": 64, "sixty-five": 65,
    "sixty-six": 66, "sixty-seven": 67, "sixty-eight": 68, "sixty-nine": 69, "seventy": 70,
    "seventy-one": 71, "seventy-two": 72, "seventy-three": 73, "seventy-four": 74, "seventy-five": 75,
    "seventy-six": 76, "seventy-seven": 77, "seventy-eight": 78, "seventy-nine": 79, "eighty": 80,
    "eighty-one": 81, "eighty-two": 82, "eighty-three": 83, "eighty-four": 84, "eighty-five": 85,
    "eighty-six": 86, "eighty-seven": 87, "eighty-eight": 88, "eighty-nine": 89, "ninety": 90,
    "ninety-one": 91, "ninety-two": 92, "ninety-three": 93, "ninety-four": 94, "ninety-five": 95,
    "ninety-six": 96, "ninety-seven": 97, "ninety-eight": 98, "ninety-nine": 99, "one hundred": 100
    }

    # Split the text into words
    words = text.split()

    # Check if each word is a spelled-out number and replace it with the corresponding digit
    for i in range(len(words)):
        if words[i].lower() in number_words:
            words[i] = number_words[words[i].lower()]

    # Join the words back together and return the result
    return ' '.join(words)

# Initialize the recognizer
#recognizer = sr.Recognizer()

# Record audio from the microphone
#with sr.Microphone() as source:
#    print("Say a number:")
#    audio = recognizer.listen(source)

#try:
    # Recognize the speech
    #spoken_text = recognizer.recognize_google(audio)
def quant_recog():
    spoken_text_pre=speech_recog()
    spoken_text=spoken_text_pre.strip(".")
#=check_sp(med)
#print(med)
    print(spoken_text)
    if not any(word in check_sp(spoken_text.strip(".!").lower()) for word in number_spellings):
        integer_value = int(spoken_text)
        print("Recognized integer:", integer_value)
        return integer_value
# Check if the recognized text contains spelled-out numbers
    else:
        converted_text = convert_spelled_numbers_to_int(spoken_text.strip())
        print("Spelled-out number detected and converted:", converted_text)
        integer_value = int(converted_text)
        print("Integer value:", integer_value)
        return integer_value
#except sr.UnknownValueError:
#    print("Could not understand the audio")
#except sr.RequestError as e:
 #   print(f"Could not request results; {e}")
#except ValueError:
 #   print("Could not convert to an integer")

