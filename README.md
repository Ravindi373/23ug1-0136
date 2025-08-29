# CCS3308 Assignment 1 – Dockerized Web App


### **Deployment Requirements**

* **Docker** – For running the application inside containers.
* **Docker Compose** – For managing multiple containers together.
* **Python & Flask** – Backend web framework.
* **Redis** – For caching/storing temporary data.

---

### **Application Description**

The application is a small web system that runs inside Docker containers. It allows users to access the service from a browser, while backend services (like Redis) work in separate containers.

---

### **Network and Volume Details**

* **Networks**: A virtual Docker network is created so containers can communicate with each other (e.g., app ↔ Redis).
* **Volumes**: Named volumes are used to store data persistently, so it is not lost when containers stop.

---

### **Container Configuration**

* Each service is defined in a **docker-compose.yml** file.
* Containers are configured with specific ports, environment variables, and mounted volumes.
* Services are connected to the same Docker network for communication.

---

### **Container List**

1. **App Container** – Runs the Flask application.
2. **Redis Container** – Provides caching/storage support.




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

