Dataset:

For this project we are using the taxi trips dataset. We choose this dataset because it has a lot of different numerical attributes to which we can compare with.


Attribute                   Description                                                 Type         

Trip ID	                    A unique identifier for the trip.                           Plain Text
Taxi ID	                    A unique identifier for the taxi.                           Plain Text
Trip Start Timestamp	    When the trip started, rounded to the nearest 15 minutes.   Date & Time
Trip End Timestamp	        When the trip ended, rounded to the nearest 15 minutes.     Date & Time
Trip Seconds	            Time of the trip in seconds.                                Number
Trip Miles	                Distance of the trip in miles.                              Number
Pickup Census Tract	        The Census Tract where the trip began.                      Plain Text
Dropoff Census Tract	    The Census Tract where the trip ended.                      Plain Text
Pickup Community Area	    The Community Area where the trip began.                    Number
Dropoff Community Area	    The Community Area where the trip ended.                    Number
Fare	                    The fare for the trip.                                      Number
Tips	                    The tip for the trip.                                       Number
Tolls	                    The tolls for the trip.                                     Number
Extras	                    Extra charges for the trip.                                 Number
Trip Total	                Total cost of the trip.                                     Number
Payment Type	            Type of payment for the trip.                               Plain Text
Company	                    The taxi company.                                           Plain Text
Pickup Centroid Latitude	The latitude of the center of the pickup census tract       Number
Pickup Centroid Longitude	The longitude of the center of the pickup census tract      Number
Pickup Centroid Location	The location of the center of the pickup census tract       Point
Dropoff Centroid Latitude	The latitude of the center of the dropoff census tract      Number
Dropoff Centroid Longitude	The longitude of the center of the dropoff census tract     Number
Dropoff Centroid Location	The location of the center of the dropoff census tract      Point

Total Number of Attributes: 26

Taxi trips reported to the City of Chicago, the dataset is heavy and characterised by 26 columns, the following reported are the ones used for our analysis

Features:
Trip ID: unique identifier for the trip
Taxi ID: unique identifier for the taxi
Trip start Timestamp: when the trip started
Fare : fare for the trip
Tips : tip for the trip 
Payment Type : type of payment for the trip

All data was filtered thanks the usage of Pandas, due to the restriction on the maximum uploading dimension on Observable (50MB). Before the filtering operations , we removed NaN and null values. Then the useless columns were removed and data were grouped according to the purpose of the visualization. After on observable the data were mapped to specific objects in order to get the different plots.


Questions:

Question 1:
    Is there any correlation between the extra charges and fare/tips? do they differ based on payment methods? 

Question 2:
    How do people tip when compared to fare charged and payment method?

Question 3:
    How has the amount of taxi taken changed during the year 2021, immediately after the Covid-19 restrictions?

Figure 1:

![Scatter Plot Matrix](Multi-Scatter.PNG)


The matrix scatterplot shows the behaviour of the fare and tips and extra charges amounts on a 3x3 matrix.
We choose this because we felt it was easiest way to visualize and compare 3 values at once. 

The color encodes the different type of payments: Credit Card, Mobile and Cash
we choose this so it would be easier to see trends based on payment type.

The graph's legend is also interactive, clicking on a square filters the data and removes none selected squares.
We choose this to help solve the problem of over plotting


Figure 2:

By seperating the graph into different encodings we can more easily see the trends of different attributes
to answer the questions we asked before

Question 2:
    How do people tip when compared to fare charged and payment method?

![Figure 2a](Credit.PNG)

The preferred way of payment is the credit card type, as shown from the majority of blue dots

Horizontal rows show fixed amounts for the tips, like 1,2,3 or 5 $, independently from the fare amount 

![Figure 2b](Mobile.PNG)

For mobile payments we can see a linear behaviour for the tips, 
probably due to the possibility on choosing the % of tips according to the fair (18%, 20%, 25%)


![Figure 2c](Cash.PNG)

For the Cash payments the tips is always zero, probably because there is no track of these.


Multi-View Interaction:

![Brushable Matrix Scatter Plot](Interaction.gif)


Thanks the usage of a brushing operation is possible to select specific range of data. It will result with a window on which the dots are colored with respect to the remaining ones that will be filled with a blackcolor. These dots will be highligted on every graph. However brushing over any of the [Fare vs Fare, Tips vs Tips, or Extra vs Extra] graphs, the brush + graph acts like a slider, moving up or down a value and showing it's respective dots associated with it. 

With this we can see trends based on amounts of attributes to answer our question.

Question 1:
    Is there any correlation between the extra charges and fare/tips? do they differ based on payment methods? 


Here we see a sliding brush example when looking at increasing extra charges

What we see is that there is no correlation between	 higher extra charges and the amount of tips/fare is charged, values seem to spread out all over the place with no noticable trend. What we do see is that Mobile payments have the smallest amounts of extra charges.




Single-View Interaction:

![Interactive Line Graph](Interactive_Map.png)


The plot used to analyse this kind of behaviour is a multiline plot in which each colored line encodes a specific month of the year. On the y axis is reported the number of rides, while on the x axis, the different days of the month. 

This kind of representation fits perfectly for timeseries and quantity values as the one described before.
Thanks the usage of the colored squares on the left, is possible to select or uncheck a specific month to make it appear in the visualization.

This also helps with overplotting

With this we can create charts to compare months together like so

![Figure C](Map_Comparison.png)

With this we can view trends easier now that overplotting is not an issue

Question 3:
    How has the amount of taxi taken changed during the year 2021, immediately after the Covid-19 restrictions?


For the first four months the number of taxi rides was low, probably due to the restrictions, so taxi were taken only by workers in this period.

Overall increasing in the number of taxi rides in the next fourth months of the year, probably to the easing of restrictions.

Increasing in the number of taxi, except for two quick decrease on Christmas day and the day after the Thanksgiving.



Conclusion:

Thanks to the visualizations proposed we were able to answer to the questions introduced at the beginning.
With the first plot we were able to see a majority of payments done through credit card and the different kind of tips related to the amount of money the method used to pay. We also saw the lack of correlation between extra charges, fare, and tips.
The connected scatterplot in the second case allow us to track the flow of taxi rides during an entire year. We are able to analyse different months together looking for interesting points characterised by big increase or decrease in the amount of rides provided during 2021.


