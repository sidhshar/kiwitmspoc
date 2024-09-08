# Kiwi TMS POC
Kiwi Test Management System POC

- Install Kiwi TCMS
- Setup docker compose using the script
- git clone https://github.com/kiwitcms/Kiwi.git
- cd Kiwi
- sudo docker compose up --build

# Access Kiwi TCMS
Once the services have started, Kiwi TCMS should be accessible at http://<IP> in your browser
- Initialize the database from the UI
- Create the First user using the Register from UI
- docker exec -it kiwi_web /Kiwi/manage.py initial_setup
- Install the requirements
```
pip install -r requirements.txt
```
