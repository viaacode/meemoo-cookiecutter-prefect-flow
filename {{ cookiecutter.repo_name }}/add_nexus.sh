#! /bin/bash
# Add Nexus to the list of repositories
# Path: add_nexus.sh
python_path=$(python -c "import sys; print(sys.executable.replace('bin/python', 'pip.conf'))")
echo [global] >> $python_path
echo "index-url = http://do-prd-mvn-01.do.viaa.be:8081/repository/pypi-all/simple" >> $python_path
echo "trusted-host = do-prd-mvn-01.do.viaa.be" >> $python_path