# Grading

## General Grading notes

- remove all instances of "%YOUR ANSWER HERE%" from answers


## Helper functions

check_output(acceptable_answers: list, strip: bool, ignore_case: bool)

## Short Answer

### fitb_1

Description: Using two statements, complete the definition of the function swapints that is passed two int variables. The function returns nothing but exchanges the values of the two variables.

```
void swapints(int &a, int &b) {
int temp = a;
[ANSWER HERE]
}
```

a=1,b=2 => swampints() => a==2,b==1
a=7,b=-8 => swampints() => a==-8,b==7


### fitb_2

Description: Write a function addOne() that adds 1 to its integer reference parameter. The function returns nothing.

```
addOne (int& x) {
    [ANSWER HERE]
}
```

a=0 => addOne(a) => a==1
a=1 => addOne(a) => a==2

Notes:
- Some responses start with "void ", most do not

### fitb_3

Description: Complete the definition of the function absoluteValue such that it receives an integer parameter and returns the absolute value of the parameter's value.

```
int absoluteValue(int num1) {
    [ANSWER HERE]
    return absoluteValue;
}
```

absoluteValue(-2) -> 2
absoluteValue(0) -> 0
absoluteValue(1) -> 1


### fitb_4

Description: Complete the for loop such that it prints the odd integers 11 through 121 inclusive, separated by spaces.

```
for (int i = 11; i <= 121; [ANSWER HERE]") {
    cout << i << " " ;
}
```

f() => check_output([" ".join([str(x) for x in range(11, 122)])], strip=True, ignore_case=True) 



### fitb_5

Description: Complete the definition of a function isSenior, that receives an integer parameter and returns true if the parameter's value is greater or equal to 65, and false otherwise.

```
bool isSenior(int age) {
    [ANSWER HERE]
}
```

isSenior(64) -> false
isSenior(65) -> true
isSenior(66) -> true


#### fitb_6

Description: Write a for loop that prints the integers 1 through 40, separated by spaces or new lines. You may use only one variable, count which has already been declared as an integer.

```
int count = 1; // This line must be put into the test file
for ([ANSWER HERE]) {
    cout << count << " ";
}
```

f() => check_output([" ".join([str(x) for x in range(1, 40)]), "\n".join([str(x) for x in range(1, 40)])], strip=True, ignore_case=True) 


### fitb_7

Description: Write the definition of a function min that has two int parameters and returns the smaller.

```
int min (int num1, int num2) {
    [ANSWER HERE]
}
```

min(1,2) -> 1
min(2,1) -> 1
min(1,1) -> 1


### fitb_8

Description: Given an int variable k that has already been declared, use a for loop to print a single line consisting of 97 asterisks. Use no variables other than k.

```
int k = 0; // This line must be put into the test file
for ([ANSWER HERE]) {
    cout << "*";
}
```

f() => check_output(['*'*97], strip=True, ignore_case=True) 


### fitb_9

Description: Complete the assignment of the variable isFailing such that it is set to true if exam_score is less than 50, and false otherwise.

```
int exam_score;
cin >> exam_score;
bool isFailing = [ANSWER HERE];
if (isFailing) {
    cout << "You failed!" << endl;
} else {
    cout << "You passed!" << endl;
}
```

49 >> f() => check_output(["You failed!"], strip=True, ignore_case=True)
50 >> f() => check_output(["You passed!"], strip=True, ignore_case=True)
51 >> f() => check_output(["You passed!"], strip=True, ignore_case=True)


### fitb_10

Description: Using one expression, complete the function notDivisibleByThree that returns false if x is divisible by three, and true otherwise.

```
bool notDivisibleByThree(int x) {
    return [ANSWER HERE];
}
```

notDivisibleByThree(0) -> false
notDivisibleByThree(1) -> true
notDivisibleByThree(2) -> true
notDivisibleByThree(3) -> false


### fitb_11

Description: Given that an array of int named a has been declared with 12 elements and that the integer variable k holds a value between 0 and 6. Assign 9 to the element just after a[k].

```
// k = 4
a[[ANSWER HERE]] = 9;
// return a[k+1] == 9
```

f() -> true


### fitb_12

Description: Complete the if/else statement such that it assigns true to the variable fever if the variable temperature is greater than 98.6; otherwise it assigns false to fever.

