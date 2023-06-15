#

In the Registration process, the Client sends "username" and hash of password
generated "hash(password)" to the Server. The Server inserts the username and
password_hash in its database.

#

Both Client and Server has the password hash.

#

The login process is as follows

1. The user enters username and password on its interface after selecting login.

2. The server sends a "random string" to the client.

3. The Client receives the random string. It encrypts the "password_hash"
with the received random string as key using AES. It sends the encryped stream
to the Server.

4. The Server also does the same encryption as it has the user's password_hash
and the generated random string.

5. The Server compares the cipher stream computed by the Client and by itself.
If they match, the Server grants the login access. If they do not match, the
server rejects the login access.

#

This protocol is a simple implementation of the Challenge-Response
Authentication Protocol which has good security. 

#
