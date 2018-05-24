Base64 ELI5
###########

:Date: 22 May 2018
:Status: Published
:Tags: ELI5
:Category: linux, ELI5

=======
Base64
=======

I thought I understood Base64. I mean its the alphabet in upper and lowercase plus
numbers and a couple characters. But, what I didn't know was how the 64 bits worked, like
thats missing a whole extra two bits. Why?

TL;DR
======

Base64 is a binary to ASCII encoding that takes a byte (8 bits) and chunks its
down into segments of 6 bits - six ones in binary equates to 64 which is where it 
derives its name. 

Let's look at an example using the three letter word "The".

.. code:: bash

        #ascii       T (84)        h (104)       e (101) <-- ASCII plus base10 number
        #binary   01010100      01101000     01100101    <-- three bytes
        #base64   010101    000110    100001   100101    <-- four segments of six bits


Given the base64 binary digits we calculate the number for each segment.

.. code:: bash

        #base64   010101    000110    100001   100101    
        #total      21        06        33       37

So now that we've split the 8 bit binary down to 6, and found what that equals in
base10 we can consult the base64 conversion table.

------

.. figure:: {filename}/images/base64.png
    :alt: Base64 Conversion Table


------

By cross referencing the binary representation of the four segments (21, 06, 33, 37)
we get the ASCII characters; :code:`VGhl`.

Gotcha's
---------

In the example we used a three byte word which can neatly be broken down into four 
segments of six. What if the word is four characters, or 32 bits? 32 / 6 is 5 with a 
remainder of 2.

In that case we need to pad out the base64 to indicate that the last segment is not 
complete.

The base2 decimal representation of "Them" is :code:`84 104 101 109` or 
:code:`VGhlbQ==` in base64. As you can see there is two :code:`=` symbols tacked on 
to the end. This indicates that there is two empty segments of 6 bits at the end of
the encoding. 

.. code:: bash  

        #ascii       T (84)        h (104)       e (101)     m (109)
        #binary   01010100      01101000     01100101      01101101
        #base64   010101    000110    100001   100101   001101  010000
        #total      21        06        33        37      13      16 

Looks like that works out perfectly, so where does the extra two segments of zero's
come in that generates the :code:`=`'s? 

The segementing of eight bits into six bits cannot delimit half way between a byte.
Meaning the base64 encoding must continue until there is no remainder. Let's explore 
this again using just one character.

.. code:: bash

        #ascii       M (77)        
        #binary   01011101   00000000   00000000   
        #base64   010111  010000  000000  000000   
        #total      19      16      00      00  

I chose the letter 'M' as it is easier to explain than 'T'. Looking at it you can see
that even with only one byte, it takes three bytes for base64's segments of six to
equally divide. Hence, this is why the letter 'M' in base64 would be padded with
:code:`==` to indicate as such. This example uses two equals signs but base64 can also 
be padded with just one. It all depends on how many segments extra are needed to 
generate a zero remainder.

More overhead
--------------

Astute readers will see that using base64 requires more overhead than hexadecimal or
binary. So why use it? Base64's genesis was in MIME (Multipurpose Internet Mail Extensions)
where large streams of text are used to send emails and attachments. The problem is that
streaming binary, or hexadecimal could of had unintended consequences as some systems
or programs may interpret certain globs incorrectly. For instance, a null byte in some
systems may indicate that the message has ended when in fact it has not. 


More information?
-----------------

As always `Wikipedia <https://en.wikipedia.org/wiki/Base64>`_ has an excellent page
on Base64. 


