#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[4]:


matches = pd.read_csv('matches.csv')
matches.head()


# In[6]:


matches.shape


# In[7]:


matches.describe()


# In[8]:


matches.info()


# In[14]:


#1.How many matches we've got in the dataset

matches['id'].max()


# In[13]:


#2.How many seasons we've got in the dataset?

uniqueseasons= matches['season'].unique()
len(uniqueseasons)


# In[19]:


#3.most successful teams based on the number of wins

team_wins = matches['winner'].value_counts()

team_wins.head()


# In[20]:


#3.wins by runs and wickets

# Set the style for the plots
sns.set(style="whitegrid")

# Plotting the distribution of wins by runs
plt.figure(figsize=(12, 6))
sns.histplot(matches['win_by_runs'], bins=30, kde=True, color='blue')
plt.title('Distribution of Wins by Runs', fontsize=14)
plt.xlabel('Win by Runs', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

# Plotting the distribution of wins by wickets
plt.figure(figsize=(12, 6))
sns.histplot(matches['win_by_wickets'], bins=11, kde=True, color='green')
plt.title('Distribution of Wins by Wickets', fontsize=14)
plt.xlabel('Win by Wickets', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()


# In[21]:


#Wins by Runs: 
#The majority of the matches have been won by a margin of fewer than 50 runs, with a sharp decline as the run margin increases.
#Wins by Wickets: 
#Most matches are won by a margin of 6 to 10 wickets, indicating that teams often achieve their target with plenty of wickets remaining.


# In[24]:


#4.impact of winning the toss on match outcomes.

# Creating a new column to check if the toss winner also won the match
matches['toss_and_match_win'] = matches['toss_winner'] == matches['winner']


toss_impact = matches['toss_and_match_win'].value_counts(normalize=True) * 100

# Display the results
toss_impact


# In[27]:


#5. Most "Player of the Match" Awards


# Finding the players with the most "Player of the Match" awards
player_awards = matches['player_of_match'].value_counts().head(10)

# Display the top 10 players with the most awards
print(player_awards)

# Plotting the data for better visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=player_awards.values, y=player_awards.index, palette='viridis')
plt.title('Top 10 Players with Most "Player of the Match" Awards', fontsize=14)
plt.xlabel('Number of Awards', fontsize=12)
plt.ylabel('Player', fontsize=12)
plt.show()


# In[29]:


# 6: City Analysis

# Finding the cities that have hosted the most matches
city_counts = matches['city'].value_counts()

# Display the top 10 cities with the most matches hosted
print(city_counts.head(10))

# Plotting the data for better visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=city_counts.values, y=city_counts.index, palette='coolwarm')
plt.title('Top 10 Cities with Most Matches Hosted', fontsize=14)
plt.xlabel('Number of Matches', fontsize=12)
plt.ylabel('City', fontsize=12)
plt.show()


# In[31]:


# 7: Venue Success Rate

# Finding the venues with the most matches played
venue_counts = matches['venue'].value_counts().head(10)

# Display the top 10 venues with the most matches hosted
print(venue_counts)

# Plotting the data for better visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=venue_counts.values, y=venue_counts.index, palette='Set2')
plt.title('Top 10 Venues with Most Matches Hosted', fontsize=14)
plt.xlabel('Number of Matches', fontsize=12)
plt.ylabel('Venue', fontsize=12)
plt.show()

# the most successful team at the top venue
top_venue = venue_counts.index[0]
top_venue_data = matches[matches['venue'] == top_venue]
top_team_at_venue = top_venue_data['winner'].value_counts().head(1)

# Display the most successful team at the top venue
print(f"The most successful team at {top_venue} is:")
print(top_team_at_venue)


# In[40]:


# 8: Seasonal Analysis - Most Successful Teams in Each Season
# Finding the most successful team in each season
season_winner = matches.groupby('season')['winner'].value_counts().unstack().idxmax(axis=1)

# Display the most successful teams in each season
print("Most Successful Teams in Each Season:")
print(season_winner)

# Plotting the most successful team in each season for visualization
plt.figure(figsize=(14, 7))
sns.countplot(data=matches, x='season', order=matches['season'].sort_values().unique(), hue='winner', palette='Paired')
plt.title('Most Successful Teams by Season', fontsize=14)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Number of Wins', fontsize=12)
plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



# Finding the most "Player of the Match" awards in each season
season_best_player = matches.groupby('season')['player_of_match'].value_counts().unstack().idxmax(axis=1)

# Display the best players in each season
print("\nBest Players in Each Season:")
print(season_best_player)


# In[41]:


# 10: Match Outcome by Venue
# Grouping by venue and winner to count the number of wins for each team at each venue
venue_win_counts = matches.groupby(['venue', 'winner']).size().unstack(fill_value=0)

# Display the venue win counts for better understanding
print("Number of Wins by Venue and Team:")
print(venue_win_counts)

# Plotting the data as a heatmap for better visualization
plt.figure(figsize=(12, 8))
sns.heatmap(venue_win_counts, 
            annot=True,                # Show counts in cells
            fmt='d',                   # Format as integers
            cmap='YlGnBu',            # Color scheme from yellow to green to blue
            cbar_kws={'label': 'Number of Wins'})  # Color bar label
plt.title('Match Outcome by Venue', fontsize=14)
plt.xlabel('Winning Team', fontsize=12)
plt.ylabel('Venue', fontsize=12)
plt.show()


# In[42]:


# Analysis: Distribution of Match Winners
# Count the number of wins for each team
winner_counts = matches['winner'].value_counts()

# Display the counts of wins
print("Number of Wins by Each Team:")
print(winner_counts)

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(winner_counts, 
        labels=winner_counts.index, 
        autopct='%1.1f%%',  # Display percentage on the pie chart
        startangle=140,     # Start angle for the pie chart
        colors=sns.color_palette('pastel'),  # Use a pastel color palette
        wedgeprops={'edgecolor': 'black'})  # Add a black edge around slices

plt.title('Distribution of Match Winners', fontsize=14)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()


# In[ ]:




