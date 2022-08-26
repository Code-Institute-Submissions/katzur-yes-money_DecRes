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
        * [Website Surface](#website-surface)
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
13. As a Site User I export my expenses and incomes to CSV file so that I can print it out or view in Excel or other application.

* From the Admin perspective:
1. As a Site Admin I can customize the Admin Panel so that I add different categories and features based on user's needs and feedback.
2. As a Site Admin I can create expense categories so that the Site Users can see better what type of expenses are generated over time.
3. As a Site Admin I can create income sources so that the Site Users can see better what type of incomes are generated over time.

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

## Database Schema Diagram
<details> <summary> View the diagram</summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661430617/2022-08-25_13_29_53-Settings_rbmm3i.png">
</details>

Database schema for this project required creating 5 different relational databases, which interact with each other to provide proper functionality of the page.
1. Default Django User database - stores the usernames and passwords of all the registered Users. Allows them to login to the wallet, view their incomes and expenses, create new ones, edit them and delete. No need for creating any models, since come as default.
2. Expense database with relationship to the Category database and Users database. Has fields for amount, date, description, owner and category. On this database all Expense related actions rely solely - without it the Users wouldn't be able to add any Expenses, then view them, see them on Chart, edit or delete, as all information from this database is crutial for all those wallet operations.
3. Income database with relationship to the Source database and Users database. Has fields for amount, date, description, owner and source. On this database all Incomes related actions rely solely - without it the Users wouldn't be able to add any Incomes, then view them, see them on Chart, edit or delete, as all information from this database is crutial for all those wallet operations.
4. Category database - allows the User to choose relevant category for their expenses based on the name field. New Category names are added by Admins within the panel, and then utilized by the Users in CRUD operations in the wallet.
5. Source database - allows the User to choose relevant source for their incomes based on the name field. New Source names are added by Admins within the panel, and then utilized by the Users in CRUD operations in the wallet.
6. UserPreference database - Expense and Income databases rely on the information passed from UserPreference fields about chosen currency for specific, logged in User. Data from this database populates the fileds within the tables in Income and Expense pages and definies specific, chosen from the JSON list, currency.

### Website Surface
### <ins>Colors</ins>
The colors used throughout the page for its main styling are shown below. They are complimented by more colorful images on the specific pages (home, contact, delete confirmation, currency preference), buttons, messages,and background on the login/ register page. The aim was to provide the website consistent, clean look. Colors and layout of the elements were intentionally picked to keep the modern, simple design. Colors compliment each other well and keep great page contrast, which makes it more user-friendly and readable.

<img src="https://res.cloudinary.com/katzur/image/upload/v1661432220/2022-08-25_13_56_37-Create_a_Palette_-_Coolors_mx0sww.png" width="700">

<img src="https://res.cloudinary.com/katzur/image/upload/v1661432391/2022-08-25_13_59_35-Color_Contrast_Checker_-_Coolors_poqsyw.png" width="700">

### <ins>Typography</ins>
I decided to stay mostly with default fonts that came with Bootstrap CSS styling. Two fonts I especially liked to continuously use within this project to provide satisfiying design:

* Monospace - well known, easy to read, fits the page overal style. Used for the page name and login/ registration pages.
* Segoe UI - sans-serif font - clean and easy to read.

### <ins>Icons and images</ins>
All icons used for YESMoney come from [IconScout](https://iconscout.com/)

All images used for YESMoney come from [Freepik](https://www.freepik.com/)

# Features
YESMoney is designed as a webpage and the functionality and features were selected based on the Kanban Board and MoSCoW prioritization (applied labels to User Stories). During the process of the page creation I was able to decide what needs to be implemented, and what set of features can be potentially added in the future.

## Exisiting Features
YESMoney currently allows the User to go through the User authentication: register the account, login to their personal wallet. Unregistered User can send the feedback or comments through the contact form, but the rest of the features require authentication. Users must have an account in order to use the wallet features, which allow them to create, edit, delete and view their incomes and expenses.
This way the User can keep track of their budget and monitor incomes and expenses over time by adding them to the table, generating CSV files, searching and viewing the chart.

<details> <summary> Homepage </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661437761/2022-08-25_15_29_07-YESMoney_qcb2d0.png">
</details>
Main page that allows the User to easily navigate through available options - contact, login, register. Once the User is loggin out of the wallet - they're brought to this page. Once the contact form is sent - the User is also brough to this page.

<details> <summary> Contact </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661438017/2022-08-25_15_33_17-YESMoney_Contact_Form_vjivec.png">
</details>
Allows the User to send a feedback or other type of message to the site creator. Contains social media information and links to other available pages within YESMoney.

<details> <summary> Login </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661439163/2022-08-25_15_52_14-YESMoney_g3ie44.png">
</details>
Allows the User to log into their wallet. Has additional function to show the password, and small collapsable navbar on the top.

<details> <summary> Register </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661439301/2022-08-25_15_54_46-YESMoney_nucale.png">
</details>
Allows the User to register their account. Has additional function to show the password, button for registered Users to sign in, and small collapsable navbar on the top.

<details> <summary> Main wallet page </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661439390/2022-08-25_15_56_13-YESMoney_w97rcn.png">
</details>
Looks nearly identical for expenses and incomes. Left pane contains a sidebar with links and option to log out. Top navbar contains greeting and displays username. Right pane contains main table with expenses/ incomes, buttons to edit and delete the entry. On the top above the table there are buttons to add new entry and download CSV file. Below the table there's a handy pagination that keeps 5 entries on each page. Additionally page has a search bar that allows the User to browse for expenses/ incomes. Table itself has option to sort entries by each table column header.

<details> <summary> Charts </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661439780/2022-08-25_16_02_43-YESMoney_ylbler.png">
</details>
Looks nearly identical for expenses and incomes. Left pane contains a sidebar with links and option to log out. Top navbar contains greeting and displays username. Right pane contains a visualization of incomes/ expenses in form of doughnut chart for the last 6 months. It allows the User to interact - by clicking on the category/ source - User can decide which expenses they want to display. After hovering over certain color on the chart - it summarize the amount spent/ gained within a certain category/ source.

<details> <summary> Currency preference </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661439968/2022-08-25_16_05_53-YESMoney_zp0nl1.png">
</details>
This page allows the User to personalize their wallet by selecting User's chosen currency. Based on this information - the other pages get the information about valid currency and autopopulate that information in the table. 

<details> <summary> Delete confirmation </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661440239/2022-08-25_16_10_25-YESMoney_vqgg3l.png">
</details>
This page displays once the User clicks on the red X button in order to delete the expense/ income entry. It confirms with the User that it was an intended action, not a mistake.

<details> <summary> Add expense/ income </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441100/2022-08-25_16_24_36-YESMoney_u1zpug.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441296/2022-08-25_16_27_55-YESMoney_kcdbda.png">
</details>
This page allows the User to add income/ expense. Once entry added - the information will display within the table on the main page for income/ expenses and will be added to the graph in the summary.

<details> <summary> Edit income/ expense </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441437/2022-08-25_16_30_19-YESMoney_ztkxb8.png">
</details>
This page allows the User to edit income/ expense and looks nearly identical for both. Once entry edited - the information will change and display with new values within the table on the main page for income/ expenses and change will be reflected within the graph in the summary. Additionally this page has a 'Delete' button that allows the User to remove the entry from the database.

<details> <summary> Messages </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441805/2022-08-25_16_36_29-YESMoney_g14vay.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441805/2022-08-25_16_35_39-YESMoney_kqj1t8.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441805/2022-08-25_16_34_40-YESMoney_beruqf.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441805/2022-08-25_16_35_51-YESMoney_kaq6yh.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441805/2022-08-25_16_35_25-YESMoney_wzfedc.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661441805/2022-08-25_16_35_06-YESMoney_bdqzkl.png">
</details>
Page has dedicated pop-up messages reflecting User's actions - it gives the User a feedback what the actions mean. Examples can be found here.

<details> <summary> Admin Page </summary>
<img src="https://res.cloudinary.com/katzur/image/upload/v1661442218/2022-08-25_16_42_21-https___8000-katzur-yesmoney-wrhcvxduy7m.ws-eu62.gitpod.io_admin__uxs1wx.png">
<img src="https://res.cloudinary.com/katzur/image/upload/v1661442218/2022-08-25_16_42_44-https___8000-katzur-yesmoney-wrhcvxduy7m.ws-eu62.gitpod.io_admin_login__next__ad_wofucv.png">
</details>
Page only available for Site Administrators once accessing https://yes-money.herokuapp.com/admin Allows the Admins to view, modify and delete Users, Expenses and Categories, Incomes and Sources. 

## Future Features
* Option for the Users to reset the password by email link
* Authentication of newly registered Users by email link
* Viewing the income on the timeline, where User can select time period (weekly, monthly, yearly expenses/ incomes)
* Add additional graphs for better income/ expense view (graphs: lines, bars)
* Add additional output boxes displaying overall spending/ income, this month's spending/ income, and amount of transactions
* History of User's actions


# Technologies Used
## Languages and Frameworks
* HTML
* CSS
* JavaScript
* Python
* Django - Python Framework used to create the project.
* Bootstrap - CSS framework used for designing the project.

## Other Technologies
* DevTools - help fix problem areas and identify the errors.
* Heroku - project deployment.
* PostgreSQL (Heroku) - database used through Heroku.
* Cloudinary - store static files and images.
* GitHub, Gitpod - storing code and deploying the site, building and editing the code.
* Notepad++ - help with writing some additional code, experiments and changes.
* Balsamiq - wireframes creation.
* Postman Agent - API requests
* Diagram.net - database diagram schema creation
* [Sortable](https://github.com/tofsjonas/sortable) - Vanilla JavaScript table sort

## Content
* [E-wallet idea](https://pl.pinterest.com/pin/293859944448506091/) - found on Pinterest in design suggestions
* Django tutorial series from [Cryce Truly](https://www.youtube.com/c/CryceTruly) - absolutely great content teaching basic Django and JavaScript/ Ajax in context of building financial websites and user authentication functionality
* Code Institute walkthrough project ['I think therefore I blog'](https://github.com/Code-Institute-Solutions/Django3blog) - great sorece of information how to start Django project and how to move with project configuration
* Bootstrap Examples. Pages for this project are based on [Dashboard](https://getbootstrap.com/docs/5.2/examples/dashboard/), [Cover](https://getbootstrap.com/docs/5.2/examples/cover/), [Sign-In](https://getbootstrap.com/docs/5.2/examples/sign-in/), as well as Bootstrap documentation.
* [Chart.js](https://www.chartjs.org/docs/latest/) - provided base for project's charts for incomes and expenses
* Django Testing from Code Institute ['Hello Django' Walkthrough project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/)
* Python Expense Tracker Project from [Data-Flair](https://data-flair.training/blogs/expense-tracker-python/) - explaining step by step how to implement charts, table, history of User's actions
* Article [Creating a Budget Web App with Django](https://kristian-roopnarine.medium.com/creating-a-budget-web-app-with-django-655369b6d43c) - useful information about the models and functions implementation
* [Colorib - Bootstrap Hamburger Menu Examples](https://colorlib.com/wp/bootstrap-hamburger-menu/) > Here I used [Menu Toggle Button](https://codepen.io/GeoffreyCrofte/full/nybYBm) for Login and Registration Page, and [Contact Form](https://preview.colorlib.com/theme/bootstrap/contact-form-16/)
* [Codepen - Sliding Diagonals Background](https://codepen.io/chris22smith/pen/RZogMa) - for interesting background effect for Login and Registration page
* [Article about User Stories by Anastasiia Kalachova](https://www.altamira.ai/blog/difference-between-epics-vs-user-stories/) - explaining difference between epics and user stories
* [Freepik](https://www.freepik.com/) - beautiful free vector images from [Storyset](https://www.freepik.com/author/stories)
* [Tutorial on contact forms functionality](https://www.youtube.com/watch?v=1ihn3iRXtsY&t=902s&ab_channel=djangotutorials) from Djangotutorials
* Color pallete creator and contrast checker were from on [Coolors](https://coolors.co/)
* The logo was created on [VistaCreate](https://create.vista.com/home/)

# Testing
Due to the size of the testing section, I created TESTING.md. It contains:
* Validators testing, 
* Lighthouse scores, 
* User Story Testing, 
* Manual Tests, 
* Error tracing and fixing in development process,
* Responsiveness Tests, 
* Issues and bugs.

Please go to [TESTING.md](TESTING.md)

# Deployment
## Forking The GitHub Repository
To use this code and make changes without affecting the original code you can do what is called 'Forking the repository'. 
By forking this repository you are given a copy of the code at that moment in time that you can use freely. 
To fork this repository you need to follow the following few steps:

1. Create an account or log into your existing GitHub account.
2. Navigate to the [Repository](https://github.com/katzur/yes-money), you are wanting to fork.
3. In the upper-right of the repository, click the 'Fork' button.
4. A copy of the Repository will now be available within your repositories.

You will now have a copy of the code available to clone and work on without affecting the original code.

## Cloning the Project.
To make a local clone of the project follow these steps:

1. Log into your GitHub account.
2. Navigate to the [Repository](https://github.com/katzur/yes-money).
3. In the upper section of the repository click the drop-down option: 'Code'.
4. Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it.
5. Open a new workspace in GitPod.
6. Open GitBash. In the bash terminal type 'git clone [copy url here from step 4]'
7. Press enter - the IDE will clone and download the repo.
8. GitBash will clone the repository into this directory.
9. Optionally type: 'python3 manage.py runserver' to host the website locally - it won't run the python file, only allow you see how it looks.
10. To use the required libraries: type in the console: pip3 install -r requirements.txt.
11. To create a web-app from the repo, follow the instructions in "Heroku App Deployment".

## GitHub Desktop App
1. Log in to your GitHub account or create an account.
2. Navigate to the [Repository](https://github.com/katzur/yes-money).
3. Select the 'Code' button above the file list on the right had side.
4. Select 'Open with GitHub Desktop'
5. Install GitHub Desktop Application.
6. The repo will be copied locally onto your machine.
7. If you want to create a web-app from the repo please follow the instructions in "Heroku App Deployment"

## Download and extract the zip directly from GitHub
1. Log in to your GitHub account
2. Navigate to the [Repository](https://github.com/katzur/yes-money)
3. Select the 'Code' button above the file list on the right had side
4. Select 'Download Zip'
5. Once you have the Zip downloaded, open it with your preferred file decompression software
6. You can then drag and drop the files from the folder into your chosen IDE or view/edit them on your local machine
7. In the console, run: pip install -r requirements.txt
8. If you want to create a web-app from the repo please follow the instructions in "Project Deployment"

## Heroku App Deployment.
1. Create the GitPod repo from the [CI Template](https://github.com/Code-Institute-Org/gitpod-full-template) via the GitPod button in GitHub.
2. Create an account or log into your existing Heroku account.
3. Click on: NEW in the top right corner and choose create a new app.
4. Enter a unique name for the Heroku app.
5. Click on: Create App.
6. Add Heroku PostgreSQL add-on in the Resources tab.
7. Once the app is built, navigate to "Settings" and scroll down to "Config Vars". 
    * Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py as a root level file.
    
    ```python
    DATABASE_URL - linking to PostgrSQL
    SECRET_KEY - needs to be created within the projects env.py file on GitPod, then added to the Config Vars on Heroku.
    DISABLE_COLLECTSTATIC = 1 - temporary solution to enable deployment without any static files.
    PORT = 8000
    CLOUDINARY_URL - copied from Cloudinary Dashboard API Environment variable and pasted starting from 'cloudinary://...'
    ```

8. Within the settings.py in the workspace file you need to import several libraries:

    ```python
    import os
    import dj_database_url
    from django.contrib.messages import constants as messages
    if os.path.isfile('env.py'):
    import env
    ```
9. In env.py add the following:

    ```python
    os.environ["DATABASE_URL"] = "postgres://..."
    os.environ["SECRET_KEY"] = <KEY SET UP WITHIN CONFIG VARS IN HEROKU>
    os.environ ["CLOUDINARY_URL"] = "cloudinary://..." >> remove the first part of the url provided from the Cloudinary Dashboard, otherwise it'll fail.
    ```
9. Replace the not secured secret key with os.environ.get('SECRET_KEY)', that we set witin the env.py file
10. Add the following python dictionary:

    ```python
    DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
    ```

11. Tell Django where to store the madia and static files in settings.py:
    * Add Cloudinary in apps:

    ```python
    'cloudinary_storage',
    'cloudinary',
    ```

    * Change the static files settings to link it to Cloudinary:

    ```python
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
    ```

13. In settings.py, under BASE_DIR add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS':

    ```python
    BASE_DIR = Path(__file__).resolve().parent.parent
    TEMLATES_DIR = os.path.join(BASE_DIR, 'templates')

    TEMPLATES = [
        'DIRS' : [TEMPLATES_DIR]
    ]
    ```

14. Add the hostname in settings.py:

    ```python
    ALLOWED_HOSTS = ['<HTTPS HEROKU APP ADDRESS>', 'localhost']
    ```

15. Create a Procfile, so Heroku knows how to run the project. In Procfile add:
    
    ```python
    web: gunicorn APP-NAME.wsgi
    ```
 
16. In Heroku navigate to the "Deploy" section.
    * Scroll down to "Deployment Method" and select "GitHub".
    * Authorize the connection of Heroku to GitHub.
    * Search for your GitHub repository name, and select the correct repository.
    * For Deployment there are two options, Automatic Deployments or Manual.
        - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
        - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so. 
17. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire.
18. Before deploying the final draft of your project you must:
    * Remove staticcollect=1 from Config Vars within Heroku
    * Ensure DEBUG is set to False in settings.py file


# Credits and Acknowledgments 
* [Crycle Truly](https://www.youtube.com/c/CryceTruly) for his amazing Django tutorials that passed me so much knowledge.
* Huge thank you to my Code Institute amazing fellow students from cohort msletb-nov-2021 and our faciliator Kasia Bogucka.
* Thank you to my mentor Chris Quinn for his precious suggestions.
