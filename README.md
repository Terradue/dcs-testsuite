# dcs-testsuite

## Installation 

Log on your Developer Cloud Sandbox host.

Run these commands in a shell:

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
