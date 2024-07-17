### Topic - Bit Magic

#### binary represent -ve numbers
* Two's complement is used to binary represent -ve numbers
### Two's complement
* Get the one's complement of number 
* Add one to it 


#### Bitwise Operators in Python
* Decimal has numbers - 0 to 9
* Binary has numbers - 0 and 1
* In Python we can use below functions - [bin(), int(<binary_rep>,base)]
* **0b** is python prefix for binary numbers

```python
>>> bin(20)
'0b10100'
>>> int('0b10100',2)
20
```

#### Bitwise AND: &
* If two bit are one then one else 0
6   : 1 1 0
3   : 0 1 1
------------
6&3 : 0 1 0 

```Python
>>> c = 6
>>> d = 3
>>> c&d
2
```

#### Bitwise OR: |
* **Rule:** If one bit is one then one else 0
6   : 1 1 0
3   : 0 1 1
------------
6|3 : 1 1 1 

```python
>>> c = 6
>>> d = 3
>>> c|d
7
```

#### Bitwise XOR: ^
* **Rule:** If two input are same then output is 0 else 1 . 
6   : 1 1 0
3   : 0 1 1
------------
6|3 : 1 0 1 

```python
>>> c = 6
>>> d = 3
>>> c^d
5
```

#### Left Shift Operator : << 
* **Rule:** Add number of zero from the left side .
* Multiplying by power of 2

#### Left Shift Operator : >>
* **Rule:** Add number of zero from the right side .
* Last bit is removed 
* Deviding by power of two 

#### Bitwise Not : ~