```
if (temperature > 98.6) {
    [ANSWER HERE]
} else {
    fever = false;
}
// return fever
```

f(98.5) -> false
f(98.6) -> false
f(99.7) -> true


### fitb_13

Description: Complete the definition of a function max that has three int parameters and returns the largest.

```
int max(int x,int y,int z) {
    if (x > z && x > y) {
        return x;
    } else if ([ANSWER HERE]) {
        return y;
    } else {
        return z;
    }
}
```

max(1,2,3) -> 3
max(2,3,1) -> 3
max(3,1,2) -> 3
max(3,2,3) -> 3


### fitb_14

Description: Given two 3x5 2D arrays of integer, x1 and x2, write the code needed to copy every value from x1 to its corresponding element in x2.

```
// x1 = 
// x2 = 
for(int i = 0; i < 3; i++){
    for(int j = 0; j < 5; j++){
        [ANSWER HERE]
    }
}

/*
for(int i = 0; i < 3; i++){
    for(int j = 0; j < 5; j++){
        if x1[i][j] != x2[i][j]{
            return false;
        }
    }
}
return true;
*/
```

f() -> true


### fitb_15

Description: You are given a 6x8 (6 rows, 8 columns) array of integers, x, already initialized and three integer variables: max, i and j. Write the necessary code so that max will have the largest value in the array x.

```
// x =
max = x[0][0];
for(i = 0; i < 6; i++){
    for(j = 0; j < 8; j++){
        if([ANSWER HERE]){
            max = x[i][j];
        }
    }
}
// return x == [predefined largest num]
```

f() -> true


### fitb_16

Description: Complete the switch statement to output 'Moo!' when the value of animal is 'cow'

```
switch(animal) {
    case "pig":
        cout << "Oink!" << endl;
        break;
    case "hen":
        cout << "Cluck!" << endl;
        break;
    [ANSWER HERE]
}
```

f("cow") => check_output(["Moo!"], strip=True, ignore_case=True)


### fitb_17

