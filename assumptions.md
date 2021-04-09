Iteration 1:

Assumed there is an online database or list of dictionaries storing information such as usernames, passwords, emails, permission ids and channels on the server.

Assumed that the sockets will already be established on the server to bind, listen and accept information from the client.

Assumed that the client?s sockets will be setup with a port and host for the computer established. The client is assumed to be ready to read, to listen, send and accept information from the server. 

Assumed that when a user pushes a request to the website (i.e. creating a message, forming a channel), the site will be automatically merging and update the screens of all other users when necessary. 

Assumed that the site will automatically allocate permission IDs to users when they register and when they join a channel and that these permission IDs will be able to be viewed by the user (i.e. to implement the function (admin_userpermission_change (?)).

When calling upon the function ?auth_passwordreset_request ()? it is assumed that the sending of emails and validation of a reset_code will be taken care of

Assumed that eventually the server will start deleting unused data and old messages (i.e. if a channel or chat has been out of use for many years the server will delete the channel as to save memory).

Assumed that the site will automatically resolve merging conflicts when two admins edit the same information or message at the same time.

Assumed that all security of the site has been taken care of, (i.e. no person outside of the developer can access the online database storing all the information required for the site such as passwords and messages). 

Assumed that if a user logs in with an unusual IP address (i.e. from an unknown computer or from another country) an email will be sent to the user?s email account confirming whether their account has been hacked. 

Assumed that the site has access to an accurate clock for the function ?message_sendlater ()?

Assumed that the server will be able to successfully respond to HTTP requests 

Assumed that when called 'messsage_sendlater' that the user sending the messasge is authorised to do so.

Assumed that the creator of the channel is already an admin and joins the channel after creating. 

It is assumed that the creator also sends an automatic welcome message which we will use to test our functions. 
    This will be done instead of using message_send as it is less complicated since it isnt neccesary to loop through the dictionary and update everything. 

When calling 'standup_send()' it is assumed that a standup is currently active.

Assumed that messages will be given a unique message ID code.

Assume that the function channel_create will send a welcome message which we will test. 

Assume that anyone can add someone into a public channel. 

Iteration 2:

Users who are admins are admins of Slackr and will have admin permissions in all channels

The message can only be deleted within 2 hours of sending

There are two ways to react to a message, thumbs up/thumbs down 

The message can only be edited within 2 hours of sending

The reset code sent can only be validated within 15 minutes of sending.

The user can only view another user's profiles when they have at least one mutual channel together




