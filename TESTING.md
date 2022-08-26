# Testing

## Validator Testing 

### 1. [PEP8 Python Validation](http://pep8online.com/) - all pages passed successfully

<details> <summary> views.py - Authentication app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661454958/2022-08-25_20_15_45-PEP8_online_check_-_Results_osakhe.png">
</details>

<details> <summary> views.py - Expenses app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661455944/2022-08-25_20_32_02-PEP8_online_check_-_Results_smrnof.png">
</details>

<details> <summary> views.py - Incomes app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661456554/2022-08-25_20_42_20-PEP8_online_check_-_Results_ipcu1w.png">
</details>

<details> <summary> views.py - UserPreferences app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661456796/2022-08-25_20_46_20-PEP8_online_check_-_Results_x1hm9y.png">
</details>

<details> <summary> models.py - Expenses app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661457025/2022-08-25_20_50_14-PEP8_online_check_-_Results_tv8zmo.png">
</details>

<details> <summary> models.py - Incomes app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661457410/2022-08-25_20_56_33-PEP8_online_check_-_Results_imdqvr.png">
</details>

<details> <summary> models.py - UserPreferences app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661457496/2022-08-25_20_58_03-PEP8_online_check_-_Results_nf14it.png">
</details>

<details> <summary> urls.py - Authentication app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661457896/2022-08-25_21_04_11-PEP8_online_check_-_Results_uxhrgs.png">
</details>

<details> <summary> urls.py - Expenses app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661458743/2022-08-25_21_18_48-PEP8_online_check_-_Results_j5usa8.png">
</details>

<details> <summary> urls.py - Incomes app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661458859/2022-08-25_21_20_44-PEP8_online_check_-_Results_eqvt3n.png">
</details>

<details> <summary> urls.py - UserPreferences app </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661458916/2022-08-25_21_21_42-PEP8_online_check_-_Results_potfr4.png">
</details>

<details> <summary> settings.py </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661459239/2022-08-25_21_27_02-PEP8_online_check_-_Results_sjca2h.png">
</details>

### 2. [HTML Validation](https://validator.w3.org/)
<details> <summary> Tested for all the pages. </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661463898/2022-08-25_22_44_31-Showing_results_for_https___yes-money.herokuapp.com__-_Nu_Html_Checker_dl8qt4.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_08_50-Showing_results_for_https___yes-money.herokuapp.com_authentication_contact_-_Nu_pfk7pv.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_08_50-Showing_results_for_https___yes-money.herokuapp.com_authentication_contact_-_Nu_pfk7pv.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_09_48-Showing_results_for_https___yes-money.herokuapp.com_add-expense_-_Nu_Html_Checke_u561be.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_09_27-Showing_results_for_https___yes-money.herokuapp.com_authentication_index_-_Nu_Ht_muttkx.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_08_59-Showing_results_for_https___yes-money.herokuapp.com_authentication_login_-_Nu_Ht_ilbbhb.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_10_20-Showing_results_for_https___yes-money.herokuapp.com_income_add-income_-_Nu_Html_v6oqkb.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_09_58-Showing_results_for_https___yes-money.herokuapp.com_stats_-_Nu_Html_Checker_jfw4kf.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533922/2022-08-26_18_10_10-Showing_results_for_https___yes-money.herokuapp.com_income_-_Nu_Html_Checker_jdtlpe.png">
</details>

### 3. [CSS Validation](https://jigsaw.w3.org/css-validator/)
<details> <summary> The errors which can be seen on the screenshot below is coming from default Bootstrap url: https://getbootstrap.com/docs/5.2/dist/css/bootstrap.min.css. Confirmed that it can be ignored, as it wasn't caused by my work on the project. </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661467017/2022-08-25_22_48_32-W3C_CSS_Validator_results_for_https___yes-money.herokuapp.com__CSS_level_3_SV_zabemc.png">
</details>

### 4. [JavaScript Validation](https://jshint.com/)
No errors, just warnings for Mozilla JS extensions (use moz) and  ES6 (use 'esversion: 6'). Missing semicolons fixed.
<details> <summary> static/js/register.js </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661532404/2022-08-26_17_46_26-JSHint_a_JavaScript_Code_Quality_Tool_wlzzrz.png">
</details>

<details> <summary> static/js/searchExpenses.js </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661532494/2022-08-26_17_47_51-JSHint_a_JavaScript_Code_Quality_Tool_l1ywww.png">
</details>

