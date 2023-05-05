# Task 3: Beginner Control Structures

This programme introduces validation. The user is asked to input their full name. If they enter at least two names then the programme runs as expected and ends.
```
What is your full name?

John Smith

Thank you for entering your name.
```

If no input is given, then the following output is given:

```
What is your full name?

You haven't entered anything. Please enter your full name.
```

If less than 4 characters are given as input, then the following output is given.

```
What is your full name?

J S

You have entered less than 4 characters. Please make sure that you have entered your name and surname.
```

If more than 25 characters are given as input, then the following output is given.

```
What is your full name?

Andrew Brian Charlie David Elliot Frank Gary Harry Jack 

You have entered more than 25 characters. Please make sure that you have only entered your full name.
```

If only one name is given as input, then the following output is given.

```
What is your full name?

John

You must enter both your first name and your surname.
```
