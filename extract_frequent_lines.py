import collections

def extract_frequent_lines(input_file, output_file, repetitions, encoding='utf-8'):
    line_counts = collections.Counter()
    
    # Read the input file and count occurrences of each line
    with open(input_file, 'r', encoding=encoding) as file:
        for line in file:
            line_counts[line.strip()] += 1
    
    # Sort the lines based on their occurrences (most frequent first)
    sorted_lines = sorted(line_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Filter the lines based on the desired number of repetitions
    frequent_lines = [line for line, count in sorted_lines if count >= repetitions]
    
    # Write the frequent lines to the output file
    with open(output_file, 'w', encoding=encoding) as file:
        for line in frequent_lines:
            file.write(line + '\n')

if __name__ == '__main__':
    input_file = 'input.txt'  # Replace 'input.txt' with the path to your input file
    output_file = 'frequent_lines.txt'  # Replace 'frequent_lines.txt' with the desired output file name
    repetitions = int(input("Enter the minimum number of repetitions: "))
    extract_frequent_lines(input_file, output_file, repetitions)
    print(f"Frequent lines with at least {repetitions} repetitions have been saved to '{output_file}'.")
