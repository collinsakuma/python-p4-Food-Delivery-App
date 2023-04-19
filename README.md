# Phase 4 Full-Stack Application Project Template

So, to implement a delivery app, we could allow users to add multiple items to their cart by creating a new CartOrder object for each item they add to their cart, with the user_id set to the current user's id and the status set to 'cart'. Each CartOrder object would have an associated Order object that specifies the item and quantity for that order.

Then, when the user is ready to check out, we could update the status of all their CartOrder objects to 'pending' or 'confirmed', depending on the delivery workflow of the app.
