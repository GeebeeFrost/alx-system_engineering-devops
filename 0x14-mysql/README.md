Directory created for ALX MySQL project

ERRORS
======
While installing MySQL on server, if error "GPG error: http://repo.mysql.com/apt/ubuntu bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY B7B3B788A8D3785C" is encountered:
Run 
```sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C```
to add public key to server

To change replication source on mysql 5.7*, use
CHANGE MASTER TO
  MASTER_HOST = 'new_primary_ip_or_hostname',
  MASTER_PORT = new_primary_port,
  MASTER_USER = 'replication_user',
  MASTER_PASSWORD = 'replication_password',
  MASTER_LOG_FILE = 'binlog_filename',
  MASTER_LOG_POS = binlog_position;
