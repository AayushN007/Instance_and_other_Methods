````markdown
# Instance, Static and Class Method Example in Python

## Description
This program demonstrates the use of different types of methods inside a Python class:

1. Instance Method
2. Static Method
3. Class Method

The program creates a class named `demo` and shows how each method is called.

---

## Program Explanation

### Class: `demo`
The class contains variables and methods to demonstrate method types.

### Constructor (`__init__`)
```python
def __init__(self):
    self.a = 10
    self.b = 20
````

* The constructor is automatically called when an object is created.
* It initializes instance variables:

  * `a = 10`
  * `b = 20`

---

## Instance Method

```python
def instance_disp(self):
    print(self.a)
    x = 100
    y = 2
    print(x * y)
```

* Instance methods work with object data.
* They use `self` to access instance variables.
* Called using an object.

Example:

```python
dl = demo()
dl.instance_disp()
```

Output:

```
10
200
```

---

## Static Method

```python
def static_disp():
    print("Python")
```

* Static methods do not use `self`.
* They do not access instance variables.
* Called using the class name.

Example:

```python
demo.static_disp()
```

Output:

```
Python
```

---

## Class Method

```python
def class_disp():
    print("Python")
```

* Class methods normally work with class-level data.
* They are called using the class name.

Example:

```python
demo.class_disp()
```

Output:

```
Python
```

---

## Complete Output

```
10
200
Python
Python
```

---

## Concepts Covered

* Classes and Objects
* Constructor
* Instance Method
* Static Method
* Class Method
* Object creation

```
```
