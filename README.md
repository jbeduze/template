# template
Here are the basics to creating a mean looking streamlit app, no longer are you restricted to boring UIs, because regardless of how well it works, pretty things are more appealing to the audience, so let's make them pretty!

This repo will serve as a template for what you can do, and I'll try and put as many notes as possible for every component I have in here too!

**Commenting out:**
---

Python code commenting out:
---
-You only have to put a hashtag (#) in front of the string you want commented out

-to comment out multiple lines of code at once use: ctrl + /
    

        #Commented out item
            and
        #multiple lines hashed out 1
        #multiple lines hashed out 1
        #multiple lines hashed out 1
CSS code commenting out:
---
-You have to surround the commented out string with /*str*/ to comment out items
    
        /*commented out item*/

---
Creating "docstrings" or descriptions of use in python
    -this can include the functions purpose, parameters and output
    -example:
        
    def new_function():
        """
        This function prints a message indicating that it is a new function.
        """
        print("This is a new function")

    #Calling the function to see the output
    new_function()