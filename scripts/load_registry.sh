#!/usr/bin/env bash

set -e

REGISTRY_URL="https://raw.githubusercontent.com/ccktaiwan/prospera-registry/main/manifest.yaml"

echo "Loading Prospera registry..."

curl -s $REGISTRY_URL -o registry.yaml

if [ ! -f registry.yaml ]; then
  echo "ERROR: registry manifest could not be loaded"
  exit 1
fi

echo "Registry manifest loaded."

echo "Detected layers:"
grep -E "^(  [a-z_]+:)" registry.yaml | sed 's/://'

echo "Registry initialization complete."
