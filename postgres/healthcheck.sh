#!/bin/bash

set -Eeo pipefail

if pg_isready -U "$POSTGRES_USER" -q; then
  exit 0
else
  exit $?
fi
