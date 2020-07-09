#!/bin/bash

function option_validate() {
    # Option 1 is the input
    # all following are valid options
    local opt_input=$1
    local found=0
    shift
    for i in $@
    do
        if [ $opt_input = $i ]; then
            found=1
        fi
    done
    if [ $found -gt 0 ]; then
        return 0
    else
        return 1
    fi
}

read -p "Enter Action - create/del (def create): " PR_ACTION
if [ -z $PR_ACTION ]; then
    PR_ACTION="create"
fi
option_validate $PR_ACTION "create" "del"
if [ $? -gt 0 ]; then
    echo "-- [x] Illegal Input: $PR_ACTION"
    exit 1
fi

read -p "Enter Language (def Python): " PR_LANG
if [ -z $PR_LANG ]; then
    PR_LANG="python"
fi
option_validate $PR_LANG "python"
if [ $? -gt 0 ]; then
    echo "-- [x] Illegal Input: $PR_LANG"
    exit 1
fi

read -p "Level - easy/medium/hard/pro (def easy): " PR_LEVEL
if [ -z $PR_LEVEL ]; then
    PR_LEVEL="easy"
fi
option_validate $PR_LEVEL "easy" "medium" "hard" "pro"
if [ $? -gt 0 ]; then
    echo "-- [x] Illegal Input: $PR_LEVEL"
    exit 1
fi

read -p "Enter problem name: " PR_NAME
if [ -d "./$PR_LEVEL/$PR_NAME/$PR_LANG" ] && [ $PR_ACTION = "create" ]; then
    echo "-- [x] Project Already exists: $PR_NAME"
    exit 1
fi

PR_PATH="./$PR_LEVEL/$PR_NAME/"
if [ $PR_ACTION = "create" ]; then
    echo "Attempting to create project.."
    echo "|--- Language: $PR_LANG"
    echo "|--- Level: $PR_LEVEL"
    echo "|--- Name: $PR_NAME"
    mkdir -p $PR_PATH
    cp -R "./template/$PR_LANG/" "./$PR_PATH/"
elif [ $PR_ACTION = "del" ]; then
    echo "Attempting to remove project => $PR_PATH"
    [ -d $PR_PATH ] && rm -rf $PR_PATH
else
    echo "Unknown action: $PR_ACTION"
fi
