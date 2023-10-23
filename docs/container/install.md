---
tags:
  - Docker Desktop
  - MacOS
  - Windows
icon: simple/docker
---
# Installing Docker Desktop on Windows and macOS

Docker Desktop is a convenient way to run Docker containers on your Windows or macOS machine. It provides an easy-to-use interface for managing containers and orchestrating your development environment. Follow these steps to install Docker Desktop on your system.

## Windows Installation

### Prerequisites

Before installing Docker Desktop on Windows, ensure that your system meets the following requirements:

- Windows 10 Pro, Enterprise, or Education (64-bit)
- Virtualization must be enabled in the BIOS/UEFI settings.
- Hyper-V must be enabled (usually enabled by default in Windows 10 Pro).

### Installation Steps

1. Go to the [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) download page.

2. Download the Docker Desktop for Windows installer.

3. Double-click the installer to run it. You may be prompted for administrator permissions.

4. Follow the installation wizard's instructions to install Docker Desktop.

5. During the installation, you will be asked if you want to use Windows containers or Linux containers. You can select either option or choose to use both.

6. Once the installation is complete, Docker Desktop will start automatically. You'll see the Docker whale icon in your system tray.

## macOS Installation

### Prerequisites

Before installing Docker Desktop on macOS, ensure that your system meets the following requirements:

- macOS 10.13 or newer with macOS Sierra, High Sierra, or Mojave, and at least 4GB of RAM.

### Installation Steps

1. Go to the [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) download page.

2. Download the Docker Desktop for Mac installer.

3. Double-click the installer to open it.

4. Drag the Docker icon into your Applications folder to complete the installation.

5. Launch Docker Desktop from your Applications folder.

6. You may be prompted to provide your system password to allow Docker to make changes. Enter your password to proceed.

7. Docker Desktop will start, and you'll see the Docker whale icon in your macOS menu bar.

## Verifying the Installation

To verify that Docker Desktop is installed and running correctly, open a terminal or command prompt and run the following command:

```bash
docker --version
```
Output:

```plaintext
Docker version 24.0.6, build ed223bc
```

You should see the Docker version displayed, which confirms that Docker Desktop is installed and ready for use.


Run the Container [hello-world](https://hub.docker.com/_/hello-world) Container


In your terminal or command prompt, type the following command and press Enter:

```bash
docker run hello-world
```
Output:

```plaintext
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete 
Digest: sha256:88ec0acaa3ec199d3b7eaf73588f4518c25f9d34f58ce9a0df68429c5af48e8d
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

That's it! You've successfully installed Docker Desktop on your Windows or macOS machine. You can now start creating and managing containers with ease.