# brainfuck

Labeled as one of the hardest programming languages on the market.<br/>
It's a language that you can keep quite simple and you can also torture yourself.

## Grid
We utilize a horizontal grid consisting of 30k cells, where the default value of each cell is zero.

![image](https://user-images.githubusercontent.com/14398606/206283242-4c5924e3-4690-40d9-bc95-3334bd8af4bb.png)


## Rule set
Standard brainfuck supports 8 different operators.

<b>Note:</b> Every character that is not shown below is ignored by the interpreter.

#### Navigation
```
* > - Moves one cell to the right
* < - Moves one cell to the left
```

#### Mathematical operators
```
* + - Increment the current cell's value by one
* - - Decreases the current cell's value by one
```

#### I/O
```
* . - Prints the value in the current cell, per default we will always try to print it in char form over integer
* , - Takes a char input from the user
```

#### Loops
```
* [ - Enter the while loop if the current cell's value isn't zero, else jump over the while statement
* ] - Exits the while loop if the current cell's value is zero, else jump to the start of the while statement
```

<b>Note:</b> This interpreter does not support while loops that span over multiple lines nor does it support while loops inside of while loops

## Code examples

#### Hello World!

`Hello World!` in brainfuck can be easy and it can be very hard. <br/>
Shown below is a medium example of how you can print the classical message.
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<.
```
