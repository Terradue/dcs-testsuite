# test005 - WPS Action

## Purpose

This test aims mainly to verify the correct behaviour of the framework using a WPS Oozie action. Minor bugs are verified also (see *Internal references*).

## Prerequisites

* To have a working WPS server that exposes the Application defined in [test001](/src/main/app-resources/test001/README.md)

## Installation

* Type:

```
$ mvn clean install -Ddcs.test.id=test005 -Dogc.wps.access.point=<WPS access point IP/hostname>
```

## Test procedure

* Type the command:

```
$ ciop-run
```

## Internal references

* http://project.terradue.com/issues/12081
* http://project.terradue.com/issues/12158
* http://project.terradue.com/issues/12051
* http://project.terradue.com/issues/9749

