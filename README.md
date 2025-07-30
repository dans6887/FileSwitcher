# FileSwitcher
File Switcher app specific to PPT agent.


1. Copy the Switch folder to the entuity user home directory
2. Change directory to the Switch directory 
	cd Switch
3. Run the SwitchFiles.py script as sudo by running the following command
	sudo python3 SwitchFiles.py
4. Stop the parkplacetech-collector service and the parkplacetech-agent-updater service
	systemctl stop parkplacetech-collector
	systemctl stop parkplacetech-agent-updater
5. Start the parkplacetech-collector service and the parkplacetech-agent-updater service
	systemctl start parkplacetech-collector
	systemctl start parkplacetech-agent-updater
6. Check the status of the parkplacetech-collector service and the parkplacetech-agent-updater service
	systemctl status parkplacetech-collector
	systemctl status parkplacetech-agent-updater
