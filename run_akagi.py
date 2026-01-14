import sys
import os

# Add vendor directory to module search path
vendor_dir = os.path.join(os.path.dirname(__file__), 'vendor')
sys.path.insert(0, vendor_dir)

from akagi.akagi import main

if __name__ == "__main__":
    main()