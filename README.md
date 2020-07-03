
# "Project Backend with Vagrant and Docker"

Project Backend uses Vagrant to set up the VM and Docker to deploy the application when the VM is up and ready  

Below are the steps to successfully run project backend  

## Prerequisites

The following programs must be installed on your computer  

Vagrant, git  

## Clone the Repository

1. git clone git@github.com:kmvinoth/backend.git  

## Creating and Activating Virtual Environment

2. cd backend  

## Start the VM

3. vagrant up  

4. docker ps (wiil show the application and database (postgres) continer running, once the vm has started)

## Stop the VM

5. vagrant halt
