# test001

## Purpose

This test aims to verify the correct behaviour of the complete workflow built through the Developer Cloud Sandbox Hands-On Exercises 1-10.

## Prerequisites

* Install the required packages:

```
$ sudo yum install -y esa-beam-4.11 ImageMagick
```

## Test Procedure

* Start the workflow through `ciop-run`:

```
$ ciop-run
```

* Start the workflow through `ciop-simwf`:

```
$ ciop-simwf
```

* Start the workflow through the *WebProcessingService*:

```
$ curl http://$HOSTNAME:8080/wps/WebProcessingService?service=wps&version=1.0.0&request=Execute&identifier=com.terradue.wps_oozie.process.OozieAbstractAlgorithm&dataInputs=startdate=2012-04-06T10%3A24%3A29.000Z;enddate=2012-04-07;qbbox=2.99%2C58.45%2C0.53%2C58.26;&ResponseDocument=result_distribution&storeExecuteResponse=true&status=true
```

References:

* http://docs.terradue.com/developer-sandbox/developer/index.html
