<img src="https://res.cloudinary.com/katzur/image/upload/v1659794036/favicon_jqzlwt.png" width="150" height="150" />

# **YESMoney** - manage your budget with handy e-wallet 

### [Click here to view the page](https://yes-money.herokuapp.com/)
### [Click here to view the repository](https://github.com/katzur/yes-money)


# Table of Contents:

1. [Introduction](#introduction)
	* [Demo](<#demo>)
2. [UX](#ux)
	* [Vision](<#vision>)
    * [Site Aims](<#site-aims>)
    * [Agile Methodology](<#agile-methodology>)
	* [Site Structure](<#site-structure>)
    * [Design](<#design>)
		* [Wireframes](#<wireframes>)
		* [Database Schema Diagram](<#database-schema-diagram>)
    * [Design](#design)
3. [Features](<#features>)
	* [Existing Features](<#existing-features>)
	* [Future Features](<#future-features>)
4. [Technologies Used](<#technologies-used>)
5. [Testing](<#testing>)
6. [Deployment](<#deployment>)
7. [Credits](<#credits>)


# Introduction
YESMoney is a website which allows users to track and monitor their daily incomes and spendings. Users are able to create their virtual wallet, where they can add their planned or current expenses and incomes, view them on the graph, and easily search and catrgorize them for better budget management.

YESMoney is a Full Stack Application built with the Django Framework which includes full CRUD functionality allowing users to Sign Up / Log In to their account and Add, Edit or Delete expenses and incomes and have a overview through graphs and charts of their financial situation, and trends of spending/ gaining money (categories of expenses and sources of incomes).
## Demo
<img src="https://res.cloudinary.com/katzur/image/upload/v1661416143/2022-08-25_09_27_30-Am_I_Responsive__hcgfoi.png" />


# UX
## Vision
The vision behind creating this site was focused on delivering a User an effective way to track their personal budget on daily basis. Allow the User to manage their wallet by using an easy to navigate website tool, that keeps it private (login required).User is able to follow the patterns of spendings based on categories and handy chart that visualize them, as well as summarize overall spendings and incomes over the last 6 months. The website was designed to be simple yet effective and provide a real use tool to people in need of monitoring their household budget. Page is easy and clear to navigate, based on the principle of "mobile first approach", which gives the freedom of using it on any type of device due to its full responsiveness. The aim was to provide all the main, necessary features expected for a personal budget tracker.

## Site Aims
* Provide the User with an easy to use page that allows them to track their personal finances.
* Allow the User to Create, Update and Delete their incomes and expenses.
* Allow the User to View (Read) their expenses and incomes via table and chart.
* Allow the User to import their incomes and expenses to handy CSV file in order to print it or save to their device.
* Allow the User to easily search their incomes and expenses through a Search bar.
* Allow the User to sort their incomes and expenses by amount, category/ source, description (alphabetically), and date.
* Provide visible and easy to understand response to User's action on the page.

## Agile Methodology
YESMoney project was based on the Agile Methodology, and Agile Kanban Board Framework was implemented in the site's creation process. It can be viewed [here](https://github.com/users/katzur/projects/5/views/1)
It was divided into three sections for clear tasks distribution and visual progress:
* Todo
* In Progress
* Done
* <img src="https://res.cloudinary.com/katzur/image/upload/v1661418886/2022-08-25_10_13_57-YESMoney_User_Stories_uqvtpa.png">

Based on the Iterative Development idea - while working on this project, I added new functional capabilities and modified existing features as needed over time. Different parts of the project were developed at various times and were integrated based on their successful completion. Increments were build based on their functionality need to not spend efforts on building features not neccessary for the project. Subsequent iterations were implemented based on the Users feedback and tests.

MoSCoW prioritization was taken under consideration while creating this project - some of the User Stories were critical (like user authentication, CRUD functionality) compared to other User Stories rather considerable (chart, contact form, CSV exports). Those with smaller impact were left for the later phase of page development, while other - vital ones - were guaranteed to be delivered on time. Timeboxing and prioritization were crutial for this project and can be reflected by viewing Iteration process (Todo > In Progress > Done) and labels assigned to each User Story (Must Have, Should Have, Could Have and Won't Have).
### <ins>Target Audience</ins>
YESMoney page was designed for all the Users, who are interested in tracking their personal budget, without any age limitation. Due to the nature of money - it is expected that adult Users will find it more useful and interesting as a product for a daily life use. By implementing modern design and vector graphics YESMoney is aspiring to be attractive also for younger Users, who wish to save information about their pocket money (this income source is available to choose) and various expenses.

### <ins>User Stories</ins>
* From the User Perspective:
1. As a Site User I can show/ hide my password once login in/ registering the account, so that I can see if it's typed in correctly/ hide it for the safety reasons.
2. As a Site User I can logout from the page so that no one can view my wallet details.
3. As a Site User I can add preference to my wallet (like currency choice) so that I can personalize the settings more.
4. As a Site User I can sign up with original, not repeating username and login to an account so that I can create and manage my wallet.
5. As a Site User I can create, read, update and delete my Expenses details so that I can see a true reflection of my actual Expenses.
6. As a Site User I can view a paginated list of expenses and incomes so that I can easily view and edit them on the page.
7. As a Site User I can search for specific expense so that I can easily find it in my wallet.
8. As a Site User I can create, read, update and delete my Income details so that I can see a true reflection of my actual Income.
9. As a Site User I can search for specific income so that I can easily find it in my wallet.
10. As a Site User I can view visual representation of my expenses (graph) so that I can have a better and easier look at my expenses details over certain period of time.
11. As a Site User I can view visual representation of my incomes (graph) so that I can have a better and easier look at my income details over certain period of time.
12. As a Site User I can provide feedback so that the Site Admin knows what needs to be changed in the app, and what additional categories they can add for expenses and incomes.
13. As a Site User I export my expenses to CSV file so that I can print it out or view in Excel or other application.
14. As a Site User I can reset my password so that I can easily regain access to my wallet in case I forget my password.
15. As a Site User I can view the income timeline: this week/ this month/ this year so that I can view better my income over certain period of time.
16. As a Site User I can view the expenses timeline: this week/ this month/ this year so that I can view better my expenses over certain period of time.

* From the Admin perspective:
1. As a Site Admin I can customize the Admin Panel so that I add different categories and features based on user's needs and feedback.
2. As a Site Admin I can create expense categories so that the Site Users can see better what type of expenses are generated over time.
3. As a Site Admin I can create income categories so that the Site Users can see better what type of expenses are generated over time.

### <ins>Epics (Ideas)</ins>
* Sign-in, sign-up, logout
* Password (reset, show)
* Manage incomes (CRUD)
* Manage expenses (CRUD)
* Page visibility (table, pagination, buttons - search, export)
* User notifications (messages, confirmation window)
* Graph (income, expense based on the database information for a specific User)

## Site Structure
YESMoney was developed usiutalizing Django. As a result the page functionality was split into separate applications. For this project I created 4 apps: authentication, expenses, incomes, userprferences for clear functionality split.

* Authentication - this app contains the pages that both: logged in and not logged in Users - will see: home page, contact page, login page and registration page. Those will be landing pages for the Users, who'll log out of the wallet (home), and those, who want to access the wallet (login). 
* Expenses - this app contain pages and functionality for Expenses site inside the wallet. Visible only for logged in Users. They allow the Users to see their expenses (main landing page), Add expenses, Edit Expenses, Delete Expenses, View the summary of expenses (chart).
* Income - this app contain pages and functionality for Income site inside the wallet. Visible only for logged in Users. They allow the Users to see their incomes (main landing page), Add incomes, Edit incomes, Delete incomes, View the summary of incomes (chart).
* Userpreferences - this app contain page and functionality for the User preferences inside the wallet under the tab "Currency preference". Visible only for logged in Users. Allows the User to choose their preffered currency out of the provided list and autopopulates this information across the other wallet pages.

## Design
### <ins>Wireframes</ins>
<details> <summary> Home page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428126/2022-08-25_12_48_23-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_frwa2i.png">
</details>
<details> <summary> Contact page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428209/2022-08-25_12_49_51-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_xfpfag.png">
</details>
<details> <summary> Login page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428251/2022-08-25_12_50_35-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_zv8z76.png">
</details>
<details> <summary> Registration page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428293/2022-08-25_12_51_17-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_f3cvm8.png">
</details>
<details> <summary> Main wallet page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428336/2022-08-25_12_51_55-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_xvqa3y.png">
</details>
<details> <summary> Chart page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428380/2022-08-25_12_52_38-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_hhkegj.png">
</details>
<details> <summary> Currency preference page</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661428446/2022-08-25_12_53_31-YESMoney.pdf_-_Adobe_Acrobat_Reader_DC_64-bit_w1owx5.png">
</details>
