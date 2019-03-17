# High-Level-Requirements

As the database team, we are envisioning creating a relational database where there is a data table for every possible class in the system. This will allow us to abstract a lot of the functionality in our interface, where there will be a fundamental set of "getter" and "setter" methods that the backend development teams can use to access the database. From here, each class will extend from our fundamental interface class. This will allow each class to add methods that are specific to the data items that will be associated with each class. Overall, this will enhance organization because we will not have to deal with having cumbersome amounts of data associated with each class, thus allowing us to simplify the process of accessing and altering data with each object in the system. 

<details>
  <summary> Data Tables </summary>
  
  ### User
  | ID | Email | Password | CC Number | CVV | isAdmin | isIdol |
  | :- | :---: | :------: | :-------: | :-: | :-----: | :----: |
  | Integer | String | String | Integer | Integer | Boolean | Boolean |
  
  ### URL
  | ID | Text/Link | Password | Shortened URL Key | User Key | Associated Website |
  | :- | :---: | :------: | :-------: | :-: | :-----: |
  | Integer | String | Integer | Integer | Date & Time Field | String |
  
  ### Shortened URL
  | ID | Text/Link | Password | Shortened URL Key | User Key | Associated Website |
  | :- | :---: | :------: | :-------: | :-: | :-----: |
  | Integer | String | Integer | Integer | Date & Time Field | String |
  
  ### Sponsored Items
  | ID | Company | Points Given | Description | Size | Times Used |
  | :- | :---: | :------: | :-------: | :-: | :-----: |
  | Integer | String | Integer | String | Int x Int | Integer |
  
  
</details>
  
