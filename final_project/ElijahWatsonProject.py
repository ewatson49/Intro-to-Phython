# Word Reverser 
def reverse_word():
    user_input = input("enter a word or sentence and i will reverse it!:")

    reversed_text = ""
    for x in user_input:
        reversed_text = x + reversed_text

    print("Reversed: " + reversed_text)
reverse_word()

#uses one input, has descriptive function name, prints a output, uses a for loop 