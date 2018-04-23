Linux file permissions 
#######################

:Date: 4 Feb 2018 
:Category: administration
:Tags: linux 
:Status: published

Linux: Chmod and Chown
======================


**Chmod: Change File Mode Bits**
-----------------------------------

.. code:: shell

    15:45:18 user@example temporary 
    total 12K
    drwxr-xr-x  2 test users 4.0K Feb  1 14:29 .
    drwx------ 33 test users 4.0K Feb  3 15:45 ..
    -rw-r--r--  1 test users    0 Jan 21 12:14 1
    -rw-r--r--  1 test users    0 Jan 21 12:14 3
    -rw-r--r--  1 test users   16 Feb  1 14:29 file.txt

In the above example output from left to right we have: filemode, number
of links, user, group, size, date last modified, name of file.

We will focus on the filemode for now.

::

    drwxr-xr-x
    0123456789 <-- this is our reference marker.

0: is either :code:`-` meaning a file, or :code:`d`` signifying that it is a
directory.

1-3: represents the user or owner of the file.

4-6: is reference to the group that owns the file.

7-9: everybody else, or other.

**Change the filemodes:**

The command :code:`chmod` is used to change the modefiles of files. Its
basic syntax is as follows:

:code:`chmod u+x file.txt` – The :code:`u` signifies :code:`user`, the :code:`+`
 means add and the :code:`x` refers to execute. This can be stacked, and used to
 takeaway permissions.

:code:`chmod -R g+rwx directory` would recursively (:code:`-R`) change all
:code:`group` files within :code:`directory` to read, write and execute.

Importantly, if the user or group **does not** own the file or directory
then the command :code:`sudo` must be used. Otherwise it is not needed.

**Octal:** In the above examples we used :code:`rwx` to note what
permissions we wanted to add or remove from a file. Another method is to
use the *octal* notation; numeral.

:code:`chmod 777 file.txt` would mean that we are giving :code:`rwx` to user,
group and other. How does 7 equal :code:`rwx`?

This is because :code:`4` gives read access, :code:`2` is write and :code:`1`,
execute. When using octal we add the numbers together, so if we wanted
read, write and execute we simply add 4,2,1 which equals 7.

:code:`chmod 765 xxx.txt` would mean: - user: read, write and execute -
group: read and write - other: read and execute

Using this is very simple, but how do I remove permissions? Previosuly,
we would :code:`chmod u-x` i.e. we used the :code:`-` to signify removal of
priviledge. Using octal we just set new filemode to what we want and it
will add or subtract the mode accordingly. An example below:

:code:`chmod a+rwx` == give read, write and execute to all (user,group a)nd
other) *or* :code:`777`.

But if we only wanted the user to have :code:`rwx` and everyone else read
and write we could call: :code:`chmod 755`. To use non-octal here would be
:code:`chmod go-x`.

Important note: As with all things linux there are many more advanced
features. We are just touching the surface here.

**Chown: Change File Owner and Group**
--------------------------------------

The :code:`chown` command deals with changing the ownership of files and
directories.

::

    drwxrwxr-x  1 test users 14.0K Jan 21 12:14 dir_1

    -rw-r--r--  1   admin   root   16 Feb  1 14:29 file.txt
    [filemode]     [owner] [grp]  

Above we have a break down of the important parts of our :code:`ls -la`
output.

In the faked output we have :code:`admin` in the first positon which is
representing the owner/ creator of :code:`file.txt`. In postition two we
have the group that :code:`file.txt` belongs to, in this case its :code:`root`.

The owner of a file can make changes to the filemode and ownsership of a
file without super user priviledges. However, if another user wanted to
change the ownership they would require this access.

To make a change is as simple as :code:`chown [user]:[group] [file/s]`.

::

    $ sudo chown root file.txt # 1.
    $ ls -l 
    -rw-r--r--  1 root root   16 Feb  1 14:29 file.txt

The simplest usage of :code:`chown` is the command plus the new owner and
file or directory to be affected.

::

    $ sudo chown -R admin dir_1 # 2.
    $ ls -l
    drwxrwxr-x  1 admin users 14.0K Jan 21 12:14 dir_1

If we wanted to make the changes to all files and directories inside a
directory we can add :code:`-R`. This is a recursive function with the same
syntax as :code:`chmod`.

::

    $ sudo chown admin:admin file.txt 
    $ ls -l
    -rw-r--r--  1 admin admin   16 Feb  1 14:29 file.txt

To specify a new owner and group the use of :code:`:` between the owner and
group can be used. :code:`admin:users`, ’root:root\` and so on.
