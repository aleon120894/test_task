What did the sensor say?

_Ajax_ sensors are wireless, running on batteries for up to 7 years, so they have to transmit their data in high
packed structures.
For example, with four bytes of information a sensor can hold information on 10 of its parameters. The sensor sends a
packet to the
hub with the data (hereinafter "payload") `27C7011D`,
hub must decode this set of bytes and provide already processed data for all 10 parameters, in next form:

```
{'field1': 'High',
 'field10': '00',
 'field2': '00',
 'field3': '00',
 'field4': '10',
 'field5': '01',
 'field6': '01',
 'field7': '01',
 'field8': 'Very Low',
 'field9': '01'}
```

The parameters structure in the sensor can be represented as:

```
# Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2, sett_byte3, sett_byte4]
device_settings = [
    {
        0: [3, 'field1'],
        3: [1, 'field2'],
        4: [1, 'field3'],
        5: [3, 'field4']},
    {
        0: [1, 'field5'],
        1: [1, 'field6'],
        2: [1, 'field7'],
        3: [3, 'field8'],
    },
    {
        0: [1, 'field9'],
        5: [1, 'field10']
    },
    {}
]
```

This is a list of bytes (4) in which each bit corresponds to some parameter (the first element in the list of the
corresponding
bit). Some parameters can use more than one bit, e.g. `field1`, it uses 3 bits, which is indicated by a zero
element in the list of the corresponding bit. For parameters that take more than 1 bit in the payload, the following
variables:

```
field1 = {
    '0': 'Low',
    '1': 'reserved',
    '2': 'reserved',
    '3': 'reserved',
    '4': 'Medium',
    '5': 'reserved',
    '6': 'reserved',
    '7': 'High',
}
field4 = {
    '0': '00',
    '1': '10',
    '2': '20',
    '3': '30',
    '4': '40',
    '5': '50',
    '6': '60',
    '7': '70',
}
field8 = {
    '0': 'Very Low',
    '1': 'reserved',
    '2': 'Low',
    '3': 'reserved',
    '4': 'Medium',
    '5': 'High',
    '6': 'reserved',
    '7': 'Very High',
}
```

For example, the parameter `field4`, which uses 3 bits, in the bitmask equals `011`, which in the decimal system equals
`3`, so it follows that the `field4` parameter is `30`.

Task:

1. Write a function that will decode the payload from the sensor and return the values of all parameters.

Check
data: `payload = "27C7011D"`, the function should return the structure:

```
{'field1': 'High',
 'field10': '00',
 'field2': '00',
 'field3': '00',
 'field4': '10',
 'field5': '01',
 'field6': '01',
 'field7': '01',
 'field8': 'Very Low',
 'field9': '01'}
```

2. Write a test for this function using `pytest`. Test receives a payload and the expected result. The test should be
   parameterized with several options.

------

Note from me: I have avoided using strings (as a data type) in places where I consider it pointless/irrational
