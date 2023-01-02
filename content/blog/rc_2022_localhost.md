+++
title = "RC 2022 - localhost and docker"
date = 2022-10-10
+++

I pair programmed with Niccolo on his project and we came across an interesting issue: we couldn't connect to a server running in a docker container.  

It turned out that we were still serving the server from `127.0.0.1`, which didn't work once it was dockerised.

## what is localhost?
localhost is the name of the address that points to a computer's own local loopback interface.  This address is usually `127.0.0.1` (it's configured in your /etc/hosts file on Linux).

A [loopback interface](https://en.wikipedia.org/wiki/Loopback#LOOPBACK-INTERFACE) is a virtual network implemented in the operating systems networking software.  It allows programs on the computer to communicate with each other as if they were communicating over a network.  Data sent via this interface doesn't actually reach the networking hardware: it's a virtual local only network.

The main use cases for this virtual interface are security and testing.  It prevents local servers being accessed remotely, for an example an internal database running on the same server as an API or a game engine being run on a personal computer.  It's useful for development and testing because it allows programs to be run locally and securely the same as they will be run in production - the only thing that changes is the address.

## localhost within a docker container
localhost from within a docker container is only accessible from within the docker container.  To expose the server to the host machine, the address should be changed to `0.0.0.0` (note: the port still needs to be mapped to a port on the host machine).
