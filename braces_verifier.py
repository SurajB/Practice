
# Defining braces check list
braces_check_list = {
    "{": "}",
    "[": "]",
    "(": ")"
}

# Enter the input json/braces pattern
input_pattern = input("Enter the input pattern to verify: ")
print("Input pattern: %s" %(input_pattern))

# Strip off the spaces from the input
input_pattern = input_pattern.replace(" ", "")
print(input_pattern)

# Fetch the length of the input pattern
length_pattern = len(input_pattern)

# If length of the input pattern is not even, return False
if length_pattern%2 is not 0:
    print("The number of opening braces and closing braces does not match")
    print(False)

# Split the input braces pattern into a list
pattern_array = [char for char in input_pattern]

print("Pattern in array: ")
print(pattern_array)

# Loop through the pattern list and compare the pattern matching
for i in range(0, (length_pattern//2)):

    forward_check = i
    backward_check = length_pattern-1

    if braces_check_list[pattern_array[forward_check]] != pattern_array[backward_check]:
        final_flag = False
        print(final_flag, ": The pattern doesn't match at position: %d and %d of the array" %(forward_check+1, backward_check+1))

        break

    length_pattern -= 1

    final_flag = True

if final_flag:
    print(final_flag, ": The pattern check has been successful ")
