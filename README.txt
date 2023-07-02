This project is for an Art E-Commerece Store.
The website lsits artists and their patinings.

- You can explore the painting by artist
- You can explore the painting in further detail by clicking on it.
- You can add/remove item form cart.
- You can Send contact info to support
- You can complete an order.
- You can view about and Contact us page.

The database was created using the following commands

from miltontours import db, create_app
app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()
quit()

Then seeded in the browser. This feature has now been disabled.
The admin.py contains teh database setup.


To start the site open the site document in your editor and run the 
'run.py' file.
Browse to the link provided - http://127.0.0.1:5000/ and browse the website.

Constant Furstenberg
