# CCS3308 Assignment 1 – Dockerized Web App



#before running the application i created a folder named ccs3308_assinment01
#then inside that created the files as follows 

 -web - app
      - Docker file
      - requirements
 -docker-compose
 -prepare-app
 -remove-app
 -start-app
 -stop-app

#then inserted the required codes and cli into the files and run the application inside the terminal as follows

## Steps to Run

```bash
# 1. Prepare environment (builds Docker images, installs dependencies)
./prepare-app.sh

# 2. Start the application (runs containers)
./start-app.sh

# 3. Stop the application (stops containers but keeps data)
./stop-app.sh

# 4. Remove the application (cleans up containers, images, and volumes)
./remove-app.sh

