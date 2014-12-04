# test003

## Purpose

This test aims to verify the correct behaviour using Data Packages as sources.

## Prerequisites

N.A.

## Test procedure

* Type the command:

```
$ ciop-run
```

* Verify in the log files that the inputs are passed to the *node* [1].

* Type the command:

```
$ ciop-simwf
```

* Verify in the log files that the inputs are passed to the *node* [1].

 [1]: It should be improved using an immutable data package source, in order to automatically check the inputs. 