<details> <summary> static/js/searchIncome.js </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661532542/2022-08-26_17_48_46-JSHint_a_JavaScript_Code_Quality_Tool_fwimwt.png">
</details>

<details> <summary> static/js/stats.js </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661532595/2022-08-26_17_49_39-JSHint_a_JavaScript_Code_Quality_Tool_ib1hqb.png">
</details>

<details> <summary> static/js/stats-income.js </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661533013/2022-08-26_17_55_22-JSHint_a_JavaScript_Code_Quality_Tool_k2to4m.png">
</details>

## Lighthouse Score

### Mobile:
<details> <summary> Mobile Lighthouse Score </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661467281/2022-08-25_22_02_42-YESMoney_u4ewst.png">
</details>

### Desktop:
<details> <summary> Desktop Lighthouse Score </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661467268/2022-08-25_23_40_43-YESMoney_likd16.png">
</details>

## User Story Testing




## Manual Testing

### <ins>Authentication pages work the same way for logged in and not logged in Users</ins>
|  | **Authentication pages - Home**
|:-------:|:--------|
| &check; | Navbar contains links to Home, Contact, Login pages
| &check; | Pressing Home brings the User to the Homepage
| &check; | Pressing Contact brings the User to the Contact Form Page
| &check; | Pressing Login brings the User to the Login Page
| &check; | Homepage displays a button Register - after clicking it brings the User to Registration Page

|  | **Authentication pages - Contact**
|:-------:|:--------|
| &check; | Navbar contains links to Home, Login, Register pages
| &check; | Pressing Home brings the User to the Homepage
| &check; | Pressing Login brings the User to the Login Page
| &check; | Pressing Register brings the User to the Registration Page
| &check; | Page contains contact form: each field (Name, Email, Message) is required and if missed any, and pressed Submit - error messages are showing, asking to fill them before sending
| &check; | Name field requires a text value to be entered in order to process with sending form
| &check; | Email field requires a email value to be entered in order to process with sending form
| &check; | Message field requires a text value to be entered in order to process with sending form
| &check; | Button to send form is only active once all fields are populated
| &check; | After pressing send button - User is brought back to Homepage and message pops on the top of the page informing about successful form submission
| &check; | Contact page contains social media icons and allows to click them 
| &check; | After clicking on the social media button - the User is brought to the relevant social media page in the new window

|  | **Authentication pages - Login**
|:-------:|:--------|
| &check; | Navbar on the Login page is collapsable and in form of hamburger on the center top of the page - User can click to open it and close
| &check; | Navbar contains links to Home, Contact, Login, Register pages
| &check; | Pressing Home brings the User to the Homepage
| &check; | Pressing Contact brings the User to the Contact Form Page
| &check; | Pressing Login keeps the User on the Login Page
| &check; | Pressing Register brings the User to the Registration Page
| &check; | Page contains login form: each field (Username, Password) is required and if missed any, and pressed Login - error messages are showing, asking to fill them before redirecting to main wallet page
| &check; | Username field requires a text value to be entered in order to process with login
| &check; | Password field requires a text value to be entered in order to process with login
| &check; | Show Password button allows the User to show/ hide the password to ensure that it was entered correctly
| &check; | If any of the fields are entered incorrectly or missed - error messages are showing, asking to fill them before sending
| &check; | If entered credentials are incorrect or don't exist in the database - error message is displayed informing the User about it
| &check; | Register button is present on the page and once clicked - redirects the User to the Registration page
| &check; | If entered credentials are correct and button is clicked - User gets redirected to main wallet page, where greetings message gets displayed


|  | **Authentication pages - Register**
|:-------:|:--------|
| &check; | Navbar on the Register page is collapsable and in form of hamburger on the center top of the page - User can click to open it and close
| &check; | Navbar contains links to Home, Contact, Login, Register pages
| &check; | Pressing Home brings the User to the Homepage
| &check; | Pressing Contact brings the User to the Contact Form Page
| &check; | Pressing Login brings the User to the Login Page
| &check; | Pressing Register keeps the User on the Registration Page
| &check; | Page contains registration form: each field (Username, Email, Password) is required and if missed any, and pressed Register - error messages are showing, asking to fill them before registering the User in the database
| &check; | Username field requires a text value to be entered in order to process with registration
| &check; | Email field requires a email value to be entered in order to process with registration
| &check; | Password field requires a text value to be entered in order to process with registration
| &check; | Show Password button allows the User to show/ hide the password to ensure that it was entered correctly
| &check; | If any of the fields are entered incorrectly or missed - error messages are showing, asking to fill them before sending
| &check; | If entered credentials are correct and button is clicked - message is displayed, informing the User that action was successful and they're allowed to log in

### <ins>Wallet pages work ONLY for logged in Users.</ins>
* It's not accessible for Users who are not logged into their account. 
* Logged in Users can see ONLY their own wallet. 
* There is no way for the Users to view other Users incomes/ expenses. 
* Admin has an option to view all the Users, their credentials, expenses and incomes within Admin Panel, that is accessible only by following the url: https://yes-money.herokuapp.com/admin

|  | **Wallet pages - Main Expenses Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains navigation links, button for exporting CSV file, button for adding expense, search bar, table with expenses, within table: edit button, delete button, table pagination
| &check; | Pressing navigation informs the user on which site they're at the moment and let's them click the link to redirect to the same page
| &check; | Pressing Export CSV allows the User to generate a CSV file and download it automatically into their device with list of all table entries
| &check; | Pressing Add Expense button brings the User to the Add Expense page
| &check; | Search bar allows the User to type in any value to search for expense in the table based on amount, category, description or date
| &check; | Pressing Edit button brings the User to the Edit Expense page
| &check; | Pressing Delete button brings the User to the Delete Confirmation page
| &check; | Information above pagination buttons contain information how many pages has the table
| &check; | Pressing Pagination button allows the User to navigate between the table pages, where each contains 5 entries.


|  | **Wallet pages - Expenses Table**
|:-------:|:--------|
| &check; | Table displays columns with following headers: amount + type of amount populated from currency preference page, category, description, date
| &check; | Table additionally contains Edit and Delete buttons next to each entry.
| &check; | Pressing Edit button brings the User to the Edit Expense page
| &check; | Pressing Delete button brings the User to the Delete Confirmation page
| &check; | Pressing on Category and Description column headers allows the User to sort the entries alphabetically ascending, descending 
| &check; | Pressing on Amount column header allows the User to sort the entries from smallest to the biggest amount and vice versa
| &check; | Pressing on Date column header allows the User to sort the entries by date from newest to oldest and vice versa


|  | **Wallet pages - Income Table**
|:-------:|:--------|
| &check; | Table displays columns with following headers: amount + type of amount populated from currency preference page, source, description, date
| &check; | Table additionally contains Edit and Delete buttons next to each entry.
| &check; | Pressing Edit button brings the User to the Edit Income page
| &check; | Pressing Delete button brings the User to the Delete Confirmation page
| &check; | Pressing on Source and Description column headers allows the User to sort the entries alphabetically ascending, descending 
| &check; | Pressing on Amount column header allows the User to sort the entries from smallest to the biggest amount and vice versa
| &check; | Pressing on Date column header allows the User to sort the entries by date from newest to oldest and vice versa


|  | **Wallet pages - Main Income Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains navigation links, button for exporting CSV file, button for adding income, search bar, table with incomes, within table: edit button, delete button, table pagination
| &check; | Pressing navigation informs the user on which site they're at the moment and let's them click the link to redirect to the same page
| &check; | Pressing Export CSV allows the User to generate a CSV file and download it automatically into their device with list of all table entries
| &check; | Pressing Add Income button brings the User to the Add Income page
| &check; | Search bar allows the User to type in any value to search for incomes in the table based on amount, category, description or date
| &check; | Pressing Edit button brings the User to the Edit Income page
| &check; | Pressing Delete button brings the User to the Delete Confirmation page
| &check; | Information above pagination buttons contain information how many pages has the table
| &check; | Pressing Pagination button allows the User to navigate between the table pages, where each contains 5 entries.

|  | **Wallet pages - Expenses Chart Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains navigation links, BACK button, chart
| &check; | Pressing BACK brings the User to the main Income page
| &check; | Pressing navigation informs the user on which site they're at the moment and let's them click the link to redirect to the same page
| &check; | Expenses chart is a type of dougnut
| &check; | Expenses chart has different color for each category
| &check; | Expenses chart displays a legend on the top with colors assigned to each category
| &check; | Expenses categories legend elements are clickable and allow the User to display/ not dispay chosen categories
| &check; | By default all categories from the expenses table are displayed on the chart
| &check; | By hoovering over certain color on the chart, the total amount for this category displays
| &check; | Chart contains information for the last 6 months of expenses

|  | **Wallet pages - Income Chart Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains navigation links, BACK button, chart
| &check; | Pressing navigation informs the user on which site they're at the moment and let's them click the link to redirect to the same page
| &check; | Pressing BACK brings the User to the main Income page
| &check; | Income chart is a type of dougnut
| &check; | Income chart has different color for each source
| &check; | Income chart displays a legend on the top with colors assigned to each source
| &check; | Income source legend elements are clickable and allow the User to display/ not dispay chosen income sources
| &check; | By default all sources from the income table are displayed on the chart
| &check; | By hoovering over certain color on the chart, the total amount for this source displays
| &check; | Chart contains information for the last 6 months of income

|  | **Wallet pages - Currency Preference**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains main table with dropdown menu and save button
| &check; | Pressing dropdown menu displays all available currencies
| &check; | Clicking Save button saves the Users preference and autopopulates within the table

|  | **Wallet pages - Add Expense Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains a form, which allows the User to add expense details
| &check; | Form has fields for: amount, description, category, date - all are required and if missed any, and pressed Submit - error messages are showing, asking to fill them
| &check; | Amount field requires a numeric value to be entered in order to process with adding the expense
| &check; | Description field requires a text value to be entered in order to process with adding the expense
| &check; | Category field contains a dropdown menu, allowing the User to choose one of the available values to be selected in order to process with adding the expense
| &check; | Date field opens a calendar and allows the User to choose the date of the expense to be selected in order to process with adding the expense
| &check; | Pressing Submit button when not all the fields are populated - displays an error for specific empty field
| &check; | Pressing Submit button when all the fields are populated - allows to save the entry in the database and displays it within the table on the main expenses page
| &check; | After successful adding of new expense - a message is displayed to the User informing about successful action of adding new expense

|  | **Wallet pages - Add Income Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains a form, which allows the User to add income details
| &check; | Form has fields for: amount, description, source, date - all are required and if missed any, and pressed Submit - error messages are showing, asking to fill them
| &check; | Amount field requires a numeric value to be entered in order to process with adding the income
| &check; | Description field requires a text value to be entered in order to process with adding the income
| &check; | Source field contains a dropdown menu, allowing the User to choose one of the available values to be selected in order to process with adding the income
| &check; | Date field opens a calendar and allows the User to choose the date of the income to be selected in order to process with adding the income
| &check; | Pressing Submit button when not all the fields are populated - displays an error for specific empty field
| &check; | Pressing Submit button when all the fields are populated - allows to save the entry in the database and displays it within the table on the main income page
| &check; | After successful adding of new income - a message is displayed to the User informing about successful action of adding new income

|  | **Wallet pages - Edit Expense Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains a form, which allows the User to edit expense details
| &check; | Form has fields for: amount, description, category, date, as well as save button and delete button
| &check; | Pressing Delete button brings the User to the Delete Confirmation page
| &check; | Form fields are autopopulated based on the previous entry and allow the User to correct the information
| &check; | Once clicked Save - it saves the entry in the database and displays corrected values within the table on the main expenses page
| &check; | Amount field requires a numeric value to be entered in order to process with adding the expense
| &check; | Description field requires a text value to be entered in order to process with adding the expense
| &check; | Date field opens a calendar and allows the User to choose the date of the expense to be selected in order to process with adding the expense
| &check; | Category field contains a dropdown menu, allowing the User to choose one of the available values to be selected in order to process with adding the expense
| &check; | After successful editing of existing expense - a message is displayed to the User informing about successful action on the main expenses page

|  | **Wallet pages - Edit Income Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains a form, which allows the User to edit income details
| &check; | Form has fields for: amount, description, source, date, as well as save button and delete button
| &check; | Pressing Delete button brings the User to the Delete Confirmation page
| &check; | Form fields are autopopulated based on the previous entry and allow the User to correct the information
| &check; | Once clicked Save - it saves the entry in the database and displays corrected values within the table on the main income page
| &check; | Amount field requires a numeric value to be entered in order to process with adding the income
| &check; | Description field requires a text value to be entered in order to process with adding the income
| &check; | Date field opens a calendar and allows the User to choose the date of the income to be selected in order to process with adding the income
| &check; | Source field contains a dropdown menu, allowing the User to choose one of the available values to be selected in order to process with adding the income
| &check; | After successful editing of existing income - a message is displayed to the User informing about successful action on the main income page


