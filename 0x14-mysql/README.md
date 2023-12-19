Directory created for ALX MySQL project
While installing MySQL on server, if error "GPG error: http://repo.mysql.com/apt/ubuntu bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY B7B3B788A8D3785C" is encountered:
Run 
```sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C```
to add public key to server
