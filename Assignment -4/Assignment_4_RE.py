#!/usr/bin/env python
# coding: utf-8

# In[122]:


import re


# # Assignment 1: Extracting Phone Numbers
# Raw Text: Extract all valid Pakistani phone numbers from a given text.
# 
# Example:
# 
# Text: Please contact me at 0301-1234567 or 042-35678901 for further details.

# In[134]:


text="Please contact me at 0301-1234567 or 042-35678901 for further details."
pattern=r"\d{3,4}[-]\d{7,8}"
mob_data=re.findall(pattern, text)
print(mob_data)


# ### Assignment 2: Validating Email Addresses
# Raw Text: Validate email addresses according to Pakistani domain extensions (.pk).
# 
# Example:
# 
# Text: Contact us at info@example.com or support@domain.pk for assistance.

# In[35]:


text="Contact us at info@example.com or support@domain.pk for assistance."

pattern= r"\w+[@]\w+\.pk"
email_data=re.findall(pattern, text)
print(email_data)


# # Assignment 3: Extracting CNIC Numbers
# Raw Text: Extract all Pakistani CNIC (Computerized National Identity Card) numbers from a given text.
# 
# Example:
# 
# Text: My CNIC is 12345-6789012-3 and another one is 34567-8901234-5.

# In[17]:


text="My CNIC is 12345-6789012-3 and another one is 34567-8901234-5."
pattern=r"\d{5}[-]\d{7}[-]\d{1}"

cnic_data= re.findall(pattern,text)
print(cnic_data)


# # Assignment 4: Identifying Urdu Words
# Raw Text: Identify and extract Urdu words from a mixed English-Urdu text.
# 
# Example:
# 
# Text: یہ sentence میں کچھ English words بھی ہیں۔

# In[184]:


text="""
 یہ sentence میں کچھ English words بھی ہیں۔
"""

urdu_pattern =r'[\u0600-\u06FF]+'
urdu_words = re.findall(urdu_pattern, text)

for word in urdu_words:
    print(word)


# # Assignment 5: Finding Dates
# Raw Text: Find and extract dates in the format DD-MM-YYYY from a given text.
# 
# Example:
# 
# Text: The event will take place on 15-08-2023 and 23-09-2023.

# In[117]:


text=" The event will take place on 15-08-2023 and 23-09-2023."
pattern=r"\d{1,2}[-]\d{1,2}[-]\d{2,4}"
date_data=re.findall(pattern, text)
print(date_data)


# # Assignment 6: Extracting URLs
# Raw Text: Extract all URLs from a text that belong to Pakistani domains.
# 
# Example:
# 
# Text: Visit http://www.example.pk or https://website.com.pk for more information.

# In[155]:


import re
text= """Visit http://www.example.pk or https://website.com.pk for more information."""
pattern= r"https?://\w+\.\w+[.pk]"
domain_pk=re.findall(pattern, text)
print(domain_pk)


# In[ ]:


# Assignment 7: Analyzing Currency
Raw Text: Extract and analyze currency amounts in Pakistani Rupees (PKR) from a given text.

Example:

Text: The product costs PKR 1500, while the deluxe version is priced at Rs. 2500.


# In[92]:


text=" The product costs PKR 1500, while the deluxe version is priced at Rs. 2500."
pattern= r"PKR.\d+" 
pattern1=r"Rs.+\d+"
rupee= re.findall(pattern1,text) + re.findall(pattern,text) 
print(rupee)


# # Assignment 8: Removing Punctuation
# Raw Text: Remove all punctuation marks from a text while preserving Urdu characters.
# 
# Example:
# 
# Text: کیا! آپ, یہاں؟

# In[144]:


text =" کیا! آپ, یہاں؟"
res = re.sub(r'[^\w\s]', '', text)
print(res)


# # Assignment 9: Extracting City Names
# Raw Text: Extract names of Pakistani cities from a given text.
# 
# Example:
# 
# Text: Lahore, Karachi, Islamabad, and Peshawar are major cities of Pakistan.

# In[169]:


text=" Lahore, Karachi, Islamabad, and Peshawar are major cities of Pakistan."
pattern = r"\b(Lahore|Karachi|Islamabad|Peshawar|Multan)\b"

cities= re.findall(pattern,text)
print(cities)


# # Assignment 10: Analyzing Vehicle Numbers
# Raw Text: Identify and extract Pakistani vehicle registration numbers (e.g., ABC-123) from a text.
# 
# Example:
# 
# Text: I saw a car with the number plate LEA-567 near the market.

# In[116]:


text="""I saw a car with the number plate LEA-567 near the market."""
pattern= r"\w+[-]\d+"
car_num=re.findall(pattern,text)
print(car_num)


# In[ ]:




