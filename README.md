# dcs-testsuite

## Installation 

* Log on your Developer Cloud Sandbox host.

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
