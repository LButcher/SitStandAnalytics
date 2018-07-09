# SitStandAnalytics

### All work for the sit stand data analytics.

## Dependencies:

1. Python 3.7
2. Pandas: Command "pip install --upgrade pandas" in a terminal


### Plan so far:

-- node-red-contrib-pythonshell
	- Run a python file from nodered

1. Desk sensors data to nodered
2. Nodered to sqlite db on pi
3. Nodered monitors sqlite file for changes
4. If a change occurs, run python script to clean all data (need previous data to determine if it's noise or not)
	- Reading dataset over again won't cause any noticeable speed issues with our relatively tiny number of rows
5. On python script update, pass new cleaned data to dashboard