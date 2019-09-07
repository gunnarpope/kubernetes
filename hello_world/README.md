# Docker container and Kubernetes
Notes from "Kubernetes In Action" by Marko Luksa (2018)
## Installation
1. Install docker
	```
	$ sudo apt-get update && sudo apt-get install docker.io
	$ sudo apt-get install nodejs
	```

1. Start Docker
	```
	~/repos/kubernetes/hello_world $ systemctl start docker
	Failed to start docker.service: Unit docker.service is masked.
	~/repos/kubernetes/hello_world $ systemctl unmask docker.service
	Removed /etc/systemd/system/docker.service.
	~/repos/kubernetes/hello_world $ systemctl unmask docker.socket
	~/repos/kubernetes/hello_world $ systemctl start docker.service
	~/repos/kubernetes/hello_world $ systemctl list-unit-files | grep docker
	docker.service                             enabled        
	docker.socket                              enabled
	~/repos/kubernetes/hello_world $ systemctl start docker
	~/repos/kubernetes/hello_world $
	```

1. Create the Dockerfile
	```
	FROM node:y
	ADD app.js /app.js
	ENTRYPOINT ["node", "app.js"]
	```

1. Build a new container image
	```
	~/repos/kubernetes/hello_world $ docker build -t kubia .
	Sending build context to Docker daemon  17.41kB
	Step 1/3 : FROM node:7
	7: Pulling from library/node
	ad74af05f5a2: Pull complete
	2b032b8bbe8b: Pull complete
	a9a5b35f6ead: Pull complete
	3245b5a1c52c: Pull complete
	afa075743392: Pull complete
	9fb9f21641cd: Pull complete
	3f40ad2666bc: Pull complete
	49c0ed396b49: Pull complete
	Digest: sha256:af5c2c6ac8bc3fa372ac031ef60c45a285eeba7bce9ee9ed66dad3a01e29ab8d
	Status: Downloaded newer image for node:7
	 ---> d9aed20b68a4
	Step 2/3 : ADD app.js /app.js
	 ---> 3803ef945a88
	Step 3/3 : ENTRYPOINT ["node", "app.js"]
	 ---> Running in d1fc24745b80
	Removing intermediate container d1fc24745b80
	 ---> 5e94774a20d5
	Successfully built 5e94774a20d5
	Successfully tagged kubia:latest
	```


1. List the available images
	```
		~/repos/kubernetes/hello_world $ docker images
		REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
		kubia               latest              5e94774a20d5        3 minutes ago       660MB

		```

1. Run the docker container
	```
	~/repos/kubernetes/hello_world $ docker run --rm --name kubia-container2 -p 8080:8080 kubia
	Kubia server starting...
	Recieved request from ::ffff:172.17.0.1
	```

1. View the containers running
	```
	~/repos/kubernetes/hello_world $ docker ps
	CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                    NAMES
	c299eb98d841        kubia               "node app.js"       About a minute ago   Up About a minute   0.0.0.0:8080->8080/tcp   kubia-container2
	~/repos/kubernetes/hello_world $ curl localhost:8080
	You've hit c299eb98d841
	```

	That's the response from your app. The ID `c299eb98d841` is the hostname of the docker container and not that of the host machine.  

