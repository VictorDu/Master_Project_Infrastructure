#!/bin/bash
set -xe

ls /opt/setup/scripts/

for SCRIPT in /opt/setup/scripts/*; do
  if [ -f "$SCRIPT" -a -x "$SCRIPT" ];  then
    $SCRIPT
  fi
done
