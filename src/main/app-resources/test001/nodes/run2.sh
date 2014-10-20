#!/bin/bash

# source the ciop functions (e.g. ciop-log, ciop-getparam)
source ${ciop_job_include}

# define the exit codes
SUCCESS=0
ERR_NOINPUT=4

# add a trap to exit gracefully
function cleanExit ()
{
   local retval=$?
   local msg=""
   case "$retval" in
     $SUCCESS)     msg="Processing successfully concluded";;
     $ERR_NOINPUT) msg="No input provided";;
     *)            msg="Unknown error";;
   esac
   [ "$retval" != "0" ] && ciop-log "ERROR" "Error $retval - $msg, processing aborted" || ciop-log "INFO" "$msg"
   exit $retval
}

trap cleanExit EXIT

# Loops over all inputs
while read inputfile 
do
  # report activity in log
  ciop-log "INFO" "Receveid $inputfile"
done

exit $SUCCESS
