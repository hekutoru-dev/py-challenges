import os

# Import Directory.
main_path = os.path.join('..', 'TextPars')

# List files in Directory for analysis
# The script asks the user to select the file to analyse by a menu number
print("\n===== FILES TO ANALYSE =====")

try:
    filelist = os.listdir(main_path)
    for file in range(len(filelist)):
        print (f'->  {file} - {filelist[file]}  <-')
    selection = input("Select the NUM of the file you want to analysis: ")
    
    
    
    
    # Select the file to analysis
    text_file = filelist[int(selection)]
    filepath = os.path.join('..', 'TextPars', text_file)
    
    # Initialize counters.
    count_letters = 0
    count_words = 0
    count_sentence = 0
    
    # Open the file in "read" mode ('r') and store the contents in the variable "text"
    with open(filepath, 'r') as paragraph:
        # Store all of the text inside a variable called "lines"
        lines = paragraph.read()
        
        # Count words, letters and sentences using fors and conditionals.
        for letter in range(len(lines)):
            if lines[letter] != " " and lines[letter] != "-":            
                if lines[letter] == "." or lines[letter] == "?" or lines[letter] == "!":
                    count_sentence += 1
                elif lines[letter] != "," and lines[letter] != "'" and lines[letter] != '"' \
                 and lines[letter] != "(" and lines[letter] != ")":
                    count_letters += 1                
            else:
                count_words += 1    
        
    # Results
    avg_letter_per_word = count_letters/count_words
    avg_sentence_lenght_words = count_words/count_sentence
    
    print ("Paragraph Analysis")
    print ("-----------------------------")
    print (f'Approximate Word Count: {count_words}')
    print (f'Approximate Sentence Count: {count_sentence}')
    print (f'Average Letter Count: {avg_letter_per_word}')
    print (f'Average Sentence Length: {avg_sentence_lenght_words}')
    print (f'Approximate Letter Count: {count_letters}')
    
    # Define an Output path and a filename for that output.
    output_file = os.path.join("..", "Outpath", "Paragraph Analysis.txt")
    
    with open(output_file,"w") as file:
        
        # Write methods to print to Financial Analysis.
        file.write("Paragraph Analysis\n")
        file.write("----------------------------\n")
        file.write(f'Approximate Word Count: {count_words}\n')
        file.write(f'Approximate Sentence Count: {count_sentence}\n')
        file.write(f'Average Letter Count: {avg_letter_per_word}\n')
        file.write(f'Average Sentence Length: {avg_sentence_lenght_words}\n')
        file.write(f'Approximate Letter Count: {count_letters}\n')
except:
    print("\n!!! FILE DOES NOT EXIST !!!")