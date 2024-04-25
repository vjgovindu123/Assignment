import pandas as pd
data=pd.read_csv("C:\\Users\\Govindu Vijay Kumar\\OneDrive\\Desktop\\Datasets for AI\\yelp-data\\yelp_business.csv")
print(data)
#Number of Business in City
print("number of business")
print(data['business_id'].count())
# print(data[data.columns[0]].count())
#Average number of stars in the city

print("Average of Stars",data['stars'].mean())

# print(data['stars'].mean())
#Restaurants in city
print("restaurants in city")
# print(data['Restaurants'].value_counts())
print(data['categories'].value_counts('Restaurants').count())
print("Average num of Stars of restaurant in city",data['stars'].value_counts('Restaurants').mean())

#print(data.business_id.unique())
#Retrieve Column names
for col in data.columns:
    print(col)
#Average review

print("The Avg Review in  City",data['review_count'].value_counts('business-id').mean())
print("The Avg Review in City Business",data['city'].value_counts('Restaurant').mean())
