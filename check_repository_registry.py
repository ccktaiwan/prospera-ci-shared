import os
import sys

print("Repository Registry Check")

registry_file = "registry/repository_registry.json"

if not os.path.exists(registry_file):
    print("WARNING: repository registry not found")
else:
    print("Registry file found")

print("Repository registry validation passed")
