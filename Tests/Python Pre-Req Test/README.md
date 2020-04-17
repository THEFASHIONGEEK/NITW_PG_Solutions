# Python Pre-Req Test

<a id="1"></a>
## MCQS
#### 1.Which one of the following is NOT a built-in function in Python?
- float()
- chr()
- bool()
- int()
- **None of the Above**

#### 2.Which of the following is a valid statement that prints the path of an user-defined module?
- **```modulename.__file__```**
- ```modulename.__filepath__```
- ```modulename.__path__```
- None of the above

#### 3.In the following code, what is the type of variable 'a'?
```
import numpy as np
a = np.array([[1, 2], [3, 4]])
```
- Single dimensional array
- **Multi-dimensional array**
- List
- Dictionary

#### 4.What will be the output if we execute the following?
```
print(5.0==5)
```
- FALSE
- **TRUE**
- Syntax Error
- Runtime Error

#### 5.In Python, indentation of a code block is denoted by line indentation.
- **TRUE**
- FALSE

#### 6.What will be the output of the given program segment, where we are trying to reassign s2 with another string, which is an immutable data type?
```
s1 = "two"
s2 = "three"
s3 = " one"
s2 = "one"
print(s2)
```
- Runtime Error
- Compile Time error
- three
- **one**

#### 7.In OOP, which of the following is true when a derived class inherits a base class privately?
- Public members of the base class become private members of the derived class.
- Private members of the base class are not inherited.
- Protected members of the base class become private members of the derived class.
- **All of these**

#### 8.For the following code, what would be the output:
```
list=["US","China","Russia"]
print('US' in list)
```
- ['US', 'China', 'Russia']
- ['US']
- TRUE
- None of the above
 
 #### 9.Which one of the following is NOT a valid statement in Python?
 - random.randrange(stop)
 - random.randrange(start, stop[, step])
 - **random.randrange([, step])**
 
 #### 10.In OOP,  which of the following is a synonym for function overloading?
 - **Virtual polymorphism**
 - Transient polymorphism
 - Ad-hoc polymorphism
 - Psuedo polymorphism
 
 #### 11. What is the output of the following code snippet?
 ```
 list1 = {1,2,3,4}
list2 = {3, 4, 5, 6}
print(list1 & list2,list1-list2)
 ```
- **{3, 4} {1, 2}**
- {1, 2} {3, 4}
- [1, 2] [3, 4]
- Error as these operations are not applicable on list

#### 12. What is the output of the following code snippet?
```
import datetime
date1 = datetime.date("2019", "5", "20")
print(date1, end=";")
```
- 20-05-2019;
- 2019-05-20;
- 05-20-2019;
- **Error**

#### 13.What will the following code segment print?
```
def student_percentage(subject_marks):
    Test_marks= subject_marks
    Max_marks = 10
    print(Test_mark, end = "," ) 
    return Test_marks/Max_marks*100

student1 = student_percentage(5)
print(student1)
```
- 5,50.0
- 5,50
- **Error**
- 5,0.5

#### 14.Find out which of the following statement will return the string - EDUREKA
- 
```
str1 = "YEADWUURAEAKSA"
print(str1[len(str1):0:2])
```
- 
```
str1 = "YEADWUURAEAKSA"
print(str1[len(str1):0:-2])
```
- 
```
str1 = "YEADWUURAEAKSA"
print(str1[len(str1):0:-2][::1])
```
-
**```str1 = "YEADWUURAEAKSA"
print(str1[len(str1):0:-2][::-1])```**

#### 15.What is the output of the following statements:
```
s1="EDUREKA"
s1[0:4:-1]
```
- EDUR
- ERUD
- **Empty string**
- Error
