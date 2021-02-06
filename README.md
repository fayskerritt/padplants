# **Pad Plants**
## Milestone Project 3: Backend Development - Code Institute
## By Fay Skerritt

Pad Plants is a community web app that allows users to view a variety of house plants with specific details about how to care for them in your home. Users can register a profile on the site which will allow them to add, edit and delete plants on the web app.

# Demo 
Live demo can be viewed [here, deployed to Heroku](https://pad-plants.herokuapp.com/)

![Mockup](static/img/readme/mockup.png)

# UX
## User Stories
### New User
* As a new user, I want to understand the main purpose of the site, so I can learn more about the site’s features.
* As a new user, I want to see tha plants featured on the website, so I can learn more about plants.
* As a new user, I want to be shown where I can buy plants, so I can purchase a house plant.

### Returning User
* As a returning user, I want to register to the site, so I have my own profile to store my information.
* As a returning user, I want to add plants to the database, so I can share my plant knowledge with the community.
* As a returning user, I want to have access to all plants added by other members, so I can benefit from other people's knowledge.
* As a returning user, I want to be able to logout of my profile, so I can keep my data safe.

### Frequent User
* As a frequent user, I want to edit my added plants, so I can keep the information current.
* As a frequent user, I want to search for specific plants, so I can find information about plants I own.
* As a frequent user, I want to be able to delete my added plants, so I can ensure no duplicates in the database.
* As a frequent user, I want to view all plants with specific filters, so I can choose a new house plant to suit my needs.

### Site Owner/Developer
* As the owner/developer, I want to expand my database of plants, so I can broaden my knowledge.
* As the owner/developer, I want to redirect users to a store, so I can gain sales from people intereted in plants.
* As the owner/developer, I want to grow my community of plant lovers, so I have an audience of potential customers.

## Design
### **Colour Scheme**
* Green was chosen as it complimented the photos of the plants nicely. Also was in keeping with the green of the leaves
* A range of greens were chosen for different attributes:
    * A darker green  ![#62985b](https://placehold.it/15/62985b/000000?text=+) `#62985b` for the Navbar and Footer with white text for easier viewing and contrast.
    * A lighter and softer green ![#83c17b](https://placehold.it/15/83c17b/000000?text=+) `#83c17b` was used for the bottom border of the headings for a subtle underline.
    * Another lighter green ![#9ec799](https://placehold.it/15/9ec799/000000?text=+) `#9ec799` was used for the background of the banner where flash messages are displayed so these stood out from the other elements.
    * A more prominent green ![#95e380](https://placehold.it/15/95e380/000000?text=+) `#95e380` was used for the hover of buttons and links.

![Mockup](static/img/readme/colourscheme.png)

### **Typography**
* Roboto was chosen for the font to go with the linear pattern of the site. It was thought that anything too fancy wouldn't have gone well with the house plant images.

### **Imagery**
* The home page features two artistic images of houseplants, which capture the eye and go well with the green colour theme.
* The profile and 404 pages also feature artistic imagery of houseplants which are inkeeping with the theme.
* Font Awesome icons are used in areas to clearly label input fields and headers.
* Each plant has an image at the top of the card which shows the user exactly what the plant looks like.

### **Wireframes**
**Home page:**

* 2 column structure on larger screens which changes to 1 on smaller screens. Had to use a Bootstrap row-reverse class to switch the second image and text to show opposite to the top whilst still showing text - image - text - image on a mobile device.
    * Figma screenshot - [Home](https://)

**Plants page:**

* Wireframe shows a hero image but during development the page looked too busy with an image so left that out.
    * Figma screenshot - [Plants](https://)

**Profile page:**

* Image added to the side of the Username as page looked quite bare for new users.
    * Figma screenshot - [Profile](https://)

**Add Plant page:**

* Page copied to create Edit page by filling in the inputs from the database
* Font Awesome icons used to represent the 3 different light conditions; Shade, Light & Shade and Direct Sunlight. Also to represent the 5 rooms; Bathroom, Bedroom, Living Room, Study and Kitchen.
    * Figma screenshot - [Add Plant](https://)

**Login page:**

* Simple form, ended up adding Font Awesome icons to the Username and Password Labels
    * Figma screenshot - [Login](https://)

**Register page:**

* Same form layout as Login page with extra input to confirm password, this was to prevent an error when entering their password first time round.
    * Figma screenshot - [Register](https://)


# Features
### Existing Features
* Registration - Creating a profile using a unique username and password which is stored in the database, the password will be hashed for better security.
* Displaying database of plants on the Plants page - Pulling the data from MongoDB to display the list of all plants in the database with all fields displayed nicely in their own individual cards.
* Adding a plant - Creating a plant and adding it to the database using the Add Plant form. This allows the user to input the name, botanical name and a description. There are two drop downs for the user to choose the size and how often the plant needs watering. There are also two lots of radio checkboxes that the user can choose how much light the plant needs and which room the plant goes best in. Finally there is an input for the user to add a URL for an image, however if the URL doesn't work then the image displayed will be a default image.
* Editing a plant you have addded - An edit button will be available to edit the fields of a plant you have added, the previously chosen fields will be autofilled on the Edit page. The Admin user profile has access to edit all plants.
* Deleting a plant you have added - A delete button will be available to delete a plant that you have added. The Admin user profile has access to delete all plants.
* Viewing all plants you have added on your Profile page - Pulling data from MongoDB to display the plants that have been added by the user that is logged in, this uses the 'created by' field.
* Searching the database - 
    * The search has the option of a text input, which searches the plant name, botanical name and description fields. 
    * Two drop down menus that allow the user to search by room and by size. 
    * Two check boxes that allow the user to filter the list by plants that are happy in low light and plants that do not need watering very often. 
    * You can combine all these search fields to find the perfect plant for you.
* Different buttons and options visible depending on logged in status - 
    * Register and Login options in the navbar are visible before logging in, which are hidden to show the Logout option once logged in. 
    * Register button on the home page changes to Browse once logged in. 
    * Edit and Delete buttons are only visible against plants that the logged in user has created.
    * Edit and Delete buttons are visible on all plants to the Admin user.
* Visible buttons when no search results found - 
    * If no plants are found when using the search functionality then a message will show and an Add button will be visible.
    * If no plants have been added yet by the current user, a message and Add button will show on the profile page.
* Responsiveness - As can be seen in the mockup at the top of this README the site is responsive across all sizes of device. The Bootstrap Grid framework was used to enable this.
* Defensive Programming - A modal is used to ask the user if they are sure they want to delete a plant when the Delete button is clicked.
* Interactive Navbar that displays a bottom border when hovering as well as bolder font on the page that is active.
* An external link is present on the home page with the option to buy plants, this sends users to an Amazon page currently.
* Social Media links in the footer - Links to social media pages increase engagement with users.


### Features to Implement in the Future
* Pagination on the Plants page as the database grows.
* A link to an active selling page to be added to the home page to gain sales from community members.
* A link option on each plant card to send the user to a site where the plant is available to buy.

# Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) - To build templates for website pages.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - To style the HTML content to make the site look nice and display nicely on the page.
* [Python3](https://www.python.org/) - To write scripts that get and post data to the MongoDb Database.
* [jQuery](https://jquery.com/) - To simplify DOM manipulation for Bootstrap
* [MongoDB](https://www.mongodb.com/) - To create a plant database that stores information entered from the Pad Plants web app.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - To create a flask app in Python that is backed by MongoDB and allows for routing to be coded for the different pages and functions of the web app.
* [Jinja](https://palletsprojects.com/p/jinja/) - Templating used in HTML files as a link for the Python expressions and functions.
* [Werkzeug](https://pypi.org/project/Werkzeug/) - To debug code when an error is highlighted, also for password hashing as a security helper.
* [Pymongo](https://pypi.org/project/pymongo/) - To simplify the communihcations between the flask app and the Mongo database.
* [Python.OS](https://docs.python.org/3/library/os.html) - To set the default environment variables for the web app.
* [BSON.ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId/) - To find documents in MongoDB by rendering the ObjectId.
* [GitHub](https://github.com/) - To store the the project once pushed from Gitpod.
* [Git](https://git-scm.com/) - For Version control by using the Gitpod terminal to add, commit and push the code to GitHub.
* [Bootstrap](https://getbootstrap.com/) - Template used to ensure site is responsive as well as for styling objects as a base for own CSS.
* [Figma](https://www.figma.com/file/HC618UdxHcbhAvexrrO5Hp/Milestone-2-Wireframes) - To create wireframes, logo, favicon and the colour chart for README.
* [Google Fonts](https://fonts.google.com/) - Roboto font used for all pages of web app.
* [Font Awesome](https://fontawesome.com/) - To display icons used for better readability.


# Testing
### Code Validation
* HTML Validator
* CSS Validator
* 


# Deployment

### Creation of database on MongoDB:
* Once registered and logged in to [MongoDB](https://www.mongodb.com/) a database was created named 'pad-plants' and a document was added to the collection with the following 'key: value' pairs:

    `_id:` ObjectId("601d0df2d8826e322ef74701")\
    `name:` "Swiss Cheese Plant"\
    `botanical_name:` "Monstera Deliciosa"\
    `description:` "A green plant with heart shaped leaves that develop as the plant grows..."\
    `watering:` "7-10"\
    `size:` "Medium"\
    `light_needed:` "Light and Shade"\
    `room:` "Living Room"\
    `img_url:` "https://images.unsplash.com/photo-1510505751526-76254482fd38?ixid=MXwx..."

* These keys were then used when adding any more plants to the database.

### Deploy App to Heroku
*In Gitpod:*

Once the Flask App is created with all sensitive files including the `env.py` added to the `.gitignore` file: 
* To specify the Python package dependencies to Heroku the requirements.txt file was created using the command `pip3 freeze --local > requirements.txt`.
* The Procfile was also created using the command `echo web: python app.py` to tell Heroku that the `app.py` file uses the Python language.

*In Heroku:*

* A new app was created with the name 'pad-plants'.
* In the 'Deploy Tab' GitHub was connected using the repository name.
* In the 'Settings' tab of Heroku, the Configuration Variabless were added (these are the 'key:value' pairs that were in the `env.py` file).
* Back in the 'Deploy' tab the 'Enable Automatic Deployment' button was clicked to allow automatic updates from GitHub.
* The branch was then deployed from the master.

*In Gitpod:*

* The Mongo database is then wired up to our Flask app by adding the Mongo links to the default environment variables.

### Local Deployment
* On the [GitHub Repository](https://github.com/fayskerritt/padplants), click on the '↓ Code' button.
* Copy the link to clone the repository using the HTTPS tab.
* In your preferred IDE CLI, navigate to the directory you would like to clone to.
* Type `git clone ` followed by the URL you copied from step 3 and press enter.
* Once cloned, all files from workspace will be visible.
* You will need to create an `env.py` that had previously been added to the `.gitignore` file.
* To test type `python3 app.py` into the CLI and open the 8080 port.
* Finally using git you can push this to your own GitHub repository.


# Credits
### Content
* Code Institute - Backend Development Mini Project - Inspiration for code layout and functionality learnt here.

### Media
* The photos used on home.html, profile.html and 404.html are all from [Unsplash](https://unsplash.com/).
* The Logo in the header and footer was made by myself.
* The favicon was also designed and created by myself.

### Acknowledgements
* Mentor sessions helped me figure out how to fix my search functionality to combine checked boxes with text. 


> Stand out text

**Bold Text Large** 
--------

**Bold Text Small**


*Italic Large*
--------

*Italic Small*