1. Inspect the container
	```
	~/repos/kubernetes/hello_world $ docker inspect kubia-container2
	[
    	{
        	"Id": "c299eb98d84124abe1158832dbf84b591aa944d955e8fe0cc85b890614e94029",
        	"Created": "2019-09-07T00:48:32.133673942Z",
        	"Path": "node",
        	"Args": [
            	"app.js"
        	],
        	"State": {
            	"Status": "running",
            	"Running": true,
            	"Paused": false,
            	"Restarting": false,
            	"OOMKilled": false,
            	"Dead": false,
            	"Pid": 31828,
            	"ExitCode": 0,
            	"Error": "",
            	"StartedAt": "2019-09-07T00:48:32.896005136Z",
            	"FinishedAt": "0001-01-01T00:00:00Z"
        	},
        	"Image": "sha256:3d4b17221deaeb0686eab96fc4bbd830df7300df2edca9d554969d45218f8af6",
        	"ResolvConfPath": "/var/lib/docker/containers/c299eb98d84124abe1158832dbf84b591aa944d955e8fe0cc85b890614e94029/resolv.conf",
        	"HostnamePath": "/var/lib/docker/containers/c299eb98d84124abe1158832dbf84b591aa944d955e8fe0cc85b890614e94029/hostname",
        	"HostsPath": "/var/lib/docker/containers/c299eb98d84124abe1158832dbf84b591aa944d955e8fe0cc85b890614e94029/hosts",
        	"LogPath": "/var/lib/docker/containers/c299eb98d84124abe1158832dbf84b591aa944d955e8fe0cc85b890614e94029/c299eb98d84124abe1158832dbf84b591aa944d955e8fe0cc85b890614e94029-json.log",
        	"Name": "/kubia-container2",
        	"RestartCount": 0,
        	"Driver": "aufs",
        	"Platform": "linux",
        	"MountLabel": "",
        	"ProcessLabel": "",
        	"AppArmorProfile": "docker-default",
        	"ExecIDs": null,
        	"HostConfig": {
            	"Binds": null,
            	"ContainerIDFile": "",
            	"LogConfig": {
                	"Type": "json-file",
                	"Config": {}
            	},
            	"NetworkMode": "default",
            	"PortBindings": {
                	"8080/tcp": [
                    	{
                        	"HostIp": "",
                        	"HostPort": "8080"
                    	}
                	]
            	},
            	"RestartPolicy": {
                	"Name": "no",
                	"MaximumRetryCount": 0
            	},
            	"AutoRemove": true,
            	"VolumeDriver": "",
            	"VolumesFrom": null,
            	"CapAdd": null,
            	"CapDrop": null,
            	"Dns": [],
            	"DnsOptions": [],
            	"DnsSearch": [],
            	"ExtraHosts": null,
            	"GroupAdd": null,
            	"IpcMode": "shareable",
            	"Cgroup": "",
            	"Links": null,
            	"OomScoreAdj": 0,
            	"PidMode": "",
            	"Privileged": false,
            	"PublishAllPorts": false,
            	"ReadonlyRootfs": false,
            	"SecurityOpt": null,
            	"UTSMode": "",
            	"UsernsMode": "",
            	"ShmSize": 67108864,
            	"Runtime": "runc",
            	"ConsoleSize": [
                	0,
                	0
            	],
            	"Isolation": "",
            	"CpuShares": 0,
            	"Memory": 0,
            	"NanoCpus": 0,
            	"CgroupParent": "",
            	"BlkioWeight": 0,
            	"BlkioWeightDevice": [],
            	"BlkioDeviceReadBps": null,
            	"BlkioDeviceWriteBps": null,
            	"BlkioDeviceReadIOps": null,
            	"BlkioDeviceWriteIOps": null,
            	"CpuPeriod": 0,
            	"CpuQuota": 0,
            	"CpuRealtimePeriod": 0,
            	"CpuRealtimeRuntime": 0,
            	"CpusetCpus": "",
            	"CpusetMems": "",
            	"Devices": [],
            	"DeviceCgroupRules": null,
            	"DiskQuota": 0,
            	"KernelMemory": 0,
            	"MemoryReservation": 0,
            	"MemorySwap": 0,
            	"MemorySwappiness": null,
            	"OomKillDisable": false,
            	"PidsLimit": 0,
            	"Ulimits": null,
            	"CpuCount": 0,
            	"CpuPercent": 0,
            	"IOMaximumIOps": 0,
            	"IOMaximumBandwidth": 0,
            	"MaskedPaths": [
                	"/proc/asound",
                	"/proc/acpi",
                	"/proc/kcore",
                	"/proc/keys",
                	"/proc/latency_stats",
                	"/proc/timer_list",
                	"/proc/timer_stats",
                	"/proc/sched_debug",
                	"/proc/scsi",
                	"/sys/firmware"
            	],
            	"ReadonlyPaths": [
                	"/proc/bus",
                	"/proc/fs",
                	"/proc/irq",
                	"/proc/sys",
                	"/proc/sysrq-trigger"
            	]
        	},
        	"GraphDriver": {
            	"Data": null,
            	"Name": "aufs"
        	},
        	"Mounts": [],
        	"Config": {
            	"Hostname": "c299eb98d841",
            	"Domainname": "",
            	"User": "",
            	"AttachStdin": false,
            	"AttachStdout": true,
            	"AttachStderr": true,
            	"ExposedPorts": {
                	"8080/tcp": {}
            	},
            	"Tty": false,
            	"OpenStdin": false,
            	"StdinOnce": false,
            	"Env": [
                	"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                	"NPM_CONFIG_LOGLEVEL=info",
                	"NODE_VERSION=7.10.1",
                	"YARN_VERSION=0.24.4"
            	],
            	"Cmd": null,
            	"ArgsEscaped": true,
            	"Image": "kubia",
            	"Volumes": null,
            	"WorkingDir": "",
            	"Entrypoint": [
                	"node",
                	"app.js"
            	],
            	"OnBuild": null,
            	"Labels": {}
        	},
        	"NetworkSettings": {
            	"Bridge": "",
            	"SandboxID": "115c22523f087ab89fbaf46a81e0803e189b6c32560f2be4e31545895492022b",
            	"HairpinMode": false,
            	"LinkLocalIPv6Address": "",
            	"LinkLocalIPv6PrefixLen": 0,
            	"Ports": {
                	"8080/tcp": [
                    	{
                        	"HostIp": "0.0.0.0",
                        	"HostPort": "8080"
                    	}
                	]
            	},
            	"SandboxKey": "/var/run/docker/netns/115c22523f08",
            	"SecondaryIPAddresses": null,
            	"SecondaryIPv6Addresses": null,
            	"EndpointID": "5129d85a8b2a812a1bb4f04304ebd57c2b99de7e2745517fecfd2c72d818a936",
            	"Gateway": "172.17.0.1",
            	"GlobalIPv6Address": "",
            	"GlobalIPv6PrefixLen": 0,
            	"IPAddress": "172.17.0.2",
            	"IPPrefixLen": 16,
            	"IPv6Gateway": "",
            	"MacAddress": "02:42:ac:11:00:02",
            	"Networks": {
                	"bridge": {
                    	"IPAMConfig": null,
                    	"Links": null,
                    	"Aliases": null,
                    	"NetworkID": "75e1e9fcd0aa94918c886adff4d068a8a76c6dfe25e374161bbc0fb6116ebdfd",
                    	"EndpointID": "5129d85a8b2a812a1bb4f04304ebd57c2b99de7e2745517fecfd2c72d818a936",
                    	"Gateway": "172.17.0.1",
                    	"IPAddress": "172.17.0.2",
                    	"IPPrefixLen": 16,
                    	"IPv6Gateway": "",
                    	"GlobalIPv6Address": "",
                    	"GlobalIPv6PrefixLen": 0,
                    	"MacAddress": "02:42:ac:11:00:02",
                    	"DriverOpts": null
                	}
            	}
        	}
    	}
			]

			```

1. Stop the container
	```
	~/repos/kubernetes/hello_world $ docker stop kubia-container2
	kubia-container2
	```
