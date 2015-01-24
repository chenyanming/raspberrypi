#!/bin/sh
### BEGIN INIT INFO
# Provides:          spy1_0.sh
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6 
# Short-Description: run spy1_0.py
# Description:
### END INIT INFO

case "$1" in
	start)
		echo "Starting the spy system..."
		sudo python /home/pi/spy1_0.py
		;;
	stop)
		echo "Stopping the spy system..."
		pgrep -l spy1_0.sh
		pgrep -l spy1_0.sh | awk '{print $1}' | sudo xargs kill -9
		;;
	restart)
		;;
	reload)
		;;
	*)
		echo "Usage: start or stop."
		;;
esac
exit 0

