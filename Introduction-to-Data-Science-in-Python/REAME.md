# Introduction to Data Science in Python
### Course 1 of the Applied Data Science in Python Specialization

**Course Description:**
The course introduces data manipulation and cleaning techniques using the python pandas data science library and introduces the abstraction of the DataFrame as the central data structure for data analysis. The course ends with a statistics primer, showing how various statistical measures can be applied to pandas DataFrames. By the end of the course, students are able to take tabular data, clean it,  manipulate it, and run basic inferential statistical analyses.


### Description of the assignments

**Some comments:**
The assignments were completed on Python using the Jupiter Notebook. They are saved as .ipynb files.


**Assignment 2**

*Part 1*

The first part of this assignment works with the All Time Olympic Games Medals dataset obtained from https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table

IDENTIFICATION: First, we identify the country with the highest number of gold medals. We then find the country with the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count. 

USING POINTS SYSTEM: We assign 3 points to each gold medal, 2 points to each silver medal and 1 point to each bronze medal. From there, we calculate the points attained by each country.

*Part 2* 

The second part of this assignment uses US Census Data. The table includes demographic data by each county of each state. 

SIMPLIFYING: We simplify the table to show the demographic data by state, by combining the data of all the counties of each state using groupby. Then, we identify the states with the largest populations. 

QUERYING: We find which county has had the largest absolute change in population within the period 2010-2015. 

We also create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
