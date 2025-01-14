# Song_server_automation
Automation testing project for song server application

## Project Description
This project contains automated tests for a song server REST API. The tests cover:
- User Management (add/get users, add friends , add/get playlist , change password)
- Song Management (add/get songs, upvote/downvote song , get songs by rating)
- Playlist Management (add song to playlist)
- Non-Functional Testing (performance, load testing)

## Related Projects

- Song Server - The main server implementation

    https://github.com/eytangro/songs_server
    
- Swagger UI Documentation - API documentation and interactive interface

    https://github.com/adam-is-here/song-server-swagger

Author:
Chen Tsafir


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/chentsafir/Song_server_automation.git
    cd Song_server_automation
    ```

2. Configure

    under sources folder change the config.ini file to relevant Port


3.  Create a virtual environment:
    ```bash
    virtualenv venv --python=3.12
    ```
4. Activate the virtual environment:

    windows:
    ```bash
        venv\Scripts\activate.bat
    ```
    linux:
    ```bash
        source venv/bin/activate
    ```
5. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the tests 
    ```bash
    pytest -s        
    ```

