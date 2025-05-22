#!/usr/bin/env python
# coding: utf-8

# ### How do you concatenate two strings in Python?

# String concatenation is the process of combining two or more strings into a single string. 

# In[24]:


string1 = "My name"

string2 = "is Gaurav"

print(string1+ " " + string2)


# ###  What is the difference between the + operator and the join() method for concatenating strings?

# The + operator and the join() method both concatenate strings, but they differ in efficiency and how they handle multiple 
# strings.
# 
# #### + Operator:
# This operator directly adds strings together. It is simple for concatenating a few strings. However, it becomes inefficient when concatenating a large number of strings, especially within loops. 
# 
# 
# #### join() Method:
# This method is specifically designed for concatenating multiple strings, particularly from an iterable (like a list or tuple). It takes an iterable of strings as input and joins them into a single string, using the string on which it is called as a separator. It is more efficient than the + operator for large numbers of strings because it creates only one new string object.

# In[16]:


#Join()
my_list = ['Kush','sharma',"@","gamail.com"]

seprator = "."

print(seprator.join(my_list))


# In[25]:


# +Operator
string1 = "My name"

string2 = "is Gaurav"

print(string1+ " " + string2)


# ### How do you access individual characters in a string?

# Individual characters in a Python string can be accessed using indexing, with the index starting at 0 for the first character. Square brackets are used to specify the index of the character to be accessed. Negative indexing can also be used, where -1 refers to the last character, -2 to the second last, and so on. Attempting to access an index outside the valid range will raise an IndexError.

# In[27]:


my_string = "Kush"
print(my_string[0])  
print(my_string[3]) 
print(my_string[-2]) 


# ### What method is used to find the length of a string in Python?

# In Python, the len() function is used to determine the length of a string. This function counts the number of characters, including spaces and special characters, within the string. It returns an integer value representing the string's length. 

# In[32]:


my_string = "Python is most important language in data science"
len(my_string)


# ### How can you convert a string to uppercase in Python?

# To convert a string to uppercase in Python, the upper() method can be used. This method does not require any arguments and returns a new string where all lowercase characters have been converted to uppercase. The original string remains unchanged.

# In[40]:


string = "My name is kush and i am learning data science"
print(string.upper())


# ### How can you convert a string to lowercase in Python?

# To convert a string to lowercase in Python, the lower() method is used. This method returns a new string where all uppercase characters have been converted to lowercase. The original string remains unchanged.

# In[41]:


string = "MY NAME IS KUSH AND I AM LEARNING DATA SCIENCE"
print(string.lower())


# ### What method is used to replace substrings within a string?

# The primary method used to replace substrings within a string is the replace().This method searches for a specific substring and replaces it with a new one, returning a new string with the replacements. 

# In[44]:


My_string = "My name is kush and i am learning data science"
print (My_string.replace("data science", "python"))


# ### How can you split a string into a list of substrings based on a delimiter?

# To split a string into a list of substrings based on a delimiter, you can use the split() method in Python. The split() method takes a delimiter as an argument and returns a list of substrings separated by that delimiter. 

# In[59]:


My_string = "My name is kush and i am learning data science"
print(My_string.split(" "))


# ### How do you check if a string starts with a particular substring?

# startswith() method in Python checks whether a given string starts with a specific prefix. It helps in efficiently verifying whether a string begins with a certain substring, which can be useful in various scenarios like:
# 
# 1. Filtering data
# 2. Validating input
# 3. Simple pattern matching

# In[60]:


My_string = "My name is kush and i am learning data science"
print(My_string.startswith("name"))


# In[61]:


My_string = "My name is kush and i am learning data science"
print(My_string.startswith("My"))


# ### How do you check if a string ends with a particular substring?

# To determine if a string ends with a particular substring, you can use the endswith() method in Python. This method takes the substring as an argument and returns True if the string ends with it, and False otherwise. 

# In[71]:


#if-else method
My_string = "My name is kush and i am learning AI"
string1 = "AI"
if string.endswith("learning"):
    print("The string ends with", string1)
else:
    print("The string does not end with", string1)


# In[72]:


My_string = "My name is kush and i am learning AI"
string.endswith("AI")


# In[73]:


My_string = "My name is kush and i am learning AI"
string.endswith("learning")


#  ### How can you remove leading and trailing whitespace from a string?

# Python's built-in strip() method is used to remove leading and trailing whitespace from a string. Whitespace includes spaces, tabs, and newline characters.

# In[87]:


My_string = "    My name is kush and i am learning AI   \n"
print(My_string.strip())


#  ### What method is used to find the index of the first occurrence of a substring within a string?
# 

# In Python, the find() method is used to find the index of the first occurrence of a substring within a string. This method returns the index of the starting position of the substring if found, and -1 if the substring is not present in the string. 

# In[89]:


My_string = "My name is kush and i am learning AI"
print(My_string.find("i am learning AI"))


# ### How can you count the number of occurrences of a substring within a string?

# To count the occurrences of a substring within a string, you can use the count() method in Python. This method takes the substring as an argument and returns the number of times it appears in the string. 

# In[92]:


My_string = "My name is kush and i am learning AI"
sub_string = "i"
print(My_string.count(sub_string))


# ### How do you check if a string contains only alphabetic characters?

# The isalpha() method can be used to determine if a string consists solely of alphabetic characters (A-Z, a-z). It returns True if all characters in the string are letters and False otherwise, including when the string is empty.

# In[98]:


My_string = "My name is kush and i am learning AI"
print(My_string.isalpha())


# ### How do you check if a string contains only numeric characters?

# To check if a string contains only numeric characters in Python, the isnumeric() method can be used. This method returns True if all characters in the string are numeric, and False otherwise. 

# In[101]:


My_string1 = "12345"
My_string2 = "123ab"
print(My_string1.isnumeric()) 
print(My_string2.isnumeric())


# ### How can you check if a string is a palindrome?

# To determine if a string is a palindrome, you can reverse the string and compare it to the original. If the reversed string matches the original, the string is a palindrome. 

# In[111]:


My_string = "malayalam"

if My_string == My_string[::-1]:
    print("Yes")
else:
    print("No")


# ### How can you reverse a string in Python?

# This slicing method is one of the simplest and an efficient method to reverse a string. It is easy to remember and best suited for reverse the string quickly.

# In[113]:


My_string = "My name is kush and i am learning AI"
rev = My_string[::-1]
print(rev)


# ### How do you format a string with placeholders for variable values?

# To format a string with placeholders for variable values, you can use placeholder syntax like {} (in Python), %s, %d, etc. (in Java, Python), or f-strings (in Python). The specific method and syntax may vary depending on the programming language, but the general concept is to insert values into a string where placeholders indicate where the values should be inserted. 

# In[117]:


name = "Rohan"
age = 28
message = "My name is name and my age is age"
message3 = "my name is {} and my age is {}".format(name,age) # {}.format method used
print(message3)


# In[116]:


name = "Rohan"
age = 28
message = "My name is name and my age is age"
message2 = f"My name is {name} and my age is {age}" # f string method used
print(message2)


# ### How do you access a substring of a string using slicing?

# In[126]:


My_string = "My name is kush and i am learning AI"
print(My_string[0:18])


# ### How can you remove specific characters from a string in Python?

# To remove specific characters from a string in Python, methods like replace() and translate() can be employed. The replace() method substitutes all occurrences of a specified character or substring with another, including an empty string to effectively remove it.

# In[151]:


My_string = "My, name, is, kush, and, i, am, learning, AI"
new_string = My_string.replace(",", "")
print(new_string) 


# In[ ]:





# In[ ]:





# In[ ]:




