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
| Status | **Authentication pages - Home**
|:-------:|:--------|
| &check; | Navbar contains links to Home, Contact, Login pages
| &check; | Pressing Home brings the User to the Homepage
| &check; | Pressing Contact brings the User to the Contact Form Page
| &check; | Pressing Login brings the User to the Login Page
| &check; | Homepage displays a button Register - after clicking it brings the User to Registration Page

| Status | **Authentication pages - Contact**
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

| Status | **Authentication pages - Login**
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


| Status | **Authentication pages - Register**
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

<details> <summary> Delete COnfirmation Page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661539569/delete_gpsaz2.jpg">
</details>

## Issues and bugs
1. Get Modal working with Delete button - I was able to create a modal for delete button, but it coudn't attach the delete option inside the modal to the expense/ income ID, hence needed to create a confirmation page in order to give the User a prompt asking for action verification.
2. Loading Bootstrap CSS and JavaScript - the example I was using had a source code urls displayed locally as <link href="../../dist/css/bootstrap.min.css"> instead of <link href="https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css"> which caused issues with recognizing the code. In effect - I couldn't get any styling until I edited them to https:// urls.
3. Displaying FontAwesome icons within the HTML code.
4. Search bar bug - when the User tries to search for an entry in the table, Search bar tends to double the output values (duplicates the entry). Once User presses backspace at least once - it comes back to normal, expected search result.
