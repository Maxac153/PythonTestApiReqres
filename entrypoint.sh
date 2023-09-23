#!/bin/bash

py.test --alluredir=allure_report tests/

if [ $? -ne 0 ]
then
    echo '::error::Tests failed. Refer to the "Checks" tab for details.'
fi
