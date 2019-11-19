#!/bin/bash

# Add the pip install script here

# user-ms startup on port 3000
# FLASK_APP=user-ms/main.py FLASK_ENV=development flask run
echo "Checking mongo running"
mongo --eval "db.stats()" > /dev/null

MongoResult=$?

if [ $MongoResult -ne 0 ]; then
    echo "mongodb not running. Please run mongodb and try again"
    exit 1
fi

echo "user-ms running on 5000"
python3 backend/user-ms/main.py > userms.log 2>&1 & 
usermspid=$!

echo "course-ms running on 5001"
python3 backend/courseManagement/myapp.py > coursems.log 2>&1 &
coursemspid=$!

echo "blog-ms running on 5002"
python3 backend/blogRecSys/myapp.py > blogms.log 2>&1 &
blogmspid=$!

echo "placements-ms running on 5003"
python3 backend/placements/myapp.py > placements.log 2>&1 &
placementspid=$!

# if ls edu-breeze-ui/build > /dev/null; then
#     echo 'Launching edu-breeze in production mode...'
#     cd edu-breeze-ui/build
#     python3 -m http.server 80 > ui.log 2>&1 &
#     httpserverpid=$!    
# else
    echo 'Launching edu-breeze in dev mode...'
    cd edu-breeze-ui
    npm start
# fi

echo "To kill run"
echo " " kill -9 $usermspid $coursemspid $blogmspid $placementspid $httpserverpid