|  | **Wallet pages - Delete COnfirmation Page**
|:-------:|:--------|
| &check; | Page displays greeting and logged in Username in the top Navbar section
| &check; | Sidebar contains Logo button, list of links with wallet options, sign out button
| &check; | Pressing Logo button brings the User to the wallet homepage
| &check; | Pressing Sign Out button brings the User to the authentication homepage and displays a message there informing about the taken action
| &check; | Pressing Expenses in the sidebar brings the User to the main Expenses page
| &check; | Pressing Income in the sidebar brings the User to the main Income page
| &check; | Pressing Expenses Chart in the sidebar brings the User to the Expenses visual statistics page
| &check; | Pressing Income Chart in the sidebar brings the User to the Income visual statistics page
| &check; | Right pane contains form with two buttons: Delete and Cancel
| &check; | Pressing on Delete button allows the User to permanently delete the entry from the database
| &check; | Once entry is deleted - User is brought back to the main page and message displays with information about successful deletion
| &check; | Pressing on Cancel brings back the User to the main Expense or Income page


## Error tracing and fixing
<details> <summary> Username testing. For that purpose I used the Postman to test the username validation request </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661534975/username.test_srymjr.jpg">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661535031/username.test2_ln0jwz.jpg">
</details>

<details> <summary> Registration form testing. Create a file register.js inside js folder to test it with DevTools > Inspect > Console > message: "register working" </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661535215/registration.testing_wboatc.jpg">
</details>

<details> <summary> Test of the user typing for the validation of the Username purpose, as real-time validation intended. Tested with Console in DevTools</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661535602/username.validation.test_ijmbu4.jpg">
</details>

<details> <summary> Email validation testing. For that purpose I used the Postman to test the username validation request and installed validate-email packet ('pip3 install validate-email')</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661535767/email.validation.test_satlwa.jpg">
</details>

<details> <summary> Python debugger for the currency.json file test that allows the User to choose currency</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661536151/currency.json.test_jrc006.jpg">
</details>

<details> <summary> add_expenses function testing using the Debug = True mode for browser error return</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661536877/add_expenses.testing_j1r09k.jpg">
</details>

<details> <summary> Proof of terminal use for errors as well as browser errors in Debug = True mode. Examples of errors received that were addressed</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661537217/examples_of_errors_odkeqy.jpg">
</details>

<details> <summary> Issues with Income > views.py for searching income that were addressed by testing and browser error responses</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661537456/income_function_testing_wr3wmt.jpg">
</details>

<details> <summary> Charts API call through Postman</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661537523/api_call_for_chart_ism4ah.jpg">
</details>

<details> <summary> Stats (charts) testing using Inspect > Console</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661537880/charts.testing_ajgljw.jpg">
</details>

## Responsiveness Test
For this test I chose three different values: default for my desktop browser 1447px, tablet - 768px, mobile - 480px
<details> <summary> Home Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/index_g9yyd1.jpg">
</details>

<details> <summary> Contact Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/contact_ikr83z.jpg">
</details>

<details> <summary> Login Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/login_zlvqw1.jpg">
</details>

<details> <summary> Main Wallet Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539570/wallet_evgcni.jpg">
</details>

<details> <summary> Chart Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/charts_ou2ow9.jpg">
</details>

<details> <summary> Currency Preference Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/currency_kk2rq9.jpg">
</details>

<details> <summary> Delete Confirmation Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/delete_gpsaz2.jpg">
</details>

## Issues and bugs
1. Get Modal working with Delete button - I was able to create a modal for delete button, but it coudn't attach the delete option inside the modal to the expense/ income ID, hence needed to create a confirmation page in order to give the User a prompt asking for action verification.
2. Loading Bootstrap CSS and JavaScript - the example I was using had a source code urls displayed locally as link href="../../dist/css/bootstrap.min.css" instead of link href="https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css" which caused issues with recognizing the code. In effect - I couldn't get any styling until I edited them to https:// urls.
3. Displaying FontAwesome icons within the HTML code.
4. Search bar bug - when the User tries to search for an entry in the table, Search bar tends to double the output values (duplicates the entry). Once User presses backspace at least once - it comes back to normal, expected search result.
