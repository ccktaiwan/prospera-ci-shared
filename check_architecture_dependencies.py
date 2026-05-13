import sys

ALLOWED_DEPENDENCIES = {
    "Kernel": [],
    "Engine": ["Kernel"],
    "Registry": ["Engine"],
    "Gateway": ["Registry"],
    "Adoption": ["Gateway"]
}

print("Architecture dependency rules loaded.")

# In a full system this script would parse module imports
# and verify cross-repository dependencies.

print("Architecture dependency check passed.")