Description: Complete the definition of a function fibonacci so that for input n it prints the nth fibonacci number. Ex: fibonacci(6) -> 8, fibonacci(1) -> 1, fibonacci(2) -> 1.
```
int fibonacci(int n) {
    [ANSWER HERE]
    else if (n == 1) 
        return 1; 
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

fibonacci(2) -> 1
fibonacci(8) -> 21


### fitb_18

Description: Complete the function isPalindrome that checks if a given string is a palindrome. A palindrome is a word that is spelled the same backwards such as "mom". Input: "mom" Output: true

```
bool isPalindrome(string str) {
    int left = 0;
    int right = [ANSWER HERE];
    while (left < right) {
        if (str[left++] != str[right--]) {
            return false;
        }
    }
    return true;
}
```

isPalindrome("a") -> true
isPalindrome("aaaaaaaaaaaa") -> true
isPalindrome("wow") -> true
isPalindrome("hi") -> false
isPalindrome("helloworld") -> false



### fitb_19

Description: Complete the capitalize_first_letter function to capitalize the first letter of each word in a given string. When given a character, touper will output the character capitalized. Input: "hello world" output: "Hello World"

```
string capitalize_first_letter(string text) {
    for ([ANSWER HERE]){
        if (x == 0 || text[x - 1] == ' '){
             text[x] = toupper(text[x]); 
            } 
        } 
     return text; 
}
```

capitalize_first_letter("my name is") -> "My Name Is"
capitalize_first_letter("a") -> "A"
capitalize_first_letter(" HeLLo earth ") -> " HeLLo Earth "


### fitb_20, 

Description: Complete a C++ program to calculate x raised to the power y (x^y). Input: x = 7 y = 2 Output: 49

```
int power(int x, int y) {
    if (y == 0) {
        return 1;
    } else if (y == 1) {
        return x;
    }

    int tmp = power([ANSWER HERE]);
    tmp = tmp * tmp;
    if (y % 2 == 1) {
        return x * tmp;
    } else {
        return tmp;
    }
}
```

power(2, 4) -> 16
power(10, 3) -> 1000
power(1, 15) -> 1
power(3, 12) -> 531441


### fitb_21


Description: Complete a C++ program to multiply two integers without using multiplication, division, bitwise operators, and loops. Sample Input: 8, 9 Sample Output: 72 Input: -11, 19 Output: -209

```
int multiply_two_nums(int x, int y) {
    if (y == 0) 
        return 0;
    if (y > 0) 
        return (x + multiply_two_nums(x, y - 1));
    if (y < 0) 
        return [ANSWER HERE];
}
```

multiply_two_nums(1, -1) -> -1
multiply_two_nums(0, -4) -> 0
multiply_two_nums(4, -5) -> -20



### fitb_22

Description: Complete a function "reverseString" where the output returns string s reversed. Input: "apple" Output: "elppa"

```
string reverseString(const string &str) {
    string reversedStr;
    for (int i = 0; i < str.length(); ++i) {
        reversedStr += str[[ANSWER HERE]];
    }
    return reversedStr;
}
```

reverseString("a") -> "a"
reverseString("abcde") -> "edcba"



### fitb_23

Description: Complete the function "digit_sum" so that the function returns the sum of the digits of a number. Input: 10, Ouput: 1

```
int digit_sum(int value) {
    int result = 0;
    while (value > 0) {
        result += value % 10;
        value = [ANSWER HERE];
    }
    return result;
}
```

digit_sum(1) -> 1
digit_sum(123) -> 6


### fitb_24

Description: Complete the function "triangle" so that the output looks like a triangle made up of value of "*" input: 5  Output: 
*****
****
***
**
*

```
void triangle(int value) {
    for (int i = value; i > 0; i--) {
        for ([ANSWER HERE]) {
            std::cout << '*';
        }
        std::cout << std::endl;
    }
    return;
}
```

triangle(1) => check_output(["*"], strip=True, ignore_case=True)
triangle(3) => check_output(["***\n**\n*"], strip=True, ignore_case=True)


## Long Answer


### fr_2

Description: Clunker Motors Inc. is recalling all vehicles in its Extravagant line from model years 1999-2002. Given an int modelYear and a string modelName, print 'RECALL' if modelYear and modelName match the recall details

f(1999, "Extravagant")  =>  check_output(["RECALL"], strip=True, ignore_case=True)
f(2000, "Extravagant")  =>  check_output(["RECALL"], strip=True, ignore_case=True)
f(2002, "Extravagant")  =>  check_output(["RECALL"], strip=True, ignore_case=True)
f(1998, "Extravagant")  =>  check_output([""], strip=True, ignore_case=True)
f(2003, "Extravagant")  =>  check_output([""], strip=True, ignore_case=True)

f(1998, "Not-Extravagant")  =>  check_output([""], strip=True, ignore_case=True)
f(1999, "Not-Extravagant")  =>  check_output([""], strip=True, ignore_case=True)
f(2000, "Not-Extravagant")  =>  check_output([""], strip=True, ignore_case=True)
f(2002, "Not-Extravagant")  =>  check_output([""], strip=True, ignore_case=True)
f(2003, "Not-Extravagant")  =>  check_output([""], strip=True, ignore_case=True)

#### Grades

O327: Pass
5ZCK: None
A23A: Pass
A3RT: Fail
ACHS: Fail
BUB4: Pass
D5ZT: Pass
DOGU: Fail
G5XR: Fail
H0VK: Fail
IOON: Fail
J21O: Pass
J3QN: Pass
L7QH: Fail
LIF8: Pass
M4QP: Pass
M6YD: Fail
NY50: Fail
P6XQ: Pass
PA20: Fail
Q7MD: Fail
RB3Z: Fail
TN3S: Fail
V7CR: Fail
X2VR: Fail
X4TN: Fail
X8LP: Pass
Y2JN: Fail


Template:
```
#include <iostream>
#include <string>

using namespace std;

void f(int modelYear, string modelName) {

}

