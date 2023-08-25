#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task1 Assignment 1: String Concatenation and Formatting**


# In[5]:


fname="Hanfia"
age="30"
country="United Arab Emirates"
formatted_String="My name is " + fname + ".I am " + age + " years old and I live in "+country+ "."
print(formatted_String)


# In[ ]:


#**Assignment 2: String Formatting using `.format()`



# In[4]:


item= "phone"
quantity = 20
price = 100
total_price = price * quantity
formatted_String= "I bought {} {} at {} each ,for total of ${} ".format(quantity,item,price,total_price)
print(formatted_String)


# In[15]:


#**Assignment 3: String Interpolation using `f''`


# In[3]:


city="Karachi"
temperature="40"
formatted_String=f"The temperature in {city} is {temperature}°C."
print(formatted_String)


# In[20]:


#**Assignment 4: String Formatting using `%()`


# In[2]:


first_name="Hanfia"
last_name="Abdul Sattar"
birth_year=1995
current_year=2023
age = current_year-birth_year

formatted_string = "My name is %(first_name)s %(last_name)s. I am %(age)d years old." %{"first_name": first_name, "last_name": last_name, "age": age}

print(formatted_string)


# In[12]:


#**Assignment 5: Combining Formatting Methods**


# In[52]:


product="laptop"
discount = 12000
original_price =150000
discounted_percentage= 100 * (discount / original_price)
discount_data="Product name is "+str(product)+\
" Orignal Price is "+str(original_price) +\
" Discounted price is "+str(discount)+ \
" Discounted price in percentage "+ str(discounted_percentage)+"%"
print (discount_data)



# In[ ]:




