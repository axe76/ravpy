from ftplib import FTP

from requests import delete

from ..config import FTP_SERVER_URL


class FTPClient:
    def __init__(self, host, user, passwd):
        self.ftp = FTP(host)
        print(self.ftp)
        print(self.ftp.welcome)
        print(self.ftp.connect(host="", port=21))
        print(self.ftp)
        self.ftp.set_pasv(True)
        # self.ftp.set_debuglevel(2)
        self.ftp.login(user, passwd)
        self.ftp.set_pasv(True)

    def download(self, filename, path):
        print('Downloading')
        self.ftp.retrbinary('RETR ' + path, open(filename, 'wb').write, blocksize=1024*1000)
        print("Downloaded")

    def upload(self, filename, path):
        self.ftp.storbinary('STOR ' + path, open(filename, 'rb'), blocksize=1024*1000)

    def list_server_files(self):
        self.ftp.retrlines('LIST')

    def delete_file(self, path):
        self.ftp.delete(path)

    def close(self):
        self.ftp.quit()


def get_client(username, password):
    return FTPClient(host=FTP_SERVER_URL, user=username, passwd=password)


def check_credentials(username, password):
    try:
        FTPClient(host=FTP_SERVER_URL, user=username, passwd=password)
        return True
    except Exception as e:
        print("Error:{}".format(str(e)))
        return False
