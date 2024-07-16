### Topic - Bit Magic

#### binary represent -ve numbers
* Two's complement is used to binary represent -ve numbers
 


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

```Python
>>> c = 6
>>> d = 3
>>> c|d
7
```