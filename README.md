## "Our Antiquities Land" Project
My website is about the most suggested Archaeology sites in Israel.
The website show you small summary about each site with additional functionalities of adding, removing and editing existing site, and looking for the site via the waze..
## Link for web:
[Link](http://127.0.0.1:5000)

## First steps:
- Preparing an external requirements analysis file that contains drawings of the web pages with notes about their routes and names.
- Install relevant libraries: flask, flask-migrate, flask-SQAlchemy, with importing wanted modules like request, redirect, url-for, migrate and Migrate and os.
- Preparing the work environment of Pycharm with flask web framework by building the database (antiquity.db), and creating the flask object application and the content data that include the classes like Reviews and Sites.
- Defining the type of static files (in this project we used only picture).
- Preparing the routes that will be used by the relevant functions to send or to get data from or to specific url or the database.
## Technology:
- Python programming language.
- Flask web framework (code library).
- HTML as the markup language to build the skeleton of the web.
- CSS style sheet langauge to design the web.
- Django web framework with Jinja2 template engine.
- SQLite database.
## Instructions of usage:
- Open the web via the link : http://127.0.0.1:5000
- You can see the main page which include teach site's picture and the names of the sites will be shown with hovering on the picture.
- You can add a new site with add button at the top of the page.
- The logo lead you also to the main current page.
- By clicking on the ADD button it will take you to a new page to add new site, in this page you have to fill all the information to add your new site, fill the location (waze_at) carefully because it is for each site.
- By clicking on the add button the new site will be added to the main page that you will see after click.
- Each picture in the main page is a link to a new page that include data about the relevant site with opportunity to search the site's location via the waze. You can also add your comment about this site, and the comment will be shown in the same page after clicking on add comment button that will take you to the same updated page.
- In the current page you can alter or remove this site from the web, by clicking the alter/ delete buttons at the top of the page.
- The alter button will take you to a new page where you can change any data you want about the relevant site, after clicking on the update button you will see the site's page with updating data.
- Click on the delete button to delete every thing about this site and also the relevant reviews, deleting the current site will take you to the main page where you can see that the main page is updated and the relevant site is deleted there too.
## The project topic:
The project should show information about the top suggested archaeological sites in Israel with possibility to search this site if you want to visit, and leaving a comment if you want.
The relevant data about the sites are their name and a small paragraph about the site and an instruction to find it on waze.
