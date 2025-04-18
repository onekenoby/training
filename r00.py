import os
from rpy2.robjects import r


# Set the R_HOME and PATH environment variables if not already set
# Adjust to your R installation path
os.environ['R_HOME'] = r'C:\\Program Files\\R\\R-4.4.1'
# Adjust to your R bin path
os.environ['PATH'] += r';C:\\Program Files\\R\\R-4.4.1\bin\\x64'

# Disable JIT in R
r("library(compiler)")
r("enableJIT(0)")  # Disable JIT

try:
    # Check R version
    print("Testing R connection...")
    r_version = r("version")
    print("R connection successful!")
    print(r_version)
except Exception as e:
    print("Failed to connect to R.")
    print("Error:", e)