int main()
{
    f(1999, "Extravagant"); // RECALL
    f(2000, "Extravagant");  // RECALL
    f(2002, "Extravagant");  // RECALL
    f(1998, "Extravagant");
    f(2003, "Extravagant");

    f(1998, "Not-Extravagant");
    f(1999, "Not-Extravagant");
    f(2000, "Not-Extravagant");
    f(2002, "Not-Extravagant");
    f(2003, "Not-Extravagant");
}
```

### fr_3

Description: Write a statement that toggles the value of the bool variable onOffSwitch. That is, if onOffSwitch is false, itsvalue is changed to true; if onOffSwitch is true, its value is changed to false

f(true) -> false
f(false) -> true


### fr_4

Description: Write the definition of a function isPositive() that receives an integer n as a parameter and returns true if the parameter is positive and false otherwise

f(1) -> true
f(25) -> true
f(-1) -> false
f(-104) -> false

### fr_5

Description: Implement a function is_sorted() that accepts a vector of integer values and returns true if it is non-decreasing, and false otherwise

std::vector<int> v = {1, 1, 1, 1};
is_sorted(v) -> true
std::vector<int> v = {1, 2, 3, 4};
is_sorted(v) -> true
std::vector<int> v = {4, 3, 2, 1};
is_sorted(v) -> false


### fr_6

Description: Given a string, s, and an integer, x, update s such that its characters are shifted by x. Ex. s = 'cd', x = 1. Loop results in s = 'de'

f("ab", 1) -> "bc"
f("ab", 2) -> "cd"
f("ab", 3) -> "de"



### fr_7

Description: Given integer variables amount and total both initialized to 0, write a loop that reads in values for amount from standard in and adds them to total until total is greater than 100.


Manually Grade this one


### fr_8

Description: Implement a function containsDuplicate() that accepts a vector (called vec_list) of integers and returns true if it contains a duplicate element, and false otherwise


std::vector<int> v = {1, 1, 1, 1};
containsDuplicate(v) -> true
std::vector<int> v = {1, 2, 3, 4};
containsDuplicate(v) -> false
std::vector<int> v = {4, 3, 2, 4};
containsDuplicate(v) -> true



### fr_9

Description: Implement a function secondGreatest() that accepts a vector of integers, called vector_num, and returns the second greatest element in the vector


std::vector<int> v = {0, 1, 1, 1};
secondGreatest(v) -> 0
std::vector<int> v = {1, 2, 3, 4};
secondGreatest(v) -> 3
std::vector<int> v = {4, 3, 2, 4};
secondGreatest(v) -> 3


### fr_10

Description: Implement a function countdown() that accepts an integer n as a parameter and counts down from n, printing each number to standard output, separated by a space. After reaching 1, print 'liftoff!'


countdown(5) =>  check_output(["5 4 3 2 1 liftoff!", "5 4 3 2 1liftoff!", "5 4 3 2 1 0 liftoff!", "5 4 3 2 1 0liftoff!"], strip=True, ignore_case=True)
countdown(3) =>  check_output(["3 2 1 liftoff!", "3 2 1liftoff!", "3 2 1 0 liftoff!", "3 2 1 0liftoff!"], strip=True, ignore_case=True)
countdown(1) =>  check_output(["1 liftoff!", "1liftoff!", "1 0 liftoff!", "1 0liftoff!"], strip=True, ignore_case=True)



### fr_11

Description: Write the definition of the function factorial() where it ouputs the factorial of non-negative integer n when given n as input. Input: 5, Output: 120

factorial(1) -> 1
factorial(4) -> 24


### fr_12

Description: Write a function called isPrime() that recieves a integer n as a parameter and returns True if n is a prime number and false otherwise. (e.g., 7 is a prime number)

isPrime(8) -> false
isPrime(11) -> true


### fr_13

Description: Write the definition of a fucntion isEven() so that it returns True or False if the int n is even or not


isEven(6) -> true
isEven(7) -> false


### fr_14

Description: Write a function called sphere_volume() that can return the volume of a sphere when given a radius described as int r. Volume of a sphere is caluculted by the following function: V = (1/3) 4 * pi * r^3 where V is volume, pi is 3.14, and r is the radius


sphere_volume(3) -> 113.04


### fr_15


Description: Write a simple function called find_mean() that recives an array of numbers, callled array_num, as a parameter. The function should return the mean of those numbers. Input: { 2, 2, 3, 10 }, Output: 4.27


int nums[5] = {0, 0, 0, 0, 0}
find_mean(nums) -> 0
int nums[5] = {1, 2, 3, 4, 5}
find_mean(nums) -> 3
