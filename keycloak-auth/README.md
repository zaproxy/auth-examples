# Keycloak Authentication Examples
A set of authentication and session management examples that uses Keycloak IDP.

## JS Client
A basic js application that authenticates using OIDC. OpenID Connect (OIDC) is an identity layer built on top of the OAuth 2.0 framework. It allows third-party applications to verify the identity of the end-user and to obtain basic user profile information.

From the `js-client` directory
```bash
docker run -i -t -p 5577:80 -v ./src:/usr/local/apache2/htdocs/ httpd:alpine
```
Will run an alpine apache and serve the static web content.

From your browser 
```
http://localhost:5577
```
Which will take you to Keycloak for authentication. Enter the following credentials.

Username: `easy` 
Password: `peasy`

You will be redirected back to the application and `authenticated` alert will pop up.