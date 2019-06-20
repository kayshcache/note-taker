# Error Handling

You may remember when we were checking to see if the user input was a number or a string. 
If we tried to cast (convert type) from a string to an integer we would get an error if the string wasnt just a simple number.
(E.g. it was "23ab" instead of just "23").

We can't always predict whether code will execute without error- but we can handle errors. We can choose to look out for specific kinds of errors, or erros we have not expected; then decide what actions to proceed with when an error has occured.

You may remember the syntax for if statements:

```python
if x > y:
  do this() # this will be done if x is greater than y.
else:
  do that() # Otherwise that will be done.
```

Try/except is very similar

```python
try:
  potentially_buggy_thing()
except Exception as err:
  print(err)
print('Done')
```

This code will attempt to run `potentially_buggy_thing`, if any error occurs, then it will instead run `print(err)` and continue with printing done.
There are a range of different types of errors, see https://docs.python.org/3/tutorial/errors.html. This means you can handle multiple different exceptions. A nice summry can be found at https://www.w3schools.com/python/python_try_except.asp.

Now try rewriting a function which takes two numbers from the user and adds them together; however make it so that their inputs are converted to integers inside of the try/except structure. Think about what you will do if the user inputs invalid information.

## Challege:
Write a note-taking application. It must:
Step 1.
- Have a main menu where you can select to `[N]ew note` or  `[V]iew note`.
- New note allows you to enter the title, then contents of a new note
- View note should give you a numbered list of existing notes and their titles
- You should be able to view a note by typing a number.

Step 2.
- Extend it to have `[I]mport note` where you can type a filename and it will add that note.
- Make sure that if you add the wrong file, the error is handled. (The program doesnt crash)

Step 3.
- Save notes so that .md or .txt files are created to store each note.
- Make the program open up notes from the last time you were using it.

NOTE: Tomorrow we are going to be looking at linting. Try to write according to the pep8 style guide, as we will be coming back to this code tomorrow in order to "refactor" it to meet the pep8 standards.
