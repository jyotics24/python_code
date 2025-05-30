# Bubble Sort with Dry Run
numbers = []
n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nBefore sorting:", numbers)
print("\n--- Starting Bubble Sort Dry Run ---")
# Bubble Sort with dry run
for i in range(n):
    print(f"\nPass {i + 1}:")
    for j in range(n - 1):
        print(f"  Comparing {numbers[j]} and {numbers[j + 1]}", end=" ")
        if numbers[j] > numbers[j + 1]:
            # Swap if the left number is bigger
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            print(f"=> swapped ->{numbers}")
        else:
            print("=> no change")
    print(f"  Result after pass {i + 1}: {numbers}")

print("\n--- Bubble Sort Completed ---")
print("After sorting:", numbers)
