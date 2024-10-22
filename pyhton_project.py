#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

customer_df = pd.read_csv("Customers.csv")
customer_df.head()
# churn_df = pd.read_csv("Churn.csv")


# In[5]:


customer_df.info()


# In[6]:


customer_df.describe()


# In[2]:


churn_data = pd.read_csv("churn.csv")
sbs_data = pd.read_csv("subscriptions.csv")
tran_data =pd.read_csv("transactions.csv")


# In[8]:


churn_data.head()


# In[9]:


sbs_data.head()


# In[10]:


tran_data.head()


# In[11]:


# Q: Find out first and lastname
customer_names = customer_df[['FirstName',"LastName"]]
customer_names.head()


# In[12]:


# Q2:Find out customers from north america
na = customer_df[customer_df['Region']=="North America"]
na.value_counts()


# In[13]:


# Q3: Europe and Asia people
ua = customer_df[customer_df['Region'].isin(["Europe","Asia"])]
ua


# In[14]:


# Q4: find the customers with Active Status
a = customer_df[customer_df['Status']=="Active"]
a


# In[15]:


# Q5:Visulaize active and inactive customers using pi chart(limited no go with this)

#counting Active and inActive customers
sizes_count = customer_df['Status'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(sizes_count, labels=sizes_count.index, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FF5722'])
plt.title("Active vs Inactive Customers")
plt.show()


# In[16]:


#Q6:List down customers who joined after 1 jan 2021
# Convert 'Join Date' column to datetime format
customer_df['JoinDate'] = pd.to_datetime(customer_df['JoinDate'], format='%d-%m-%Y')
after_jan21 = customer_df[customer_df['JoinDate']>"2020-01-01"]
after_jan21


# In[17]:


# Q7:create bar chart after and before 2021-01-01

customer_df['JoinDate'] = pd.to_datetime(customer_df['JoinDate'], format='%d-%m-%Y')

# Filter customers who joined before and after Jan 1, 2021
before_2021 = customer_df[customer_df['JoinDate'] < "2021-01-01"]
after_2021 = customer_df[customer_df['JoinDate'] >= "2021-01-01"]


# Count the number of customers in each group
counts = [len(before_2021),len(after_2021)]

# Create a bar chart
labels = ['Before 2021-01-01', 'After 2021-01-01']

plt.figure(figsize=(8,6))
bars=plt.bar(labels, counts, color=['#FF5722', '#4CAF50'])
# Add title and labels
plt.title('Customer Join Dates: Before and After 2021-01-01')
plt.xlabel('Time Period')
plt.ylabel('Number of Customers')


# Add numbers on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), 
             ha='center', va='bottom', fontsize=12)

# Display the chart
plt.show()


# In[18]:


#List down active customer from Europe
Europe_ct = customer_df[(customer_df["Status"]=="Active") & (customer_df["Region"]=="Europe")]

print(len(Europe_ct))


# In[19]:


#Show Active customer and InActive customer in Europe
Active = customer_df[(customer_df["Status"]=="Active") & (customer_df["Region"]=="Europe")]
InActive = customer_df[(customer_df["Status"]=="Inactive") & (customer_df["Region"]=="Europe")]

counts =[len(Active),len(InActive)]
label=["Active","InActive"]

plt.figure(figsize=(8,6))
plt.pie(counts,labels=label,colors=["blue","green"],autopct='%1.1f%%')
plt.title("Active vs Inactive Customers in Europe")
plt.show()


# In[20]:


## Q7:create bar chart who joined in 2021 and not

customer_df['JoinDate'] = pd.to_datetime(customer_df['JoinDate'], format='%d-%m-%Y')

# Filter customers who joined before and after Jan 1, 2021
in_2021 = customer_df[customer_df['JoinDate'].dt.year == 2021]
not_2021 = customer_df[customer_df['JoinDate'].dt.year != 2021]

counts= {"in_2021":len(in_2021),"not_2021":len(not_2021)}

# print(counts)
plt.figure(figsize=(8,6))
plt.bar(counts.keys(),counts.values(),color=["red", 'yellow'])
plt.xlabel("Joined Date")
plt.ylabel("Customers")
#add number to the each bar
for i, (key, value) in enumerate(counts.items()):
    plt.text(i, value + 0.10, str(value), ha='center', va='bottom', fontsize=12)

plt.show()


# In[26]:


# calculate avg transation amount

tran_data.head()
avg = tran_data['Amount'].mean()
avg


# In[43]:


# with respect index how transation amount varing
tran_data.head()

#line plot
# Plotting transaction amount with respect to the index
plt.figure(figsize=(10,6))
plt.plot(tran_data.index,tran_data["Amount"],linewidth=2)
plt.xlabel("index")
plt.ylabel("Amount")
plt.title("Varianace amount with respect to index")
plt.grid(True)
plt.show()


# In[44]:


#scatter plot
# Plotting transaction amount with respect to the index 
plt.figure(figsize=(10,6))
plt.scatter(tran_data.index,tran_data["Amount"],linewidth=2)
plt.xlabel("index")
plt.ylabel("Amount")
plt.title("Varianace amount with respect to index")
plt.grid(True)
plt.show()


# In[45]:


#How many trans more than 100k
more100k= tran_data[tran_data["Amount"]>100]
more100k


# In[56]:


# using pie chart showing % breakdown above 100k and below or equal to 100k

more100k= tran_data[tran_data["Amount"]>100]
below100k= tran_data[tran_data["Amount"]<=100]

label_counts = {"morethan100k":len(more100k),"below100k":len(below100k)}
print(label_counts)

plt.figure(figsize=(10,6))
plt.pie(label_counts.values(),labels=label_counts.keys(),autopct='%1.1f%%', startangle=90)
plt.title('Percentage Breakdown of Transaction Amounts Above and Below/Equal to 100k')
plt.show()


# In[65]:


more100k= tran_data[tran_data["Amount"]>100]
below100k= tran_data[tran_data["Amount"]<=100]

label_counts = {"morethan100k":len(more100k),"below100k":len(below100k)}
print(label_counts)

plt.figure(figsize=(10,6))
plt.bar(label_counts.keys(),label_counts.values(),color=['blue', 'green'])
plt.xlabel('Transaction Amount Category')
plt.ylabel('Count')
plt.title('Breakdown of Transaction Amounts Above and Below/Equal to 100k')
#add number to the each bar
for i, (key, value) in enumerate(label_counts.items()):
    plt.text(i, value + 0.10, str(value), ha='center', va='bottom', fontsize=12)
plt.show()


# In[78]:


import matplotlib.pyplot as plt

# Filter the data based on the amount condition
more100k = tran_data[tran_data["Amount"] > 100]
below100k = tran_data[tran_data["Amount"] <= 100]

# Create the scatter plot
plt.figure(figsize=(10, 6))

# Plotting the points for transactions above 100k
plt.scatter(more100k.index, more100k["Amount"], color='blue', label='More than 100k', alpha=0.7)

# Plotting the points for transactions below or equal to 100k
plt.scatter(below100k.index, below100k["Amount"], color='green', label='Below or equal to 100k', alpha=0.7)

plt.axhline(y=100, color='red', linestyle='--', label='Threshold (100k)')

# Adding labels and title
plt.xlabel('Transaction Index')
plt.ylabel('Transaction Amount')
plt.title('Scatter Plot of Transaction Amounts')

# Adding a legend
plt.legend()

# Display the plot
plt.show()


# In[80]:


import matplotlib.pyplot as plt
import seaborn as sns

# Create a new column for categorization
tran_data['AmountCategory'] = tran_data['Amount'].apply(lambda x: 'Above 100k' if x > 100 else 'Below or Equal 100k')

# Set the color palette
palette = {'Above 100k': 'green', 'Below or Equal 100k': 'blue'}

# Create the scatter plot using Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tran_data, x=tran_data.index, y='Amount', hue='AmountCategory', palette=palette, alpha=0.7)

# Adding a horizontal line at y = 100
plt.axhline(y=100, color='black', linestyle='--', label='Threshold (100k)')

# Adding labels and title
plt.xlabel('Transaction Index')
plt.ylabel('Transaction Amount')
plt.title('Scatter Plot of Transaction Amounts')
plt.legend()

# Display the plot
plt.show()


# In[85]:


# find most recent transations
tran_data.head()
most_recent_transactions = tran_data.sort_values(by='TransactionDate', ascending=False)
most_recent_transactions


# In[89]:


#find reason for leaving customers
churn_data.head()
churn_data["Reason"].value_counts()


# In[5]:


#visulation of churn customer and not churn
totalcust=customer_df.shape[0]
churncust=churn_data.shape[0]
notchurncust=totalcust-churncust

label_counts = {"Churn":churncust,"NotChurn":notchurncust}
print(label_counts)

plt.figure(figsize=(10,6))
plt.bar(label_counts.keys(),label_counts.values(),color=['blue', 'green'])
plt.xlabel('Customer Status')
plt.ylabel('Count')
plt.title('Churn and not churn customer data')
#add number to the each bar
for i, (key, value) in enumerate(label_counts.items()):
    plt.text(i, value + 0.10, str(value), ha='center', va='bottom', fontsize=12)
plt.show()


# In[8]:


plt.figure(figsize=(10,6))
plt.pie(label_counts.values(),labels=label_counts.keys(),autopct='%1.1f%%')
plt.show()


# In[13]:


# List churn date with reason of service

service = churn_data[churn_data['Reason'].str.contains('service',case=False,na=False)]
service


# In[21]:


# join customer and subscription 

merged_df = pd.merge(customer_df, sbs_data, on='CustomerID', how='inner')
merged_df


# In[28]:


# Visulization for different customer groups [Active-Monthly, InActive-Monthly, Active-Annual, InActive Annual ]

merged_df = pd.merge(customer_df, sbs_data, on='CustomerID', how='inner')
# Create a new column 'Group' that combines 'Status' and 'PlanType'
merged_df['Group'] = merged_df['Status'] + '-' + merged_df['PlanType']
# Count the number of customers in each group
group_counts = merged_df['Group'].value_counts()

# Visualization: Pie chart for different groups
plt.figure(figsize=(5, 5))
plt.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette('Set1', len(group_counts)))
plt.title('Customer Distribution by Subscription Status and Plan Type', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[ ]:




