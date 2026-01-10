#!/bin/bash
echo "Updating system..."
sudo dnf update -y
echo "Cleaning up..."
sudo dnf clean all
echo "Starting firewall..."
sudo ufw enable
sudo ufw status
echo "All done!"
