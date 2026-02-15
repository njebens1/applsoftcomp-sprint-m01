The project provided two different datasets: child mortality rate and GDP per capita.

Both datasets were in wide format where each year existed as a separate column.

This format is difficult to analyze and needed to be converted into tidy data.



Cleaning Process:



First, both the CSV files were uploaded using pandas.



The country identifiers were renamed "Country Code" to geo

and "Country Name".



Next, each dataset was converted from wide format to tidy format using the

melt() function. This changed the structure so that each row represents

one country in one specific year. Additionally, the year columns were converted to numeric values and rows with missing data were removed.



Finally, I merged the mortality dataset with the GDP dataset using the

columns geo and year. The result was a single dataset containing: country code, country name, year, mortality rate, GDP per capita.



In the tidy data created, each row represents one observation. In this dataset, one observation is a single country during a single year.



Visualization Choices:



X-axis = GDP per capita



Y-axis = child mortality rate



Color = year



Using color allows for us to see how the relationship changed over time.



Observations:



The plot shows a clear inverse relationship: countries with higher GDP per

capita generally have lower child mortality. Over time, many countries

shift toward lower mortality rates, especially in more recent years.

