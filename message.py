
class Message:
    welcome = "Welcome to Pitchfinder!"
    enter_freq = "\nEnter a frequency in Hz: "
    back_to_main = "\nGoing back to the main loop..."
    bye = "\nGoodbye!\n"
    invalid_freq = "\nInvalid value for a frequency."

    @classmethod
    def info(cls, x, y):
        str1 = "\nEnter a frequency in Hz to find the closest note,"
        str2 = f" or F to change the reference frequency for the note {x} "
        str3 = f"(current value: {y} Hz), or X to quit."
        return str1 + str2 + str3

    @classmethod
    def closest(cls, a, b, c, d):
        return f"\nClosest note to {a} Hz: {b} ({c} Hz), {d} cents difference."

    @classmethod
    def prompt_a4(cls, x, y):
        str1 = f"\nEnter the new frequency for {x}"
        str2 = f" (current value: {y} Hz), or press X to cancel: "
        return str1 + str2
    
    @classmethod
    def a4_set(cls, x, y, z):
        return f"\nFrequency for {x} set from {y} Hz to {z} Hz. \n{cls.back_to_main}"
    
    @classmethod
    def a4_out_of_range(cls, x, y, z): 
        str1 = "\nThe value you've entered is out of range. "
        str2 = f"The frequency of {x} must be between {y} Hz and {z} Hz."
        return str1 + str2
    