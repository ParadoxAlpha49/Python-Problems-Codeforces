# Input the number of problems
n = int(input())

# Initialize a counter for the number of problems they will implement
implement_count = 0

# Loop through each problem's input
for _ in range(n):
    # Read the input for each friend's certainty
    petya, vasya, tonya = map(int, input().split())
    # Check if at least two friends are sure about the solution
    if petya + vasya + tonya >= 2:
        implement_count += 1

# Output the count of problems they will implement
print(implement_count)
