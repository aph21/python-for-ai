#range() -> doesn't just generates a sequence of numbers, it describes a pattern of numbers. It can be used to create lists, iterate over sequences, and more. It's a powerful tool for working with numbers in Python.
for i in range(2,6):
    print(i)
#output is: 2, 3, 4, 5.
#What number does range(2,6) generate internally? It generates the numbers 2, 3, 4, and 5. The range() function generates numbers starting from the first argument (inclusive) up to the second argument (exclusive). So in this case, it starts at 2 and goes up to but does not include 6.
#RANGE DOES NOT return a list, it returns a range object. To get a list, you can use the list() function to convert the range object into a list.
print(list(range(2,6)))  # Output: [2, 3, 4, 5]

#Difference between break and continue in loops:
#break: it is used to exit a loop permanently.when a break statement is encountered, loop terminates immediately and control is transferred to the statement following the loop.
#continue: it is used to skip the current iteration of a loop and move to next iteration when a continue statement is encountered, the rest of the code inside the loop for that iteration is skipped and control is transferred to the next iteration of the loop.
#break     → stop the loop
#continue  → skip this iteration
#break is used for successful completion of a task, while continue is used for handling exceptions or skipping unwanted iterations. or skipping the bad datasets in a loop.

#1
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
#prints 0,1,3. 
#why? because when i is 2, the continue statement is executed, which skips the rest of the code in that iteration and moves to next iteration. So 2 is skipped. when i is 4, the break statement is executed, which exits the loop immediately. so 4 is not printed and the loop terminates. Therefore, only 0, 1, and 3 are printed.



###########Nested loops - a loop inside another loop. The inner loop is executed for each iteration of the outer loop.
#Outer loop controls rows
#Inner loop runs completely for each outer iteration

#examples
#1
for i in range(1,4):
    for j in range(1,4):
        print(i * j, end=" ")
    print()

#output is:
#1 2 3  
#2 4 6
#3 6 9
#why? because the outer loop iterates through the numbers 1 to 3, and for each iteration of the outer loop, the inner loop iterates through the numbers 1 to 3. The print statement inside the inner loop multiplies the current values of i and j and prints them on the same line (due to end=" "). After the inner loop completes for each iteration of the outer loop, a new line is printed (due to print()) to separate the rows. Therefore, we get a multiplication table for numbers 1 to 3.

#2 -Grid traversal
# used heavily in algorithms that involve 2D arrays, such as pathfinding algorithms, image processing, and game development.
for row in range(3):
    for col in range(3):
        print("cell:" ,row, col)
