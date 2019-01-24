# dcs-testsuite

## Installation 

* Log on your Developer Cloud Sandbox host

* Install needed packages:

```bash
$ sudo yum install -y esa-beam-4.11 ImageMagick
```

* Run these commands in a shell:

```bash
cd ~
git clone git@github.com:crossi-T2/dcs-testsuite.git
cd dcs-testsuite
mvn clean install -Ddcs.test.id=testid
```

where *testid* is the test id you want to install. For example:

```
mvn clean install -Ddcs.test.id=test001
```

## Available Tests

* [test001 - Developer Cloud Sandbox Hands-On Exercises 1-10](src/main/app-resources/test001/README.md)
* [test002 - ciop-publish feature #9746](src/main/app-resources/test002/README.md)
* [test003 - Data packages as source](src/main/app-resources/test003/README.md)
* [test004 - Workflow ending with multiple nodes](src/main/app-resources/test004/README.md)
* [test005 - WPS Action](src/main/app-resources/test005/README.md)
* [test006 - cioppy: cioppy.publish, default behaviour](src/main/app-resources/test006/README.md)
* [test007 - cioppy: cioppy.publish, mode = recursive](src/main/app-resources/test007/README.md)
* [test008 - cioppy: cioppy.publish, mode = anonymous](src/main/app-resources/test008/README.md)
* [test009 - cioppy: cioppy.getparam](src/main/app-resources/test009/README.md)
* [test010 - cioppy: cioppy.copy, default behaviour](src/main/app-resources/test010/README.md)
* [test011 - cioppy: cioppy.copy, automatic decompression disabled](src/main/app-resources/test011/README.md)
* [test012 - cioppy: cioppy.copy, automatic decompression enabled](src/main/app-resources/test012/README.md)
* [test013 - cioppy: cioppy.log](src/main/app-resources/test013/README.md)
* [test014 - cioppy: cioppy.publish, metalink = false](src/main/app-resources/test014/README.md)
* [test015 - cioppy.publish and cioppy.getparam / Python 3.5](src/main/app-resources/test015/README.md)
