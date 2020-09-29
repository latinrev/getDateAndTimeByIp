# Get Date and Time by IP

Simple script using http://worldtimeapi.org/ API to get and set the date and time (currently only working for windows)

# Why don't just use Windows automatic datetime?

I had a really old computer which had the BIOS battery dead, Windows for some reason didn't want to work and having it start with the date 01/01/2000 was really annoying, so I created this little script which connects to an api that uses HTTP and sets the time in the computer (Couldn't use HTTPS because of the date error on start)

# How do I use it?

Clone the repo

`$ git clone https://github.com/latinrev/getDateAndTimeByIp.git`

Install Requirements
`$ pip install -r requirements.txt `

With the console on the folder do
`$ python time.py`

# How does it work?

It uses requests from the python library to call a datetime api and set the correct datetime in the users PC
