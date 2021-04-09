# Software Engineering Principles

### What are the principles we used?
 - DRY (Don't Repeat Yourself)
 - KISS (Keep it Simple Stupid)
 - Decorators
 - Top-Down Thinking

### Where and why did we use the principles?

<h4> Db.py </h4>

- We created a file called db.py, which has all the functions that deal with the database which enables us to call these functions every time instead of copying code and repeating ourselves
- previously, we did ____ stored in another branch
- The reason why we changed it for this iteration is so that we didn't have to continuously copy the code, and instead we imported the file instead which addresses DRY
- In addition, it also reduces design smells such as rigidity (code is difficult to change) and fragility (changing one thing has a high chance of breaking the project). This is because since all our functions and test files use the database and without the db.py, we would have to copy and paste it for all our files. This means that if we need to update our database or change the structure, we need to go through each file individually to change it. For our project, there would always be new updates which we would need to consider hence this file was extremely helpful and also incorporates top-down thinking.
- Lastly, this also ensures that if we want to change a database system in the future, it will be much easier to do this, since we will just have to change the code that in db.py and return the same outputs as before, so all the other functions and files can remain how they are.

<h4> auth_login & auth_register </h4>

- In both of these functions, we wrote some helper functions such as hash_password/check_email
- This was used so that our code would be more readable and utilises KISS as by having these functions, we would break down a bigger task into smaller functions so that our code would easier to understand and read.
- this mainly addresses opacity (difficult to understand) as we are abstracting by removing characteristics and reducing it from a high level component to something smaller.
- previously, our code was much harder to read as there were more steps in the process and it was harder to follow without the helper functions.

<h4> Decorators (db.py) </h4>

- allow us to add functionality to a function without altering the function itself, by "decorating" (wrapping) around it.
- The functions we used it for are to collects all of something from the database, like all channel_ids or all message_ids, in order to make sure a channel id or message id that is provided from the frontend is a valid id.

```
def from_db(func):
    def wrapper(*args, **kwargs):
    f = func(*args, **kwargs)
        return [value[f[0]] for value in f[2][f[1]]]
    return wrapper
```

```
@from_db
def get_all_channels(data):
    return ('channel_id', 'channels', data)
```

```
@from_db
def get_all_messages(data):
    return ('message_id', 'messages', data)
```
<h4>._include.py </h4>
- a file created for this iteration that is called in all of our tests
- the reason why we did this was so that for all our tests, we need to import the function we're testing 
e.g. from auth_register import auth_register 
     from token.py import generate_token
     we also include all our global functions and libraries in here
- by having this ._include.py file we are ensuring our code doesn't repeat and we are applying top-down thinking and DRY
- this is so that if in the future, we need to change our code we don't have to individually open each test file and instead, we can just change our ._include.py
- we are refactoring (restructing but doesn't change external behaviour) our code so that it will be easier to modify in the future, as well as making it more clean and simple to read/understand. This addresses design smells like rigidity and fragility.  

<h4>message_react & message_pin</h4>
- files that are really similiar and look like they repeat themselves
- In consideration of DRY, we tried our best to not repeat the same code in each function
- We came up with new ways to test the functions, and tried to make use of the differences we found in the coverage report