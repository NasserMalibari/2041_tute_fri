#!/bin/dash

top_and_bottom() {
    filename=$1
    echo "$filename"
    echo '-------------------'
    sed -n -E -e '1p;$p'  $filename
    # sed -n -e '1p' -e '$p' $filename #   sed -n '$p'
    echo '==================='

}

top_and_bottom $1